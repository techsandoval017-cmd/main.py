import os
import sys
import json
import urllib.request
import urllib.error

# 1. Extraer la clave limpia de .env
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
    print("❌ ERROR: No se encontró GEMINI_API_KEY en .env ni en el entorno.")
    sys.exit(1)

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"

tareas = [
    ("Agente eCommerce", "Generar el backend mock en Python de busqueda de catalogo y link directo de checkout para WhatsApp."),
    ("Agente Mensajeria", "Generar el flujo de conversacion y confirmacion de anticipo para turnos de talleres o barberias."),
    ("Agente Pagos", "Generar funcion que arme links de pago para SPEI/Mercado Pago y Stripe Checkout segun la moneda."),
    ("Agente Contenido", "Generar el script que exporte a CSV 20 variaciones de copys y precios para crear creativos en Canva Pro."),
    ("Agente Infraestructura", "Generar el esquema SQLite con tablas de citas, carritos y control de existencias sin duplicados."),
    ("Agente Legal", "Generar el borrador base de contrato comercial y politicas de servicio para venta de software.")
]

print("===================================================================")
print("🚀 FÁBRICA TECH SANDOVAL: PRODUCCIÓN COMPLETA DE 6 AGENTES")
print("===================================================================")

memoria = {}
headers = {"Content-Type": "application/json; charset=utf-8"}

for rol, tarea in tareas:
    print(f"⚙️  {rol} ejecutando...", flush=True)
    prompt = (
        f"Eres el {rol} de Tech Sandoval.\n"
        f"ORDEN TECNICA: {tarea}\n"
        "Entrega unicamente el codigo o plantilla mock listo para usar.\n"
        "Al final incluye una seccion llamada 'APRENDIZAJE_REUTILIZABLE' con 2 reglas fijas."
    )
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    data_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            texto = data["candidates"][0]["content"]["parts"][0]["text"]
            memoria[rol] = texto
            print(f"✅ {rol}: Completado con éxito.", flush=True)
    except urllib.error.HTTPError as e:
        error_detail = e.read().decode("utf-8", errors="ignore")
        memoria[rol] = f"Error {e.code}: {error_detail}"
        print(f"❌ {rol}: Error {e.code} -> {error_detail[:150]}", flush=True)
    except Exception as e:
        memoria[rol] = f"Error: {e}"
        print(f"❌ {rol}: {e}", flush=True)

with open("/workspaces/main.py/memoria_fabrica.json", "w", encoding="utf-8") as f:
    json.dump(memoria, f, indent=2, ensure_ascii=False)

print("\n===================================================================")
print("🎯 PROCESO TERMINADO AL 100%: Revisa 'memoria_fabrica.json'")
print("===================================================================")
