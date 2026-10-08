import os, sys, json, urllib.request, urllib.error, subprocess

ROOT = "/workspaces/main.py"
ENV_PATH = os.path.join(ROOT, "credenciales_maestras.env")
CSV_PATH = os.path.join(ROOT, "canva_bulk_saas_300.csv")
DATASET_PATH = os.path.join(ROOT, "dataset_entrenamiento_ia.jsonl")
SENTINEL_LOG = os.path.join(ROOT, "bitacora_sentinel_compliance.json")
UMBRAL_ENTRENAMIENTO = 50

# 1. Leer variables
creds = {}
if os.path.exists(ENV_PATH):
    with open(ENV_PATH, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                creds[k.strip()] = v.strip()

domain = creds.get("SHOPIFY_STORE_DOMAIN", "tech-sandoval.myshopify.com")
token = creds.get("SHOPIFY_ADMIN_ACCESS_TOKEN", "")
gemini_key = creds.get("GEMINI_API_KEY", "")

# 2. Contar procedimientos en dataset
total_registros = 0
if os.path.exists(DATASET_PATH):
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        total_registros = len([l for l in f if l.strip()])

# 3. Comprobar servidor web
try:
    ps_res = subprocess.run(["pgrep", "-f", "servidor_interfaz.py"], capture_output=True, text=True)
    servidor_ok = bool(ps_res.stdout.strip())
except Exception:
    servidor_ok = False

print("===================================================================")
print("🛡️ TECH SANDOVAL: AUDITORÍA MAESTRA & CENTRO DE OPERACIONES")
print("===================================================================")

print("\n📦 1. INFRAESTRUCTURA ACTIVA:")
print("   • Shopify GraphQL Admin API : " + ("🟢 EN VIVO (Conectado)" if token.startswith("shpat_") else "🔴 FALTANTE"))
print("   • Servidor Web Local (8080) : " + ("🟢 EN LÍNEA" if servidor_ok else "⚪ DETENIDO"))
print("   • Dataset Canva Bulk        : " + ("🟢 LISTO" if os.path.exists(CSV_PATH) else "🔴 PENDIENTE"))
print("   • Director Gemini Cloud     : " + ("🟢 VINCULADO" if gemini_key.startswith("AIza") else "🟡 MODO LOCAL / PENDIENTE"))

print("\n🧠 2. ESTADO DE MEMORIA & AUTOAPRENDIZAJE:")
print("   • Procedimientos Auditados  : " + str(total_registros) + " / " + str(UMBRAL_ENTRENAMIENTO) + " para Fine-Tuning")

# ALERTA DE UMBRAL
if total_registros >= UMBRAL_ENTRENAMIENTO:
    print("\n🚨🚨🚨 ALERTA DE SISTEMA: UMBRAL DE ENTRENAMIENTO ALCANZADO 🚨🚨🚨")
    print("   El dataset cuenta con datos suficientes para entrenar a tu IA propia.")
    print("   -> ESPERANDO TU ORDEN PARA DESPLEGAR EL ENTRENAMIENTO.")
    print("-------------------------------------------------------------------")
else:
    faltan = UMBRAL_ENTRENAMIENTO - total_registros
    print("   • Estado del Umbral         : Acumulando experiencia (" + str(faltan) + " registros restantes)")

print("\n📋 3. LO QUE HACE FALTA PARA EL 100% OPERATIVO:")
pendientes = []
if not gemini_key.startswith("AIza"):
    pendientes.append("Inyectar GEMINI_API_KEY en credenciales_maestras.env")
if not creds.get("STRIPE_SECRET_KEY"):
    pendientes.append("Registrar STRIPE_SECRET_KEY (cuando decidas cobrar con tarjeta)")
if not creds.get("MERCADO_PAGO_ACCESS_TOKEN"):
    pendientes.append("Registrar MERCADO_PAGO_ACCESS_TOKEN (para cobros SPEI en México)")

if not pendientes:
    print("   🟢 Cero pendientes. Sistema operando a capacidad máxima.")
else:
    for idx, p in enumerate(pendientes, 1):
        print("   " + str(idx) + ". " + p)

print("\n===================================================================")
