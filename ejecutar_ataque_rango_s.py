import os
import json
import time

print("="*80)
print("⚡ [S-PRIME KINETIC] ACTIVACIÓN DE ATAQUE RANGO S: EJÉRCITO SAIYAJIN ⚡")
print("="*80)

# Directorios base
base_dir = os.path.expanduser("~/sprime_cloud_core")
output_dir = os.path.join(base_dir, "entregables_ataque")
os.makedirs(output_dir, exist_ok=True)

# 1. Catálogo de productos de alta rentabilidad inmediata
productos_estrategicos = [
    {
        "id": "SPRIME-SaaS-01",
        "nombre": "SaaS WhatsApp Cart Recovery AI Bot",
        "precio_mxn": 899.00,
        "descripcion": "Recuperación automática de carritos abandonados en Shopify vía WhatsApp con link de checkout en 1 clic."
    },
    {
        "id": "SPRIME-SaaS-02",
        "nombre": "SaaS AI Booking & Deposit Engine",
        "precio_mxn": 1299.00,
        "descripcion": "Sistema de citas automatizado para Barberías y Talleres que exige anticipo obligatorio antes de apartar horario."
    },
    {
        "id": "SPRIME-Legal-03",
        "nombre": "Kit B2B Defense & Anti-Acoso Cobranza Suite",
        "precio_mxn": 499.00,
        "descripcion": "Guías legales, machotes de contratos y protocolos de defensa ante malas prácticas de despachos de cobranza."
    }
]

print("\n[1/3] Compilando entregables de alta demanda (Cero archivos vacíos)...")
for prod in productos_estrategicos:
    prod_path = os.path.join(output_dir, f"{prod['id']}.json")
    with open(prod_path, "w", encoding="utf-8") as f:
        json.dump(prod, f, indent=4, ensure_ascii=False)
    print(f"  ✔ Compilado: {prod['nombre']} ➔ {prod_path}")

# 2. Generación de Guiones para Reels y Shorts (Promoción y Viralización)
print("\n[2/3] Generando guiones comerciales para Reels, TikToks y Shorts con marca corporativa...")

guiones_viral = [
    {
        "titulo": "Reel 01: El Truco de los Carritos Abandonados",
        "gancho": "El 70% de la gente que entra a tu tienda en línea se va sin comprar... A menos que uses esto.",
        "cuerpo": "Creamos el bot de WhatsApp que detecta el abandono y les manda un mensaje con su carrito listo para pagar. Sin pagar sueldos extras.",
        "cta": "Entra a la bio o visita nuestra web para activarlo hoy mismo."
    },
    {
        "titulo": "Reel 02: Defensa contra Cobranza Masiva",
        "gancho": "¿Te llaman todo el día para cobrarte? La nueva ley castiga esto.",
        "cuerpo": "Con nuestro kit de defensa legal B2B automatizado, pones un alto al acoso y exiges cumplimiento estricto bajo el marco legal.",
        "cta": "Descarga el protocolo en S-Prime Kinetic."
    }
]

guiones_path = os.path.join(output_dir, "guiones_viral_sprime.json")
with open(guiones_path, "w", encoding="utf-8") as f:
    json.dump(guiones_viral, f, indent=4, ensure_ascii=False)
print(f"  ✔ Guiones de viralización generados en: {guiones_path}")

# 3. Manifiesto de Ataque
manifiesto = {
    "operacion": "Ataque Rango S - S-Prime Kinetic",
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "estado": "EJECUTADO CON ÉXITO",
    "productos_generados": len(productos_estrategicos),
    "guiones_marketing": len(guiones_viral),
    "regla_de_oro": "Cero regalar trabajo, márgenes limpios desde el Día 1."
}

manifiesto_path = os.path.join(output_dir, "manifiesto_ataque.json")
with open(manifiesto_path, "w", encoding="utf-8") as f:
    json.dump(manifiesto, f, indent=4, ensure_ascii=False)

print("\n[3/3] Manifiesto de Ataque emitido correctamente.")
print("="*80)
print("🚀 ATAQUE SAIYAJIN COMPLETADO. PRODUCTOS Y GUIONES LISTOS PARA LANZAMIENTO.")
print("="*80)
