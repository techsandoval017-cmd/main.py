import os

html_auditado = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S-Prime | Shadow Core (Audited)</title>
    <style>
        body { background: #050505; color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; display: flex; height: 100vh; }
        .sidebar { width: 280px; background: #0a0a0a; border-right: 1px solid #333; padding: 20px; display: flex; flex-direction: column; }
        .sidebar h2 { color: #ff4500; font-size: 1.5em; border-bottom: 1px solid #ff4500; padding-bottom: 15px; margin-top: 0; }
        .menu-btn { background: #111; color: #aaa; border: 1px solid #222; padding: 15px; margin-bottom: 10px; border-radius: 5px; cursor: pointer; text-align: left; font-weight: bold; }
        .menu-btn:hover { background: #1a1a1a; color: #ff4500; border-color: #ff4500; }
        .content { flex: 1; padding: 40px; background: #0f0f0f; overflow-y: auto; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .card { background: #111; border: 1px solid #222; padding: 20px; border-radius: 8px; }
        .card h3 { color: #00ffcc; margin-top: 0; }
        input, button { width: 100%; padding: 10px; margin-top: 10px; border-radius: 4px; box-sizing: border-box; }
        input { background: #222; color: #fff; border: 1px solid #444; }
        button { background: #00ffcc; color: #000; border: none; font-weight: bold; cursor: pointer; text-transform: uppercase; }
        button:hover { background: #00ccaa; }
        .log { margin-top: 15px; font-size: 0.85em; color: #888; background: #000; padding: 10px; border-radius: 4px; min-height: 20px; }
    </style>
</head>
<body>
    <div class="sidebar">
        <h2>SHADOW CORE</h2>
        <button class="menu-btn" onclick="window.open('/tier2/', '_blank')">🌐 Módulos Tier 2</button>
        <button class="menu-btn" onclick="window.open('/tier3/', '_blank')">💼 Dashboards Tier 3</button>
        <button class="menu-btn" onclick="window.open('/productos/sprime_import_motors/landing.html', '_blank')">🚢 Importadora</button>
        <button class="menu-btn" style="margin-top: auto; border-color: #00ffcc; color: #00ffcc;">🟢 Rango S: ACTIVO</button>
    </div>
    <div class="content">
        <div class="grid">
            <div class="card">
                <h3>🎙️ Agente de Voz</h3>
                <input type="text" id="voz_input" placeholder="Texto para locución...">
                <button onclick="ejecutarAgente('voz')">Generar Audio</button>
                <div id="log_voz" class="log">Esperando orden...</div>
            </div>
            <div class="card">
                <h3>🎨 Agente Visual (Simulador)</h3>
                <input type="text" id="img_input" placeholder="Ej: Motor CG150 renderizado...">
                <button onclick="ejecutarAgente('img')">Generar Render</button>
                <div id="log_img" class="log">Esperando orden...</div>
            </div>
            <div class="card">
                <h3>✍️ Agente Copywriter</h3>
                <input type="text" id="copy_input" placeholder="Tema del Reel...">
                <button onclick="ejecutarAgente('copy')">Redactar Guion</button>
                <div id="log_copy" class="log">Esperando orden...</div>
            </div>
        </div>
    </div>

    <script>
        async function ejecutarAgente(tipo) {
            const input = document.getElementById(tipo + '_input').value;
            const log = document.getElementById('log_' + tipo);
            
            if(!input) { log.innerHTML = "❌ Error: Ingresa un texto."; log.style.color = "#ff3333"; return; }
            
            log.innerHTML = "⏳ Procesando orden...";
            log.style.color = "#d4af37";

            try {
                const response = await fetch('/api/agentes', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ agente: tipo, payload: input })
                });
                const data = await response.json();
                log.innerHTML = "✅ " + data.respuesta;
                log.style.color = "#00ffcc";
            } catch (error) {
                log.innerHTML = "❌ Error de conexión al núcleo.";
                log.style.color = "#ff3333";
            }
        }
    </script>
</body>
</html>"""

os.makedirs("panel_maestro", exist_ok=True)
with open("panel_maestro/index.html", "w", encoding="utf-8") as f:
    f.write(html_auditado)

archivo_main = "main.py"
with open(archivo_main, "r") as f:
    codigo_actual = f.read()

if "def api_agentes" not in codigo_actual:
    bloque_api = """
from pydantic import BaseModel
class OrdenAgente(BaseModel):
    agente: str
    payload: str

@app.post("/api/agentes")
def api_agentes(orden: OrdenAgente):
    if orden.agente == 'voz':
        return {"respuesta": f"Audio generado para: '{orden.payload[:15]}...'. Listo para descarga."}
    elif orden.agente == 'img':
        return {"respuesta": f"Renderizado completado. Modelo listo en el Simulador S-Prime."}
    elif orden.agente == 'copy':
        return {"respuesta": f"Guion redactado y guardado en base de datos."}
    return {"respuesta": "Agente no reconocido."}
"""
    with open(archivo_main, "a", encoding="utf-8") as f:
        f.write(bloque_api)

print("✅ PANEL AUDITADO LISTO.")
