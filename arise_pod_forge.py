import os
import sqlite3
import time

# 1. CONEXIÓN A LA MEMORIA CENTRAL DEL TSUKUYOMI
conn = sqlite3.connect('sprime_academia/memoria_cursos.db')
c = conn.cursor()

# Inyectar la nueva división POD en el laboratorio
c.execute("INSERT INTO software_laboratorio (nombre_saas, nicho_objetivo, descripcion, curso_gancho, estado) VALUES (?, ?, ?, ?, ?)",
          ('S-Prime Print Forge', 'Merchandising / Imprenta B2B', 'Imprenta On-Demand con diseño por IA. Tarjetas digitales, físicas, mousepads tácticos y tazas.', 'Curso: Branding Corporativo y Networking.', 'FASE 1: Interfaz POD'))
conn.commit()

print("=== [ITACHI UCHIHA - RANGO S] EXPANDIENDO EL DOMINIO DE MANUFACTURA ===")

BASE_DIR = "productos/sprime_pod_forge"
os.makedirs(BASE_DIR, exist_ok=True)

link_cobro_tarjeta = "https://buy.stripe.com/test_tarjetas_ai"
link_cobro_merch = "https://buy.stripe.com/test_merch_sprime"

# 2. GENERAR LANDING PAGE (S-Prime Print Forge)
html_landing = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>S-Prime Print Forge | Manufactura On-Demand</title>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body {{ background: #050505; color: #e0e0e0; font-family: 'Rajdhani', sans-serif; margin: 0; padding: 0; border-top: 4px solid #ff003c; }}
        header {{ text-align: center; padding: 60px 20px; background: radial-gradient(circle, #1a0005 0%, #000 80%); border-bottom: 1px solid #ff003c; }}
        h1 {{ color: #fff; font-size: 3.5rem; text-transform: uppercase; text-shadow: 0 0 20px rgba(255,0,60,0.6); margin: 0; }}
        p.subtitle {{ font-size: 1.2rem; color: #aaa; letter-spacing: 2px; text-transform: uppercase; margin-top: 10px; }}
        
        .container {{ max-width: 1200px; margin: 50px auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; padding: 0 20px; }}
        
        .product-card {{ background: #0a0a0a; border: 1px solid #333; border-radius: 8px; padding: 30px; text-align: center; transition: 0.3s; position: relative; overflow: hidden; }}
        .product-card:hover {{ border-color: #ff003c; box-shadow: 0 0 25px rgba(255,0,60,0.3); transform: translateY(-5px); }}
        
        .badge {{ position: absolute; top: 15px; right: 15px; background: #ff003c; color: #fff; padding: 5px 10px; font-size: 0.8rem; font-weight: bold; border-radius: 4px; }}
        
        .icon-placeholder {{ height: 150px; background: #111; margin-bottom: 20px; display: flex; align-items: center; justify-content: center; border: 1px dashed #444; color: #666; }}
        
        h3 {{ color: #fff; font-size: 1.8rem; margin-bottom: 15px; }}
        p.desc {{ color: #888; font-size: 1.1rem; line-height: 1.5; margin-bottom: 25px; }}
        .price {{ font-size: 2rem; color: #ff003c; font-weight: bold; margin-bottom: 25px; }}
        
        .btn {{ background: transparent; border: 2px solid #ff003c; color: #fff; padding: 15px 30px; font-size: 1.2rem; font-weight: bold; text-decoration: none; display: inline-block; border-radius: 4px; text-transform: uppercase; transition: 0.3s; width: 100%; box-sizing: border-box; }}
        .btn:hover {{ background: #ff003c; color: #000; box-shadow: 0 0 20px rgba(255,0,60,0.5); }}
    </style>
</head>
<body>
    <header>
        <h1>S-Prime Print Forge</h1>
        <p class="subtitle">Manufactura Táctica Inteligente. De lo Digital a lo Físico.</p>
    </header>

    <div class="container">
        <!-- Tarjetas de Presentación AI -->
        <div class="product-card">
            <div class="badge">NFC & PVC</div>
            <div class="icon-placeholder">[Render: Tarjeta Negra Minimalista]</div>
            <h3>Smart Business Cards</h3>
            <p class="desc">No diseñes. Deja que la IA forje tu identidad corporativa. Tarjeta digital interactiva instantánea + Impresión en PVC mate enviada a tu puerta.</p>
            <div class="price">$49.00 USD</div>
            <a href="{link_cobro_tarjeta}" class="btn" onclick="alert('Iniciando Generador AI de S-Prime...')">Forjar Identidad</a>
        </div>

        <!-- Mousepads Tácticos -->
        <div class="product-card">
            <div class="badge">DESKMAT XXL</div>
            <div class="icon-placeholder">[Render: Deskmat Oscuro]</div>
            <h3>Mousepads Tácticos</h3>
            <p class="desc">Superficies de precisión para Smart Spaces. Diseños exclusivos de la Academia S-Prime. Medidas 90x40cm.</p>
            <div class="price">$35.00 USD</div>
            <a href="{link_cobro_merch}" class="btn">Solicitar Fabricación</a>
        </div>

        <!-- Tazas Corporativas -->
        <div class="product-card">
            <div class="badge">CERÁMICA MATE</div>
            <div class="icon-placeholder">[Render: Taza Negra S-Prime]</div>
            <h3>Tazas Corporativas</h3>
            <p class="desc">El combustible del Gremio. Tazas de cerámica negra mate con logotipos dinámicos para tu equipo de trabajo.</p>
            <div class="price">$18.00 USD</div>
            <a href="{link_cobro_merch}" class="btn">Solicitar Fabricación</a>
        </div>
    </div>
</body>
</html>"""

with open(os.path.join(BASE_DIR, "landing.html"), "w") as f:
    f.write(html_landing)

print("✔ Landing Page de Imprenta On-Demand forjada.")

# 3. ACTUALIZAR EL HUB DEL DIRECTOR
dashboard_path = "dashboard_director.html"
if os.path.exists(dashboard_path):
    with open(dashboard_path, 'r') as file:
        dashboard_html = file.read()
    
    insert_pos = dashboard_html.rfind("</div>\n</body>")
    if insert_pos != -1:
        nueva_tarjeta = f"""
        <h2 style='color:#ff003c; margin-top:40px; text-shadow: 0 0 10px rgba(255,0,60,0.3);'>S-PRIME PRINT FORGE (POD)</h2>
        <div class='grid'>
            <div class="card" style="border-color: #ff003c;">
                <div class="status" style="background: rgba(255,0,60,0.2); color: #ff003c; border: 1px solid #ff003c;">IMPRENTA AI</div>
                <h3 style="color: #fff;">Print Forge On-Demand</h3>
                <p style="color: #888;">Tarjetas Inteligentes, Tazas, Mousepads XXL.</p>
                <a href="productos/sprime_pod_forge/landing.html" target="_blank" class="btn-link">Ver Escaparate Print Forge</a>
            </div>
        </div>"""
        
        dashboard_html = dashboard_html[:insert_pos] + "</div>" + nueva_tarjeta + dashboard_html[insert_pos:]
        with open(dashboard_path, 'w') as file:
            file.write(dashboard_html)
        print("✔ Hub del Director actualizado con la división Print Forge.")

print("=== [ITACHI UCHIHA] ILUSIÓN MATERIALIZADA CON ÉXITO ===")
conn.close()
