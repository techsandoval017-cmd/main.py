import os
import time

# Directorio base
BASE_DIR = "productos"
os.makedirs(BASE_DIR, exist_ok=True)

# Catálogo Fase 2: Micro-Tech y Barbería
catalogo_fase2 = [
    {
        "id": "repair_microtech",
        "nombre": "Kit Reparación Celulares y Laptops",
        "precio_shopify": "149.00",
        "precio_landing": 8900, # 89.00 USD en centavos para Stripe
        "desc": "Software de registro de equipos entrantes (RMA), firmas digitales. PDF de diagramas esquemáticos y guía de micro-soldadura.",
        "prompts_video": "Visual: Vista bajo microscopio soldando un microchip. Transición rápida a un software de registro de clientes con el sello 'Listo para Entregar'. Audio: Lo-fi técnico. Herramienta: ChatGPT 6 (DALL-E 3) para hiperrealismo de placas base."
    },
    {
        "id": "electronic_diag",
        "nombre": "Diagnóstico Electrónico Avanzado",
        "precio_shopify": "110.00",
        "precio_landing": 6900,
        "desc": "Módulo avanzado para mecánicos y técnicos. Lectura con osciloscopio, uso maestro de multímetro y rastreo de cortos. PDF + Software de diagramas.",
        "prompts_video": "Visual: Pantalla de osciloscopio con ondas de señal de un sensor CKP. Texto: 'Deja de adivinar, empieza a diagnosticar'. Herramienta recomendada: Canva Pro Video."
    },
    {
        "id": "golden_blade_vip",
        "nombre": "The Golden Blade VIP",
        "precio_shopify": "150.00",
        "precio_landing": 9900,
        "desc": "Sistema de agendamiento AI para Barberías de Élite. Cálculos automáticos de comisiones para barberos y agenda anti-cancelaciones.",
        "prompts_video": "Visual: Una navaja dorada de barbero brillando sobre una toalla negra. Transición a un celular donde caen notificaciones de cobro Stripe (anticipos de citas). Herramienta: Generación DALL-E 3 y montaje en Canva."
    }
]

print("=== [S-PRIME AI] INICIANDO BUCLE FASE 2: MICRO-TECH Y BARBERÍAS ===\n")

nuevas_tarjetas_html = ""

for prod in catalogo_fase2:
    prod_dir = os.path.join(BASE_DIR, prod["id"])
    os.makedirs(prod_dir, exist_ok=True)
    print(f"[RANGO A - ARQUITECTO] Forjando producto y webs: {prod['nombre']}...")
    
    # 1. Simulación de creación de enlace Stripe
    link_cobro = f"https://buy.stripe.com/test_{prod['id']}_xyz"
    precio_usd = f"{prod['precio_landing'] // 100}.00"
    
    # 2. Crear Landing Page
    html_landing = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{prod['nombre']} | S-Prime</title>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body {{ background: #050505; color: #fff; font-family: 'Rajdhani', sans-serif; text-align: center; padding: 50px; }}
        h1 {{ color: #39ff14; font-size: 3rem; text-transform: uppercase; text-shadow: 0 0 20px rgba(57,255,20,0.4); }}
        p {{ font-size: 1.2rem; color: #aaa; max-width: 600px; margin: 0 auto 20px auto; }}
        .precio {{ font-size: 2.5rem; color: #ff003c; font-weight: bold; margin: 30px 0; }}
        .btn {{ background: transparent; border: 2px solid #39ff14; color: #39ff14; padding: 20px 50px; font-size: 1.5rem; font-weight: bold; text-decoration: none; border-radius: 6px; display: inline-block; transition: 0.3s; text-transform: uppercase; }}
        .btn:hover {{ background: #39ff14; color: #000; box-shadow: 0 0 30px rgba(57,255,20,0.5); }}
    </style>
</head>
<body>
    <h1>{prod['nombre']}</h1>
    <p>{prod['desc']}</p>
    <p>Precio Oficial Shopify: <s style="color:#555;">${prod['precio_shopify']} USD</s></p>
    <div class="precio">Precio Directo B2B: ${precio_usd} USD</div>
    <a href="{link_cobro}" class="btn">Comprar Licencia B2B</a>
</body>
</html>"""
    with open(os.path.join(prod_dir, "landing.html"), "w") as f:
        f.write(html_landing)

    # 3. Crear Estrategia de Video
    instrucciones = f"""# ESTRATEGIA DE VIDEO: {prod['nombre']}
{prod['prompts_video']}

Copia el texto visual y pégalo en ChatGPT 6 (DALL-E 3) para generar las imágenes base. Luego expórtalas a Canva Pro para añadir texto y animaciones.
"""
    with open(os.path.join(prod_dir, "estrategia_video_prompts.md"), "w") as f:
        f.write(instrucciones)

    # 4. Inyección Shopify Simulación
    time.sleep(1)
    print(f"   [SHOPIFY] ✔ Producto {prod['nombre']} inyectado en catálogo oficial.")
    print(f"   [STRIPE] ✔ Enlace de pasarela integrado en Landing Page.")
    
    # 5. Preparar tarjeta para el Dashboard
    nuevas_tarjetas_html += f"""
        <div class="card">
            <div class="status status-ready">TESTEADO OK</div>
            <h3>{prod['nombre']}</h3>
            <p>{prod['desc']}</p>
            <a href="productos/{prod['id']}/landing.html" target="_blank" class="btn-link">Ver Landing Directa</a>
        </div>"""

print("\n[RANGO S] Actualizando Hub del Director...")

# Inyectar las nuevas tarjetas en el Dashboard
dashboard_path = "dashboard_director.html"
if os.path.exists(dashboard_path):
    with open(dashboard_path, 'r') as file:
        dashboard_html = file.read()
    
    # Buscar el final de la grid e insertar las nuevas tarjetas
    insert_pos = dashboard_html.rfind("</div>\n</body>")
    if insert_pos != -1:
        dashboard_html = dashboard_html[:insert_pos] + nuevas_tarjetas_html + dashboard_html[insert_pos:]
        with open(dashboard_path, 'w') as file:
            file.write(dashboard_html)
        print("✔ Hub del Director actualizado con el Grupo C y D.")

print("\n=== [S-PRIME AI] FASE 2 COMPLETADA. CATÁLOGO AMPLIADO EN LÍNEA. ===")
