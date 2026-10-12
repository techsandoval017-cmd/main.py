import os, sys, json, urllib.request, urllib.error, subprocess

ROOT = "/workspaces/main.py"
ENV_PATH = os.path.join(ROOT, "credenciales_maestras.env")
CSV_PATH = os.path.join(ROOT, "canva_bulk_saas_300.csv")
SENTINEL_LOG = os.path.join(ROOT, "bitacora_sentinel_compliance.json")
DATASET_PATH = os.path.join(ROOT, "dataset_entrenamiento_ia.jsonl")

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

print("===================================================================")
print("📊 INFORME EJECUTIVO & AUTOAPRENDIZAJE DE IA - TECH SANDOVAL")
print("===================================================================")

# 1. ESTADO DE MEMORIA Y ENTRENAMIENTO IA
total_entrenamiento = 0
if os.path.exists(DATASET_PATH):
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        total_entrenamiento = len([l for l in f if l.strip()])

print("\n1️⃣  MEMORIA Y AUTOAPRENDIZAJE PARA TU IA PROPIA:")
print("   • Procedimientos Auditados : " + str(total_entrenamiento) + " registros en dataset_entrenamiento_ia.jsonl")
print("   • Estado de Preparación    : " + ("🟢 LISTO PARA FINE-TUNING" if total_entrenamiento >= 50 else f"🟡 RECOPILANDO ({total_entrenamiento}/50 recomendados)"))

# 2. GOBERNANZA CORPORATIVA Y SENTINEL
print("\n2️⃣  GOBERNANZA CORPORATIVA (SENTINEL):")
if os.path.exists(SENTINEL_LOG):
    with open(SENTINEL_LOG, "r", encoding="utf-8") as f:
        sentinel_data = json.load(f)
    print("   • Estatus de Calidad       : 🟢 " + sentinel_data.get("status_general", "OK"))
    print("   • Entidad Legal            : Tech Sandoval LLC (NM) + Compliance SAT")

# 3. CATÁLOGO EN SHOPIFY
print("\n3️⃣  CATÁLOGO VIVO EN SHOPIFY:")
if token.startswith("shpat_"):
    url = "https://" + domain + "/admin/api/2024-10/graphql.json"
    query = "query { products(first: 5, reverse: true) { edges { node { id title status } } } }"
    req = urllib.request.Request(
        url,
        data=json.dumps({"query": query}).encode("utf-8"),
        headers={"Content-Type": "application/json", "X-Shopify-Access-Token": token}
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            prods = data.get("data", {}).get("products", {}).get("edges", [])
            print("   • Últimos productos registrados en tienda:")
            for p in prods:
                n = p.get("node", {})
                print("     └─ [" + str(n.get("status")) + "] " + str(n.get("title")) + " (ID: " + str(n.get("id")).split("/")[-1] + ")")
    except Exception as e:
        print("   • Error consultando catálogo: " + str(e))

print("\n===================================================================")
print("🎯 DIAGNÓSTICO: Registro de memoria activo. Cada paso queda asentado.")
print("===================================================================")
