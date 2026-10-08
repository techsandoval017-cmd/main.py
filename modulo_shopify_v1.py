import os
import sys
import json
import urllib.request
import urllib.error

# 1. Cargar credenciales desde .env
env_file = "/workspaces/main.py/.env"
creds = {}
if os.path.exists(env_file):
    with open(env_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                creds[k.strip()] = v.strip("'\" \t\r\n")

SHOP_DOMAIN = creds.get("SHOPIFY_STORE_DOMAIN", os.environ.get("SHOPIFY_STORE_DOMAIN", "tech-sandoval.myshopify.com"))
ACCESS_TOKEN = creds.get("SHOPIFY_ADMIN_ACCESS_TOKEN", os.environ.get("SHOPIFY_ADMIN_ACCESS_TOKEN", ""))

if not ACCESS_TOKEN or ACCESS_TOKEN.startswith("("):
    print("⚠️ ATENCIÓN: SHOPIFY_ADMIN_ACCESS_TOKEN no configurado o con marcador de posición.")
    print("Modo de simulación (MOCK) activo para pruebas de arquitectura.\n")

def listar_primeros_productos(limite=5):
    """Consulta los productos mediante la Admin API GraphQL de Shopify."""
    if not ACCESS_TOKEN or ACCESS_TOKEN.startswith("("):
        return {
            "modo": "MOCK_SIMULADO",
            "productos": [
                {"id": "gid://shopify/Product/1001", "title": "Agente WhatsApp Bot Pro", "status": "ACTIVE"},
                {"id": "gid://shopify/Product/1002", "title": "Plantilla Canva Bulk Pro", "status": "ACTIVE"}
            ]
        }

    url = f"https://{SHOP_DOMAIN}/admin/api/2024-10/graphql.json"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": ACCESS_TOKEN
    }
    
    query = """
    query GetProducts($first: Int!) {
      products(first: $first) {
        edges {
          node {
            id
            title
            status
            totalInventory
            variants(first: 1) {
              edges {
                node {
                  id
                  price
                }
              }
            }
          }
        }
      }
    }
    """
    payload = {"query": query, "variables": {"first": limite}}
    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error_http": e.code, "detalle": e.read().decode("utf-8", errors="ignore")}
    except Exception as e:
        return {"error_sistema": str(e)}

def generar_checkout_dinamico(variant_id: str, cantidad: int = 1, descuento: str = "WELCOME10"):
    """Construye la URL directa de pago para recuperación de ventas vía WhatsApp."""
    clean_id = variant_id.split("/")[-1] if "/" in variant_id else variant_id
    url_checkout = f"https://{SHOP_DOMAIN}/cart/{clean_id}:{cantidad}?discount={descuento}"
    return {
        "variant_id": clean_id,
        "descuento_aplicado": descuento,
        "enlace_checkout": url_checkout,
        "mensaje_whatsapp": (
            f"Tu pedido en Tech Sandoval está reservado. "
            f"Finaliza tu compra con descuento especial aquí: {url_checkout}"
        )
    }

if __name__ == "__main__":
    print("====================================================")
    print("🛍️  CONECTOR OFICIAL SHOPIFY - TECH SANDOVAL (v1)")
    print(f"Tienda: {SHOP_DOMAIN}")
    print("====================================================")
    
    resultado_catalogo = listar_primeros_productos(3)
    print("\n📦 RESULTADO CONSULTA CATÁLOGO:")
    print(json.dumps(resultado_catalogo, indent=2, ensure_ascii=False))
    
    demo_checkout = generar_checkout_dinamico("4102938475", cantidad=1, descuento="PROMO20")
    print("\n🔗 ENLACE DE RECUPERACIÓN GENERADO:")
    print(json.dumps(demo_checkout, indent=2, ensure_ascii=False))
    print("====================================================")
