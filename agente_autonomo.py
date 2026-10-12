import os
import json
import urllib.request
import urllib.error

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("❌ ERROR: GEMINI_API_KEY no encontrada.")
    exit(1)

def consultar_gemini(prompt_sistema, entrada_usuario):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [
                {"text": f"SISTEMA: {prompt_sistema}\n\nENTRADA: {entrada_usuario}"}
            ]
        }]
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["candidates"][0]["content"]["parts"][0]["text"]
    except urllib.error.HTTPError as e:
        return f"Error HTTP {e.code}: {e.read().decode('utf-8')}"

print("=====================================================")
print("🤖 AGENTE CENTRAL TECH SANDOVAL: FÁBRICA EN EJECUCIÓN")
print("=====================================================")

# SUBAGENTE 1: ANALISTA B2B
print("\n[1/3] 🔍 Subagente Analista B2B ejecutando...")
res_analista = consultar_gemini(
    "Eres el Analista B2B. Define el problema, perfil de cliente y valida viabilidad en 3 viñetas.",
    "Producto: PromptFlow Pro para PYMEs"
)
print(res_analista)

# SUBAGENTE 2: MONETIZACIÓN
print("\n[2/3] 💰 Subagente de Monetización ejecutando...")
res_monetizacion = consultar_gemini(
    "Eres el Estratega de Monetización. Define ticket entre $297 y $597 USD y la oferta irresistible en 3 viñetas.",
    res_analista
)
print(res_monetizacion)

# SUBAGENTE 3: ARQUITECTO
print("\n[3/3] 🛠️ Subagente Arquitecto Técnico ejecutando...")
res_arquitecto = consultar_gemini(
    "Eres el Arquitecto de Software. Define el blueprint técnico y tareas prioritarias en formato estructurado.",
    res_monetizacion
)
print(res_arquitecto)

print("\n=====================================================")
print("✅ CICLO COMPLETADO: Agente y subagentes operando al 100%")
print("=====================================================")
