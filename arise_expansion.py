import os
import time

BASE_DIR = "productos"

# Agrega aquí los nuevos negocios que quieras dominar en el futuro
nuevos_nichos = [
    {
        "id": "dark_kitchen_ai",
        "nombre": "Dark Kitchen Optimizer",
        "desc": "Software de gestión de pedidos múltiples (UberEats, Rappi) y costeo de recetas para cocinas ocultas.",
        "precio_landing": 8900 # $89.00 USD
    },
    {
        "id": "real_estate_vortex",
        "nombre": "Vortex Inmobiliario B2B",
        "desc": "CRM automatizado para agentes independientes. Seguimiento de leads en WhatsApp y catálogos virtuales.",
        "precio_landing": 14900 # $149.00 USD
    },
    {
        "id": "healthcore_dental",
        "nombre": "HealthCore Dental",
        "desc": "Gestor de expedientes clínicos, radiografías y recordatorios automáticos de limpieza para pacientes.",
        "precio_landing": 19900 # $199.00 USD
    },
    {
        "id": "ink_master_suite",
        "nombre": "Tattoo Studio Manager",
        "desc": "Agendamiento con depósitos obligatorios por Stripe, firmas de consentimiento digital y cuidados post-tatuaje.",
        "precio_landing": 7900 # $79.00 USD
    },
    {
        "id": "gym_spartan_core",
        "nombre": "Spartan Gym Core",
        "desc": "Control de accesos, cobros recurrentes de mensualidades y rutinas en PDF automatizadas para gimnasios locales.",
        "precio_landing": 9900 # $99.00 USD
    }
]

print("=== [S-PRIME AI] INICIANDO EXPANSIÓN A NUEVOS MERCADOS ===")

nuevas_tarjetas = ""

for prod in nuevos_nichos:
    prod_dir = os.path.join(BASE_DIR, prod["id"])
    os.makedirs(prod_dir, exist_ok=True)
    
    link_cobro = f"https://buy.stripe.com/test_{prod['id']}_expansion"
    precio_usd = f"{prod['precio_landing'] // 100}.00"
    
    # Generar Landing Page
    html_landing = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{prod['nombre']} | S-Prime</title>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body {{ background: #000; color: #fff; font-family: 'Rajdhani', sans-serif; text-align: center; padding: 50px; border-top: 3px solid #39ff14; }}
        h1 {{ color: #39ff14; font-size: 3rem; text-transform: uppercase; }}
        p {{ font-size: 1.2rem; color: #aaa; max-width: 600px; margin: 0 auto 20px auto; }}
        .precio {{ font-size: 2.5rem; color: #ff003c; margin: 30px 0; }}
        .btn {{ background: transparent; border: 2px solid #39ff14; color: #39ff14; padding: 15px 40px; font-size: 1.5rem; text-decoration: none; border-radius: 5px; display: inline-block; transition: 0.3s; text-transform: uppercase; }}
        .btn:hover {{ background: #39ff14; color: #000; }}
    </style>
</head>
<body>
    <h1>{prod['nombre']}</h1>
    <p>{prod['desc']}</p>
    <div class="precio">Inversión B2B: ${precio_usd} USD</div>
    <a href="{link_cobro}" class="btn">Obtener Licencia</a>
</body>
</html>"""
    with open(os.path.join(prod_dir, "landing.html"), "w") as f:
        f.write(html_landing)

    nuevas_tarjetas += f"""
        <div class="card" style="border-color: #39ff14;">
            <div class="status" style="background: rgba(57,255,20,0.2); color: #39ff14; border: 1px solid #39ff14;">NUEVO NICHO</div>
            <h3 style="color: #fff;">{prod['nombre']}</h3>
            <p style="color: #888;">{prod['desc']}</p>
            <a href="productos/{prod['id']}/landing.html" target="_blank" class="btn-link">Ver Landing Directa</a>
        </div>"""
    
    print(f"✔ Nicho asimilado y empaquetado: {prod['nombre']}")

# Actualizar el Hub
dashboard_path = "dashboard_director.html"
if os.path.exists(dashboard_path):
    with open(dashboard_path, 'r') as file:
        dashboard_html = file.read()
    
    insert_pos = dashboard_html.rfind("</div>\n</body>")
    if insert_pos != -1:
        separador = "<h2 style='color:#39ff14; margin-top:40px;'>NUEVA EXPANSIÓN B2B</h2>"
        dashboard_html = dashboard_html[:insert_pos] + "</div>" + separador + "<div class='grid'>" + nuevas_tarjetas + dashboard_html[insert_pos:]
        with open(dashboard_path, 'w') as file:
            file.write(dashboard_html)
        print("✔ Hub del Director actualizado con las nuevas expansiones.")

print("\n=== [S-PRIME AI] EXPANSIÓN COMPLETADA. ===")
