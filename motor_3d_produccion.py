import os
import time

BASE_DIR = "productos"
os.makedirs(BASE_DIR, exist_ok=True)

# Catálogo Élite 3D On-Demand
catalogo_3d = [
    {
        "id": "3d_relicario_sukuna",
        "nombre": "Soporte PS5: El Relicario Demoníaco",
        "precio_shopify": "65.00",
        "precio_landing": 4500, # $45.00 en centavos
        "desc": "Soporte táctico para mando impreso en resina oscura. Estética del Rey de las Maldiciones."
    },
    {
        "id": "3d_vacio_purpura",
        "nombre": "Stand Audífonos: Vacío Púrpura",
        "precio_shopify": "80.00",
        "precio_landing": 6000, # $60.00
        "desc": "Busto minimalista con integración de iluminación LED violeta hacia la diadema de los audífonos."
    },
    {
        "id": "3d_magsafe_itachi",
        "nombre": "Cargador MagSafe: Tsukuyomi",
        "precio_shopify": "50.00",
        "precio_landing": 3500, # $35.00
        "desc": "Placa táctica de carga inalámbrica con textura industrial e iluminación LED roja reactiva."
    },
    {
        "id": "3d_organizador_jinwoo",
        "nombre": "Organizador: Ejército de Sombras",
        "precio_shopify": "55.00",
        "precio_landing": 4000, # $40.00
        "desc": "Gestor de escritorio para USBs y Apple Pencil. Detalles en pintura UV morada fluorescente."
    },
    {
        "id": "3d_dock_rick",
        "nombre": "Dock Smartwatch: Nave C-137",
        "precio_shopify": "45.00",
        "precio_landing": 3000, # $30.00
        "desc": "Réplica de la nave. El smartwatch actúa como parabrisas y oculta el cable de carga."
    }
]

print("[RANGO A - ARQUITECTO] Forjando línea de Hardware 3D...")

nuevas_tarjetas = ""

for prod in catalogo_3d:
    prod_dir = os.path.join(BASE_DIR, prod["id"])
    os.makedirs(prod_dir, exist_ok=True)
    
    # 1. Simulación Enlace Stripe
    link_cobro = f"https://buy.stripe.com/test_{prod['id']}_xyz"
    precio_usd = f"{prod['precio_landing'] // 100}.00"
    
    # 2. Crear Landing Page Directa (Modo Oscuro Obsidian)
    html_landing = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{prod['nombre']} | Obsidian 3D</title>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body {{ background: #050505; color: #fff; font-family: 'Rajdhani', sans-serif; text-align: center; padding: 50px; border-top: 5px solid #ff003c; }}
        h1 {{ color: #fff; font-size: 3rem; text-transform: uppercase; text-shadow: 0 0 20px rgba(255,0,60,0.5); }}
        .badge {{ background: rgba(255,0,60,0.1); color: #ff003c; padding: 5px 15px; border: 1px solid #ff003c; border-radius: 20px; font-weight: bold; letter-spacing: 2px; margin-bottom: 20px; display: inline-block; }}
        p {{ font-size: 1.2rem; color: #aaa; max-width: 600px; margin: 0 auto 20px auto; }}
        .precio {{ font-size: 2.5rem; color: #ff003c; font-weight: bold; margin: 30px 0; }}
        .btn {{ background: transparent; border: 2px solid #ff003c; color: #fff; padding: 20px 50px; font-size: 1.5rem; font-weight: bold; text-decoration: none; border-radius: 6px; display: inline-block; transition: 0.3s; text-transform: uppercase; }}
        .btn:hover {{ background: #ff003c; box-shadow: 0 0 30px rgba(255,0,60,0.5); }}
    </style>
</head>
<body>
    <div class="badge">MANUFACTURA ON-DEMAND</div>
    <h1>{prod['nombre']}</h1>
    <p>{prod['desc']}</p>
    <p>Precio de Lista: <s style="color:#555;">${prod['precio_shopify']} USD</s></p>
    <div class="precio">Precio Final: ${precio_usd} USD</div>
    <a href="{link_cobro}" class="btn">Solicitar Fabricación</a>
    <p style="color: #444; margin-top: 20px; font-size: 0.9rem;">Envíos globales operados por red de proveedores premium.</p>
</body>
</html>"""
    with open(os.path.join(prod_dir, "landing.html"), "w") as f:
        f.write(html_landing)

    # 3. Preparar tarjeta para el Dashboard
    nuevas_tarjetas += f"""
        <div class="card" style="border-color: #ff003c;">
            <div class="status" style="background: rgba(255,0,60,0.2); color: #ff003c; border: 1px solid #ff003c;">HARDWARE 3D</div>
            <h3 style="color: #fff;">{prod['nombre']}</h3>
            <p style="color: #888;">{prod['desc']}</p>
            <a href="productos/{prod['id']}/landing.html" target="_blank" class="btn-link">Ver Landing B2C</a>
        </div>"""
    
    print(f"✔ Empaquetado en línea: {prod['nombre']}")
    time.sleep(0.5)

print("\n[RANGO S] Actualizando Hub del Director con la línea Obsidian Smart Spaces...")

# Inyectar las nuevas tarjetas en el Dashboard
dashboard_path = "dashboard_director.html"
if os.path.exists(dashboard_path):
    with open(dashboard_path, 'r') as file:
        dashboard_html = file.read()
    
    insert_pos = dashboard_html.rfind("</div>\n</body>")
    if insert_pos != -1:
        # Añadir un separador visual para el hardware 3D
        separador = "<h2 style='color:#ff003c; margin-top:40px; text-shadow: 0 0 10px rgba(255,0,60,0.3);'>OBSIDIAN: SMART SPACES & 3D</h2>"
        dashboard_html = dashboard_html[:insert_pos] + "</div>" + separador + "<div class='grid'>" + nuevas_tarjetas + dashboard_html[insert_pos:]
        with open(dashboard_path, 'w') as file:
            file.write(dashboard_html)
        print("✔ Hub del Director actualizado.")

print("\n=== [S-PRIME AI] LÍNEA 3D EN PRODUCCIÓN. ===")
