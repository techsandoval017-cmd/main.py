import os
import sys
import json
import subprocess

# 1. Extraer API KEY limpia de .env
api_key = ""
env_path = "/workspaces/main.py/.env"
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.strip().startswith("GEMINI_API_KEY="):
                val = line.strip().split("=", 1)[1]
                api_key = val.strip("'\" \t\r\n")
                break

if not api_key:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip("'\" \t\r\n")

if not api_key:
    print("ERROR: No se encontro GEMINI_API_KEY.")
    sys.exit(1)

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"

tareas = [
    ("Agente eCommerce", "Generar el backend mock en Python de busqueda de catalogo y link directo de checkout para WhatsApp."),
    ("Agente Mensajeria", "Generar el flujo de conversacion y confirmacion de anticipo para turnos de barberia."),
    ("Agente Pagos", "Generar funcion que arme links de pago para SPEI/Mercado Pago y Stripe Checkout segun la moneda."),
    ("Agente Contenido", "Generar el script que exporte a CSV 20 variaciones de copys y precios para crear creativos en Canva Pro."),
    ("Agente Infraestructura", "Generar el esquema SQLite con tablas de citas, carritos y control de existencias sin duplicados."),
    ("Agente Legal", "Generar el borrador base de contrato comercial y politicas de servicio para venta de software.")
]

print("===================================================================")
print("🚀 FABRICA TECH SANDOVAL: PRODUCCION CON CURL NATIVO (100% BLINDADO)")
print("===================================================================")

memoria = {}

for rol, tarea in tareas:
    print(f"⚙️  {rol} ejecutando...", flush=True)
    prompt = (
        f"ROL: {rol} de Tech Sandoval.\n"
        f"ORDEN TECNICA: {tarea}\n"
        "Entrega unicamente el codigo o plantilla mock listo para usar.\n"
        "Al final incluye una seccion llamada 'APRENDIZAJE_REUTILIZABLE' con 2 reglas tecnicas fijas."
    )
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    temp_json = f"/tmp/payload_{abs(hash(rol))}.json"
    with open(temp_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=True)
    
    cmd = [
        "curl", "-s", "-X", "POST", url,
        "-H", "Content-Type: application/json",
        "-d", f"@{temp_json}"
    ]
    
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(proc.stdout)
        if "candidates" in data and len(data["candidates"]) > 0:
            texto = data["candidates"][0]["content"]["parts"][0]["text"]
            memoria[rol] = texto
            print(f"✅ {rol}: Completado con exito.", flush=True)
        else:
            print(f"❌ {rol}: Respuesta vacia o error de API -> {proc.stdout[:150]}")
    except Exception as e:
        print(f"❌ {rol}: Fallo al invocar -> {e}")
    finally:
        if os.path.exists(temp_json):
            os.remove(temp_json)

with open("/workspaces/main.py/memoria_fabrica.json", "w", encoding="utf-8") as f:
    json.dump(memoria, f, indent=2, ensure_ascii=False)

print("\n===================================================================")
print("🎯 PRODUCCION FINALIZADA: Todos los modulos guardados en memoria_fabrica.json")
print("===================================================================")
