import os

print("⚡ INICIANDO DESPLIEGUE DEL PANEL SHADOW CORE...")

# 1. Crear el directorio del Panel Maestro
os.makedirs("panel_maestro", exist_ok=True)

html_panel = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S-Prime | Shadow Core (Master Panel)</title>
    <style>
        body { background: #050505; color: #fff; font-family: 'Segoe UI', Tahoma, sans-serif; margin: 0; display: flex; height: 100vh; overflow: hidden; }
        .sidebar { width: 280px; background: #0a0a0a; border-right: 1px solid #333; padding: 20px; display: flex; flex-direction: column; }
        .sidebar h2 { color: #ff4500; font-size: 1.5em; text-transform: uppercase; letter-spacing: 2px; border-bottom: 1px solid #ff4500; padding-bottom: 15px; margin-top: 0; }
        .menu-btn { background: #111; color: #aaa; border: 1px solid #222; padding: 15px; margin-bottom: 10px; border-radius: 5px; cursor: pointer; text-align: left; font-weight: bold; transition: 0.3s; }
        .menu-btn:hover, .menu-btn.active { background: #1a1a1a; color: #ff4500; border-color: #ff4500; }
        .content { flex: 1; padding: 40px; background: #0f0f0f; overflow-y: auto; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 20px; margin-bottom: 30px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .card { background: #111; border: 1px solid #222; padding: 20px; border-radius: 8px; }
        .card h3 { color: #00ffcc; margin-top: 0; }
        .card p { color: #888; font-size: 0.9em; }
        .action-btn { display: inline-block; background: #00ffcc; color: #000; padding: 10px 15px; border-radius: 4px; text-decoration: none; font-weight: bold; text-transform: uppercase; font-size: 0.8em; margin-top: 10px; }
        .action-btn:hover { background: #00ccaa; }
    </style>
</head>
<body>
    <div class="sidebar">
        <h2>SHADOW CORE</h2>
        <button class="menu-btn active">🤖 Orquestador de Agentes (IA)</button>
        <button class="menu-btn" onclick="window.open('/tier2/', '_blank')">🌐 Ecosistema Tier 2 (Público)</button>
        <button class="menu-btn" onclick="window.open('/tier3/', '_blank')">💼 Ecosistema Tier 3 (Dueños)</button>
        <button class="menu-btn" onclick="window.open('/productos/sprime_import_motors/landing.html', '_blank')">🚢 Landing Importaciones</button>
        <button class="menu-btn" style="margin-top: auto; border-color: #ff3333; color: #ff3333;">🔴 Estado: ONLINE</button>
    </div>
    <div class="content">
        <div class="header">
            <h1>Panel Central de Mando S-Prime</h1>
            <div style="background: #25D366; padding: 5px 15px; border-radius: 4px; color: #000; font-weight: bold;">Director Autenticado</div>
        </div>

        <div class="grid">
            <div class="card">
                <h3>🎙️ Agente de Voz (ElevenLabs)</h3>
                <p>Generación de locuciones para Shorts y VSLs.</p>
                <input type="text" placeholder="Ingresa el texto aquí..." style="width: 100%; padding: 10px; background: #222; color: #fff; border: 1px solid #444; border-radius: 4px; box-sizing: border-box;">
                <a href="#" class="action-btn">Generar Audio</a>
            </div>
            
            <div class="card">
                <h3>🎨 Agente Visual (Midjourney/Leonardo)</h3>
                <p>Renderizado 3D de Smartspaces y Talleres.</p>
                <input type="text" placeholder="Ej: Motor FT 150G desarmado cyberpunk..." style="width: 100%; padding: 10px; background: #222; color: #fff; border: 1px solid #444; border-radius: 4px; box-sizing: border-box;">
                <a href="#" class="action-btn">Generar Render</a>
            </div>

            <div class="card">
                <h3>✍️ Agente Copywriter</h3>
                <p>Creación de guiones y copys de venta.</p>
                <input type="text" placeholder="Tema del video..." style="width: 100%; padding: 10px; background: #222; color: #fff; border: 1px solid #444; border-radius: 4px; box-sizing: border-box;">
                <a href="#" class="action-btn">Escribir Guion</a>
            </div>
        </div>
    </div>
</body>
</html>"""

with open("panel_maestro/index.html", "w", encoding="utf-8") as f:
    f.write(html_panel)

# 2. Inyectar TODAS las rutas en el backend de forma absoluta para eliminar el 404
archivo_backend = "backend/main.py"
if os.path.exists(archivo_backend):
    with open(archivo_backend, "r") as f:
        codigo = f.read()
    
    # Limpiar montajes anteriores para evitar conflictos
    lineas = [l for l in codigo.split("\n") if "app.mount" not in l]
    codigo_limpio = "\n".join(lineas)
    
    # Inyectar las rutas correctas
    bloque_rutas = """
# MONTAJES DEL ECOSISTEMA S-PRIME
import os
from fastapi.staticfiles import StaticFiles

if os.path.exists('panel_maestro'):
    app.mount('/panel', StaticFiles(directory='panel_maestro', html=True), name='panel')
if os.path.exists('entregables_reales'):
    app.mount('/tier2', StaticFiles(directory='entregables_reales', html=True), name='tier2')
if os.path.exists('entregables_reales/tier3_enterprise'):
    app.mount('/tier3', StaticFiles(directory='entregables_reales/tier3_enterprise', html=True), name='tier3')
if os.path.exists('productos'):
    app.mount('/productos', StaticFiles(directory='productos', html=True), name='productos')
"""
    codigo_final = codigo_limpio + "\n" + bloque_rutas
    
    with open(archivo_backend, "w") as f:
        f.write(codigo_final)

# 3. Subir a Producción
os.system("git add . && git commit -m 'deploy: Master Panel Shadow Core y correccion de rutas' && git push origin main")

print("✅ PANEL MAESTRO FORJADO Y DESPLEGADO.")
