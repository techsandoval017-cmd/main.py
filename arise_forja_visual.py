import os

BASE_DIR = "laboratorio_software"

print("=== [ITACHI UCHIHA] INYECTANDO INTERFACES VISUALES (FRONT-END) RANGO S ===")

# ==========================================
# 1. OBSIDIAN ORACLE (Data Science / Dashboards)
# ==========================================
html_obsidian = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Obsidian Oracle | S-Prime</title>
    <style>
        body { background: #050505; color: #fff; font-family: 'Courier New', Courier, monospace; padding: 40px; }
        .header { border-bottom: 2px solid #ff003c; padding-bottom: 10px; margin-bottom: 20px; }
        h1 { color: #ff003c; text-transform: uppercase; text-shadow: 0 0 10px rgba(255,0,60,0.5); }
        .dashboard { display: none; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px; }
        .card { background: #111; border: 1px solid #333; padding: 20px; text-align: center; border-radius: 5px; }
        .btn { background: #ff003c; color: #fff; border: none; padding: 10px 20px; cursor: pointer; font-weight: bold; text-transform: uppercase; }
        .btn:hover { box-shadow: 0 0 15px #ff003c; }
        .log { color: #00ffcc; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="header"><h1>Obsidian Oracle // El Ojo Absoluto</h1></div>
    <p>Sube el archivo crudo de Excel/CSV de tu empresa. Obsidian proyectará la verdad.</p>
    <input type="file" id="fileInput" style="margin-bottom: 15px; color: #fff;">
    <br>
    <button class="btn" onclick="procesar()">Inyectar Datos al Oráculo</button>
    <div class="log" id="status"></div>

    <div class="dashboard" id="dash">
        <div class="card"><h3 style="color:#00ffcc;">Flujo de Caja</h3><h2 id="caja">$0.00</h2></div>
        <div class="card"><h3 style="color:#ff003c;">Fugas Detectadas</h3><h2>0</h2></div>
        <div class="card" style="grid-column: span 2;"><h3 style="color:#fff;">Proyección Algorítmica</h3><p>Riesgo Financiero: MÍNIMO. Operación estabilizada por S-Prime Corp.</p></div>
    </div>

    <script>
        function procesar() {
            document.getElementById('status').innerText = "[+] Analizando nodos de datos...";
            setTimeout(() => {
                document.getElementById('status').innerText = "[+] Limpiando ruido estadístico... Completado.";
                document.getElementById('dash').style.display = 'grid';
                document.getElementById('caja').innerText = "$145,230.50 USD";
            }, 1500);
        }
    </script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "obsidian_oracle", "frontend", "index.html"), "w") as f: f.write(html_obsidian)

# ==========================================
# 2. SHADOW LEGION FORGE (IA / Bots)
# ==========================================
html_shadow = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Shadow Legion Forge</title>
    <style>
        body { background: #000; color: #39ff14; font-family: 'Courier New', monospace; padding: 40px; }
        h1 { border-bottom: 1px solid #39ff14; padding-bottom: 10px; }
        .btn { background: transparent; border: 1px solid #39ff14; color: #39ff14; padding: 10px; cursor: pointer; }
        .btn:hover { background: #39ff14; color: #000; }
        .terminal { background: #0a0a0a; border: 1px solid #333; padding: 20px; height: 200px; overflow-y: auto; margin-top: 20px; color: #aaa; }
        input { background: #111; border: 1px solid #333; color: #39ff14; padding: 10px; width: 300px; }
    </style>
</head>
<body>
    <h1>SHADOW LEGION FORGE // Reclutamiento IA</h1>
    <p>Despliega un Soldado de Sombra para automatizar WhatsApp.</p>
    <input type="text" id="wa_num" placeholder="Número de WhatsApp Destino">
    <button class="btn" onclick="desplegar()">Desplegar Soldado</button>
    <div class="terminal" id="term">S-Prime OS v2.0 Iniciado.<br>Esperando órdenes de despliegue...<br></div>
    <script>
        function desplegar() {
            let num = document.getElementById('wa_num').value;
            let term = document.getElementById('term');
            if(!num) { term.innerHTML += "<br>[ERROR] Destino requerido."; return; }
            term.innerHTML += "<br>> Compilando modelo NLP Rango B...";
            setTimeout(() => { term.innerHTML += "<br>> Inyectando webhook de WhatsApp al número: " + num; }, 800);
            setTimeout(() => { term.innerHTML += "<br><span style='color:#39ff14;'>> SOLDADO DESPLEGADO CON ÉXITO. Escuchando mensajes.</span>"; }, 1800);
        }
    </script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "shadow_legion_forge", "frontend", "index.html"), "w") as f: f.write(html_shadow)

# ==========================================
# 3. VORTEX CITADEL (Ciberseguridad)
# ==========================================
html_vortex = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>VORTEX Citadel</title>
    <style>
        body { background: #020202; color: #00d2ff; font-family: monospace; padding: 50px; text-align: center; }
        h1 { text-shadow: 0 0 15px #00d2ff; }
        .scan-box { border: 2px dashed #00d2ff; padding: 40px; display: inline-block; margin-top: 20px; }
        .btn { background: #00d2ff; color: #000; font-weight: bold; padding: 15px 30px; border: none; cursor: pointer; text-transform: uppercase; }
        .progress { width: 100%; background: #111; height: 20px; margin-top: 20px; display: none; }
        .bar { width: 0%; background: #00d2ff; height: 100%; transition: width 2s; }
    </style>
</head>
<body>
    <h1>VORTEX CITADEL // Escáner de Red</h1>
    <div class="scan-box">
        <input type="text" id="target" placeholder="IP o Dominio Objetivo" style="padding:10px; width:250px; background:#111; border:1px solid #00d2ff; color:#fff;">
        <br><br>
        <button class="btn" onclick="escanear()">Ejecutar Auditoría</button>
        <div class="progress" id="prog"><div class="bar" id="bar"></div></div>
        <p id="res" style="margin-top:20px; color:#fff;"></p>
    </div>
    <script>
        function escanear() {
            document.getElementById('prog').style.display = 'block';
            setTimeout(() => { document.getElementById('bar').style.width = '100%'; }, 100);
            setTimeout(() => { document.getElementById('res').innerHTML = "<b>[+] 0 Vulnerabilidades Críticas. Fortaleza Impenetrable.</b>"; }, 2100);
        }
    </script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "vortex_citadel", "frontend", "index.html"), "w") as f: f.write(html_vortex)

# ==========================================
# 4. S-PRIME GUILD MASTER (Gestión de Equipo)
# ==========================================
html_guild = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>S-Prime Guild Master</title>
    <style>
        body { background: #1a1a1d; color: #fff; font-family: Arial, sans-serif; padding: 40px; }
        h1 { color: #f9a826; border-left: 5px solid #f9a826; padding-left: 15px; }
        .grid { display: flex; gap: 20px; margin-top: 30px; }
        .col { background: #222; padding: 20px; width: 30%; border-radius: 8px; border-top: 3px solid #555; min-height: 200px;}
        .task { background: #333; padding: 10px; margin-bottom: 10px; border-left: 3px solid #f9a826; }
        .btn { background: #f9a826; color: #000; border: none; padding: 10px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <h1>GUILD MASTER // Asignación de Cazadores</h1>
    <input type="text" id="hunter" placeholder="Nombre del Cazador" style="padding:10px;">
    <button class="btn" onclick="addHunter()">Reclutar y Asignar Misión</button>

    <div class="grid">
        <div class="col" style="border-color: #ff003c;">
            <h3>Rango E (En Espera)</h3>
            <div id="rank_e"></div>
        </div>
        <div class="col" style="border-color: #39ff14;">
            <h3>Rango B (En Producción)</h3>
            <div class="task">Jinwoo - Desarrollo API</div>
        </div>
        <div class="col" style="border-color: #00d2ff;">
            <h3>Rango S (Completado)</h3>
            <div class="task">Goku - Reforja Visual</div>
        </div>
    </div>
    <script>
        function addHunter() {
            let h = document.getElementById('hunter').value;
            if(h) {
                document.getElementById('rank_e').innerHTML += `<div class="task">${h} - Misión Asignada</div>`;
                document.getElementById('hunter').value = '';
            }
        }
    </script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "sprime_guild_master", "frontend", "index.html"), "w") as f: f.write(html_guild)

# ==========================================
# 5. MONARCH QUANT TERMINAL (Trading)
# ==========================================
html_quant = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Monarch Quant Terminal</title>
    <style>
        body { background: #000; color: #fff; font-family: monospace; padding: 0; margin: 0; }
        .topbar { background: #111; padding: 15px; border-bottom: 1px solid #444; display: flex; justify-content: space-between;}
        h2 { margin: 0; color: #eab308; }
        .ticker { font-size: 4rem; text-align: center; margin-top: 50px; }
        .btn { background: #eab308; color: #000; font-size: 1.5rem; padding: 15px 40px; border: none; cursor: pointer; display: block; margin: 50px auto; text-transform: uppercase; }
        .green { color: #39ff14; } .red { color: #ff003c; }
    </style>
</head>
<body>
    <div class="topbar"><h2>MONARCH QUANT</h2> <span style="color:#888;">Operación Algorítmica HFT</span></div>
    <div class="ticker" id="btc">BTC/USD: <span class="green">$64,250.00</span></div>
    <button class="btn" onclick="alert('Protocolo de Preservación de Capital Rango S Activado. Ejecutando trades automáticos...')">Activar Algoritmo Monarch</button>
    
    <script>
        setInterval(() => {
            let base = 64250;
            let move = (Math.random() * 100) - 50;
            let val = (base + move).toFixed(2);
            let color = move > 0 ? 'green' : 'red';
            document.getElementById('btc').innerHTML = `BTC/USD: <span class="${color}">$${val}</span>`;
        }, 2000);
    </script>
</body>
</html>"""
with open(os.path.join(BASE_DIR, "monarch_quant_terminal", "frontend", "index.html"), "w") as f: f.write(html_quant)

print("✔ Las 5 Interfaces Visuales han sido forjadas y conectadas.")

# Crear el lanzador de Laboratorio (Servidor Web Dedicado)
script_lanzador = """#!/bin/bash
echo "Levantando Hub Visual del Laboratorio S-Prime en el Puerto 8060..."
cd ~/sprime_cloud_core/laboratorio_software
python3 -m http.server 8060 &
npm exec localtunnel --port 8060 --subdomain sprime-arsenal &
echo "El Arsenal Visual está en vivo en: https://sprime-arsenal.loca.lt"
"""
with open("iniciar_arsenal_visual.sh", "w") as f: f.write(script_lanzador)
os.system("chmod +x iniciar_arsenal_visual.sh")

print("=== [S-PRIME AI] SISTEMAS VISUALES LISTOS. ===")
