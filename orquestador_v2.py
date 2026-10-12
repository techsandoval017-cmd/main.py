import os, sys, json, urllib.request, urllib.error

ENV_FILE = "/workspaces/main.py/credenciales_maestras.env"
creds = {}

if os.path.exists(ENV_FILE):
    with open(ENV_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                creds[k.strip()] = v.strip()

gemini_key = creds.get("GEMINI_API_KEY", "")
shop_domain = creds.get("SHOPIFY_STORE_DOMAIN", "tech-sandoval.myshopify.com")
shop_token = creds.get("SHOPIFY_ADMIN_ACCESS_TOKEN", "")

print("===================================================================")
print("🚀 TECH SANDOVAL - ORQUESTADOR DE PRODUCCIÓN AUTOMÁTICA")
print("===================================================================")
print(f"Tienda Shopify   : {shop_domain}")
print(f"Shopify Admin API: {'LISTO' if shop_token.startswith('shpat_') else 'PENDIENTE'}")
print(f"Gemini Director  : {'LISTO' if gemini_key.startswith('AIza') else 'MODO AUTÓNOMO LOCAL'}")

# 1. Dataset de Canva sincronizado
csv_path = "/workspaces/main.py/canva_bulk_saas_300.csv"
if not os.path.exists(csv_path):
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write("Producto,Gancho_Viral,Subtitulo,Precio_USD,Llamado_Accion\n")

# 2. Catálogo SaaS listo para procesar y publicar
suite_saas = [
    {
        "titulo": "SaaS WhatsApp Cart Recovery AI Bot",
        "gancho": "¿Ventas perdidas en Shopify?",
        "sub": "Recupera hasta 25% de carritos con checkout en 1 clic",
        "precio": "49.00",
        "desc": "<h3>Recuperación de Carritos en WhatsApp</h3><p>Micro-SaaS conectado por webhook que despacha recordatorios con link dinámico.</p>",
        "tags": ["saas", "whatsapp", "recuperacion-carritos"]
    },
    {
        "titulo": "SaaS AI Booking & Deposit Engine",
        "gancho": "Cero citas canceladas en tu negocio",
        "sub": "Cobra anticipo obligatorio por SPEI o Stripe antes de agendar",
        "precio": "79.00",
        "desc": "<h3>Agenda con Cobro de Anticipo</h3><p>Micro-SaaS para barberías y talleres mecánicos con integración a Google Calendar.</p>",
        "tags": ["saas", "citas", "turnos", "anticipos"]
    },
    {
        "titulo": "SaaS Canva Auto-Publisher Bulk Engine",
        "gancho": "100 creativos en 60 segundos",
        "sub": "Generación masiva de banners desde tu catálogo de Shopify",
        "precio": "39.00",
        "desc": "<h3>Generador Masivo de Banners para Redes</h3><p>Microservicio que ingesta catálogo y genera creativos en Canva listos para pauta.</p>",
        "tags": ["saas", "canva", "marketing-automation"]
    }
]

# 3. Publicación en Shopify mediante GraphQL
url_shopify = f"https://{shop_domain}/admin/api/2024-10/graphql.json"
headers_shopify = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": shop_token
}

mutation = """
mutation CreateProduct($input: ProductInput!) {
  productCreate(input: $input) {
    product {
      id
      title
      status
    }
    userErrors {
      field
      message
    }
  }
}
"""

publicados = 0
for item in suite_saas:
    print(f"\n⚙️  Procesando: {item['titulo']}")
    
    # Agregar a dataset de Canva
    with open(csv_path, "a", encoding="utf-8") as f:
        f.write(f'"{item["titulo"]}","{item["gancho"]}","{item["sub"]}","${item["precio"]} USD","Comprar Ahora"\n')
    print("  🎨 Agregado a dataset Canva Bulk.")
    
    # Publicar a Shopify
    if shop_token.startswith("shpat_"):
        payload = {
            "query": mutation,
            "variables": {
                "input": {
                    "title": item["titulo"],
                    "descriptionHtml": item["desc"],
                    "vendor": "Tech Sandoval SaaS",
                    "productType": "Digital Software / SaaS",
                    "status": "ACTIVE",
                    "tags": item["tags"]
                }
            }
        }
        req = urllib.request.Request(url_shopify, data=json.dumps(payload).encode("utf-8"), headers=headers_shopify, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                prod = data.get("data", {}).get("productCreate", {}).get("product")
                errs = data.get("data", {}).get("productCreate", {}).get("userErrors", [])
                if prod:
                    print(f"  🛍️ Publicado en Shopify -> ID: {prod['id']}")
                    publicados += 1
                elif errs:
                    print(f"  ⚠️ Aviso Shopify: {errs[0]['message']}")
        except Exception as e:
            print(f"  ❌ Error de conexión: {e}")

print("\n===================================================================")
print(f"🎯 INFORME FINAL: {publicados} productos sincronizados en Shopify.")
print(f"📁 Dataset Canva actualizado en: {csv_path}")
print("===================================================================")
