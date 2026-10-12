import os, sys, json, urllib.request, urllib.error

# 1. Leer credenciales maestras
env_path = "/workspaces/main.py/credenciales_maestras.env"
creds = {}
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                creds[k.strip()] = v.strip()

domain = creds.get("SHOPIFY_STORE_DOMAIN", "tech-sandoval.myshopify.com")
token = creds.get("SHOPIFY_ADMIN_ACCESS_TOKEN", "")

if not token or token.startswith("PEGA_"):
    print("❌ ERROR: SHOPIFY_ADMIN_ACCESS_TOKEN no válido en credenciales_maestras.env")
    sys.exit(1)

url = f"https://{domain}/admin/api/2024-10/graphql.json"
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": token
}

# 2. Catálogo SaaS asignado a los agentes
catalogo_agentes = [
    {
        "agente": "Agente eCommerce",
        "title": "SaaS WhatsApp Cart Recovery AI Bot",
        "desc": "<h3>Recuperación Automática de Carritos en WhatsApp</h3><p>Micro-SaaS listo para conectar por Webhook a Shopify. Detecta abandonos en tiempo real y despacha recordatorios con link dinámico de checkout en 1-clic.</p><ul><li>Aumento del 25% en conversión</li><li>Plantillas interactivas aprobadas por Meta</li><li>Cero mantenimiento de servidor</li></ul>",
        "price": "49.00",
        "tags": ["saas", "whatsapp", "recuperacion-carritos", "micro-saas"]
    },
    {
        "agente": "Agente Mensajería & Citas",
        "title": "SaaS AI Booking & Deposit Engine",
        "desc": "<h3>Sistema de Citas y Anticipos Automatizados</h3><p>Plataforma para barberías, talleres mecánicos y consultorios. Exige y valida el anticipo antes de apartar el horario en Google Calendar.</p><ul><li>Cobro automático de seña/anticipo</li><li>Confirmación por WhatsApp</li><li>Reducción a cero de inasistencias</li></ul>",
        "price": "79.00",
        "tags": ["saas", "citas", "turnos", "anticipos", "ai-booking"]
    },
    {
        "agente": "Agente Contenido & Canva",
        "title": "SaaS Canva Auto-Publisher Bulk Engine",
        "desc": "<h3>Generador Masivo de Creativos e-Commerce</h3><p>Microservicio que ingesta el catálogo de Shopify y genera por lotes 100 imágenes publicitarias en Canva listas para campañas.</p><ul><li>Sincronización directa vía CSV/API</li><li>Formatos para Reels, TikTok y Feed</li><li>Plantillas optimizadas para conversión</li></ul>",
        "price": "39.00",
        "tags": ["saas", "canva", "bulk-content", "marketing-automation"]
    },
    {
        "agente": "Agente Pagos & Finanzas",
        "title": "SaaS Multi-Gateway Webhook Router",
        "desc": "<h3>Enrutador Inteligente de Pagos e IPN</h3><p>Endpoint unificado en FastAPI que procesa eventos de compra, concilia transacciones y actualiza el estado de pedidos automáticamente.</p><ul><li>Recepción unificada de webhooks</li><li>Reintentos automáticos ante fallas</li><li>Seguridad de firma criptográfica</li></ul>",
        "price": "49.00",
        "tags": ["saas", "pagos", "webhooks", "infraestructura"]
    },
    {
        "agente": "Agente Infraestructura",
        "title": "Shopify GraphQL Python Starter Kit Pro",
        "desc": "<h3>Framework Backend para Micro-SaaS en Shopify</h3><p>Código base en Python 3 para consultar, mutar y administrar inventarios de Shopify de forma nativa sin librerías pesadas.</p><ul><li>Autenticación por Access Token</li><li>Manejo de paginación y rate limits</li><li>Dockerizado y listo para producción</li></ul>",
        "price": "59.00",
        "tags": ["dev-tools", "shopify-api", "python", "starter-kit"]
    },
    {
        "agente": "Agente Legal & Compliance",
        "title": "B2B SaaS Legal Agreement & SLA Suite",
        "desc": "<h3>Contratos de Software y Acuerdos de Nivel de Servicio</h3><p>Paquete de contratos comerciales blindados para vender micro-servicios y software a empresas con cláusulas de propiedad intelectual y soporte.</p><ul><li>Términos y condiciones SaaS</li><li>Acuerdo de Nivel de Servicio (SLA)</li><li>Acuerdo de confidencialidad (NDA) bilingüe</li></ul>",
        "price": "67.00",
        "tags": ["legal", "saas-contracts", "sla", "b2b"]
    }
]

mutation = """
mutation CreateProduct($input: ProductInput!) {
  productCreate(input: $input) {
    product {
      id
      title
      status
      variants(first: 1) {
        edges {
          node {
            id
            price
          }
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
"""

print("===================================================================")
print("🤖 ESCUADRÓN DE AGENTES: PUBLICANDO EN SHOPIFY EN VIVO")
print(f"Tienda Destino: {domain}")
print("===================================================================")

registro_publicados = []

for item in catalogo_agentes:
    print(f"\n⚙️ [{item['agente']}] Empaquetando y publicando: {item['title']}...")
    payload = {
        "query": mutation,
        "variables": {
            "input": {
                "title": item["title"],
                "descriptionHtml": item["desc"],
                "vendor": "Tech Sandoval SaaS",
                "productType": "Digital Software / SaaS",
                "tags": item["tags"],
                "status": "ACTIVE"
            }
        }
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            data = res.get("data", {}).get("productCreate", {})
            errs = data.get("userErrors", [])
            if errs:
                print(f"  ⚠️ Error de validación: {errs[0]['message']}")
            else:
                p = data.get("product", {})
                prod_id = p.get("id")
                print(f"  ✅ ¡PUBLICADO CON ÉXITO! -> ID: {prod_id}")
                registro_publicados.append({
                    "agente": item["agente"],
                    "producto": item["title"],
                    "shopify_id": prod_id,
                    "precio": item["price"]
                })
    except Exception as e:
        print(f"  ❌ Error de red con Shopify: {e}")

# Guardar bitácora para entrenamiento futuro
with open("/workspaces/main.py/registro_agentes_shopify.json", "w", encoding="utf-8") as f:
    json.dump(registro_publicados, f, indent=2, ensure_ascii=False)

print("\n===================================================================")
print(f"🎯 MISIÓN CUMPLIDA: {len(registro_publicados)} productos publicados.")
print("📁 Registro guardado en: /workspaces/main.py/registro_agentes_shopify.json")
print("===================================================================")
