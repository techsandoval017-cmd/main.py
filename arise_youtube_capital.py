import os
import sqlite3
import time

# 1. CONEXIÓN AL TSUKUYOMI LOCAL
conn = sqlite3.connect('sprime_academia/memoria_cursos.db')
c = conn.cursor()

# Crear tabla militarizada para el rastreo de enlaces de capital
c.execute('DROP TABLE IF EXISTS capital_referidos')
c.execute('''CREATE TABLE capital_referidos
             (id INTEGER PRIMARY KEY, empresa TEXT, nicho TEXT, tipo_comision TEXT, titulo_video_youtube TEXT, estado TEXT)''')
conn.commit()

# 2. LAS VENAS DE CAPITAL (Fintech & SaaS de alto pago)
maquina_afiliados = [
    {
        "empresa": "Binance / Bybit",
        "nicho": "Fintech / Cripto",
        "tipo_comision": "20% de las comisiones de trading de por vida.",
        "titulo_video": "Binance 2026: Cómo abrir tu cuenta y no perder tu dinero (Guía Completa)"
    },
    {
        "empresa": "Shopify",
        "nicho": "E-commerce",
        "tipo_comision": "Pago único de $150 USD por cada usuario que abra una tienda.",
        "titulo_video": "Shopify desde Cero: La verdad sobre vender en línea hoy"
    },
    {
        "empresa": "Hostinger / AWS",
        "nicho": "Servidores / Web",
        "tipo_comision": "60% de comisión por cada plan de hosting vendido.",
        "titulo_video": "Dónde alojar tu web en 2026: Pruebas de velocidad reales"
    },
    {
        "empresa": "Printful",
        "nicho": "Impresión On-Demand",
        "tipo_comision": "10% de cada orden que hagan tus referidos por 9 meses.",
        "titulo_video": "Cómo crear tu marca de ropa sin comprar inventario (Printful Tutorial)"
    },
    {
        "empresa": "Nu / MercadoPago",
        "nicho": "Fintech Local (MX/LATAM)",
        "tipo_comision": "Bono en efectivo por cada tarjeta de crédito activada.",
        "titulo_video": "Las 3 Mejores Tarjetas de Crédito para empezar tu negocio"
    }
]

print("=== [ITACHI UCHIHA] ACTIVANDO LA MÁQUINA DE CAPITAL YOUTUBE ===")
BASE_DIR = "youtube_capital_engine"
os.makedirs(BASE_DIR, exist_ok=True)

# 3. FORJANDO ESTRATEGIA Y GUIONES
for afiliado in maquina_afiliados:
    print(f"➜ Integrando red de extracción de capital: {afiliado['empresa']}...")
    
    # Memoria local
    c.execute("INSERT INTO capital_referidos (empresa, nicho, tipo_comision, titulo_video_youtube, estado) VALUES (?, ?, ?, ?, ?)",
              (afiliado['empresa'], afiliado['nicho'], afiliado['tipo_comision'], afiliado['titulo_video'], 'Pendiente de Grabación'))
    conn.commit()
    
    # Escribir el Guion de Youtube (Markdown)
    guion_md = f"""# ESTRATEGIA YOUTUBE: {afiliado['empresa']}
## Meta de Capital: Convertir tráfico en comisiones pasivas para S-Prime Corp.

### 1. Título SEO del Video
**{afiliado['titulo_video']}**

### 2. El Escenario (Product Placement Sutil)
- **Fondo:** El Busto de Gojo (Vacío Púrpura) encendido sutilmente atrás.
- **Utilería:** El instructor (Tú o tu avatar IA) sostiene una Taza negra mate de S-Prime Print Forge mientras explica. (Inception visual).

### 3. Estructura del Guion (Retención Máxima)
- **Gancho (0:00 - 0:15):** "¿Quieres usar {afiliado['empresa']} pero tienes miedo de cometer un error que te cueste dinero? Hoy te enseño la configuración exacta que usamos en nuestra corporación."
- **Contenido (0:15 - 5:00):** Tutorial de pantalla grabando cómo hacer la cuenta o mostrando la nueva actualización del mes.
- **Call to Action Oculto (5:00 - 5:30):** "Para que tengan el bono de bienvenida y no les cobren comisiones el primer mes, usen el enlace oficial que les dejé abajo en la descripción y en el primer comentario fijado."

### 4. Link a inyectar en la descripción
`[TU ENLACE DE AFILIADO AQUÍ]`
"""
    filename = afiliado['empresa'].replace(" / ", "_").replace(" ", "_").lower() + "_script.md"
    with open(os.path.join(BASE_DIR, filename), "w") as f:
        f.write(guion_md)
        
    time.sleep(0.3)

# 4. ACTUALIZAR EL HUB DEL DIRECTOR
dashboard_path = "dashboard_director.html"
if os.path.exists(dashboard_path):
    with open(dashboard_path, 'r') as file:
        dashboard_html = file.read()
    
    insert_pos = dashboard_html.rfind("</div>\n</body>")
    if insert_pos != -1:
        nueva_tarjeta = f"""
        <h2 style='color:#39ff14; margin-top:40px; text-shadow: 0 0 10px rgba(57,255,20,0.3);'>MÁQUINA DE CAPITAL (YOUTUBE AFILIADOS)</h2>
        <div class='grid'>
            <div class="card" style="border-color: #39ff14;">
                <div class="status" style="background: rgba(57,255,20,0.2); color: #39ff14; border: 1px solid #39ff14;">INGRESO PASIVO</div>
                <h3 style="color: #fff;">YouTube Affiliate Engine</h3>
                <p style="color: #888;">Generación de capital para hardware mediante reseñas Fintech y SaaS.</p>
                <a href="#" class="btn-link" onclick="alert('Revisa la carpeta local youtube_capital_engine para ver los guiones.')">Ver Guiones de Producción</a>
            </div>
        </div>"""
        
        dashboard_html = dashboard_html[:insert_pos] + "</div>" + nueva_tarjeta + dashboard_html[insert_pos:]
        with open(dashboard_path, 'w') as file:
            file.write(dashboard_html)
        print("✔ Hub del Director inyectado con el Motor de Capital.")

print("\n=== [ITACHI UCHIHA] MUGEN TSUKUYOMI AL 100%. SISTEMA OPERATIVO. ===")
conn.close()
