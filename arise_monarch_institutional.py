import os

DIR_QUANT = "laboratorio_software/monarch_quant_terminal/frontend"
os.makedirs(DIR_QUANT, exist_ok=True)

html_quant_pro = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Monarch Quant Terminal | Radar Institucional</title>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { background: #040508; color: #fff; font-family: 'JetBrains Mono', monospace; margin: 0; padding: 25px; border-top: 4px solid #eab308; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1f2533; padding-bottom: 15px; margin-bottom: 25px; }
        h1 { margin: 0; font-family: 'Rajdhani', sans-serif; color: #eab308; font-size: 2rem; letter-spacing: 1px; }
        .status-badge { background: rgba(57,255,20,0.1); border: 1px solid #39ff14; color: #39ff14; padding: 4px 12px; font-size: 0.8rem; border-radius: 4px; font-weight: bold; }
        
        .grid-main { display: grid; grid-template-columns: 2fr 1fr; gap: 20px; }
        .card { background: #0a0d14; border: 1px solid #1a2233; border-radius: 6px; padding: 20px; }
        
        .metric-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 20px; }
        .metric-box { background: #101522; border: 1px solid #222b40; padding: 15px; border-radius: 4px; text-align: center; }
        .metric-box span { color: #7e8b9b; font-size: 0.75rem; text-transform: uppercase; }
        .metric-box h3 { margin: 5px 0 0; font-size: 1.4rem; color: #fff; font-family: 'Rajdhani', sans-serif; }
        
        .price-radar { font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: bold; text-align: center; margin: 25px 0; color: #39ff14; text-shadow: 0 0 25px rgba(57,255,20,0.3); }
        
        .terminal-log { background: #030406; border: 1px solid #161c28; border-radius: 4px; padding: 15px; height: 260px; overflow-y: auto; font-size: 0.85rem; line-height: 1.6; }
        .log-inflow { color: #39ff14; font-weight: bold; }
        .log-be { color: #00d2ff; }
        .log-trail { color: #eab308; }
        .log-choch { color: #ff003c; font-weight: bold; }
        
        .btn-action { width: 100%; background: #eab308; color: #000; border: none; padding: 15px; font-family: 'Rajdhani', sans-serif; font-size: 1.2rem; font-weight: bold; cursor: pointer; text-transform: uppercase; border-radius: 4px; transition: 0.2s; margin-top: 15px; }
        .btn-action:hover { background: #fff; box-shadow: 0 0 20px rgba(234,179,8,0.5); }
        
        .control-group { margin-bottom: 12px; }
        .control-group label { display: block; color: #8892b0; font-size: 0.8rem; margin-bottom: 5px; }
        .control-group input { width: 100%; box-sizing: border-box; background: #121824; border: 1px solid #232d42; color: #fff; padding: 10px; border-radius: 4px; font-family: inherit; }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h1>MONARCH QUANT // RADAR INSTITUCIONAL & TRAILING 30-PIP</h1>
            <small style="color:#7e8b9b;">Protocolo Smart Money Flow • Preservación de Capital Rango S</small>
        </div>
        <div class="status-badge" id="botStatus">ESCANEANDO FLUJO BANCARIO</div>
    </div>

    <div class="metric-row">
        <div class="metric-box"><span>Activo en Rastreo</span><h3>EUR/USD • XAU/USD</h3></div>
        <div class="metric-box"><span>Pips Acumulados</span><h3 id="pipsContador" style="color:#39ff14;">+0 Pips</h3></div>
        <div class="metric-box"><span>Protección Activa</span><h3 id="stopStatus" style="color:#00d2ff;">Standby</h3></div>
        <div class="metric-box"><span>Ganancia Asegurada</span><h3 id="profitAsegurado">$0.00 USD</h3></div>
    </div>

    <div class="grid-main">
        <div class="card">
            <h4 style="margin-top:0; color:#8892b0;">TELEMETRÍA DE PRECIO EN VIVO</h4>
            <div class="price-radar" id="precioLive">1.08450</div>
            
            <h4 style="color:#8892b0; margin-bottom:10px;">REGISTRO DE ÓRDENES Y SEGUIMIENTO INSTITUCIONAL</h4>
            <div class="terminal-log" id="consolaLog">
                [00:00:01] Monarch Quant Engine v4.0 inicializado.<br>
                [00:00:02] Monitoreando inyecciones de liquidez institucional (Order Blocks)...<br>
            </div>
        </div>

        <div class="card">
            <h4 style="margin-top:0; color:#eab308; border-bottom:1px solid #222b40; padding-bottom:10px;">PARÁMETROS DE EJECUCIÓN</h4>
            
            <div class="control-group">
                <label>Umbral de Inyección Institucional (Lotes):</label>
                <input type="text" value=">= 500 Lots / 50M USD" disabled>
            </div>
            <div class="control-group">
                <label>Stop-Loss Inicial (Poco Pips):</label>
                <input type="text" value="12 Pips (Bajo el Bloque)">
            </div>
            <div class="control-group">
                <label>Activación de Breakeven:</label>
                <input type="text" value="+15 Pips (Riesgo Cero)">
            </div>
            <div class="control-group">
                <label>Paso de Trailing Stop:</label>
                <input type="text" value="Cada +30 Pips (Sin Cerrar Orden)">
            </div>
            <div class="control-group">
                <label>Cierre por Estructura:</label>
                <input type="text" value="Ruptura de Tendencia (CHoCH)">
            </div>

            <button class="btn-action" onclick="iniciarCaza()">Iniciar Caza Institucional</button>
        </div>
    </div>

    <script>
        let pips = 0;
        let basePrice = 1.08450;
        let corriendo = false;
        let trailingStep = 0;

        function log(msg, className="") {
            let c = document.getElementById('consolaLog');
            let t = new Date().toLocaleTimeString();
            c.innerHTML += `<div class="${className}">[${t}] ${msg}</div>`;
            c.scrollTop = c.scrollHeight;
        }

        function iniciarCaza() {
            if(corriendo) return;
            corriendo = true;
            document.getElementById('botStatus').innerText = "CAZA EN CURSO • SMART MONEY DETECTADO";
            document.getElementById('botStatus').style.color = "#eab308";
            document.getElementById('botStatus').style.borderColor = "#eab308";
            
            log("Escaneando libro de órdenes y volumen anómalo...", "");
            
            setTimeout(() => {
                log("⚡ VELA DE IGNICIÓN DETECTADA: Compra masiva institucional de $82M en 1.08450", "log-inflow");
                log("➜ EJECUTANDO ORDEN COMPRA (LONG) // SL colocado a 12 pips bajo el bloque institucional.", "log-inflow");
                document.getElementById('stopStatus').innerText = "SL: -12 Pips";
                iniciarSeguimientoPrecio();
            }, 1200);
        }

        function iniciarSeguimientoPrecio() {
            let intervalo = setInterval(() => {
                // Simulación de avance institucional en tendencia
                let incremento = (Math.random() * 0.00030) + 0.00010;
                basePrice += incremento;
                pips = Math.round((basePrice - 1.08450) * 10000);
                
                document.getElementById('precioLive').innerText = basePrice.toFixed(5);
                document.getElementById('pipsContador').innerText = `+${pips} Pips`;

                // 1. Activar Breakeven
                if (pips >= 15 && trailingStep === 0) {
                    trailingStep = 1;
                    document.getElementById('stopStatus').innerText = "BREAKEVEN (0 Riesgo)";
                    log("🛡️ PRECIO SUPERA +15 PIPS ➔ Stop-Loss movido a Entrada (BREAKEVEN). La orden ya no puede perder.", "log-be");
                }

                // 2. Trailing Stop cada 30 pips sin cerrar la orden
                if (pips >= 30 && trailingStep === 1) {
                    trailingStep = 2;
                    document.getElementById('stopStatus').innerText = "SL Protegido: +30 Pips";
                    document.getElementById('profitAsegurado').innerText = "$3,000 USD";
                    log("🔒 UMBRAL DE +30 PIPS ALCANZADO ➔ Stop asegurado a +30 pips. Posición sigue abierta exprimiendo la tendencia.", "log-trail");
                }

                if (pips >= 60 && trailingStep === 2) {
                    trailingStep = 3;
                    document.getElementById('stopStatus').innerText = "SL Protegido: +60 Pips";
                    document.getElementById('profitAsegurado').innerText = "$6,000 USD";
                    log("🔒 UMBRAL DE +60 PIPS ALCANZADO ➔ Stop subido a +60 pips protegidos. Maximizando carrera.", "log-trail");
                }

                if (pips >= 90 && trailingStep === 3) {
                    trailingStep = 4;
                    document.getElementById('stopStatus').innerText = "SL Protegido: +90 Pips";
                    document.getElementById('profitAsegurado').innerText = "$9,000 USD";
                    log("🔒 UMBRAL DE +90 PIPS ALCANZADO ➔ Stop subido a +90 pips.", "log-trail");
                }

                // 3. Fin de la tendencia: Ruptura de estructura (CHoCH)
                if (pips >= 115) {
                    clearInterval(intervalo);
                    log("⚠️ CAMBIO DE TENDENCIA DETECTADO (CHoCH / Ruptura de Mínimo Previo).", "log-choch");
                    log("💰 ORDEN CERRADA EN CÚSPIDE ESTRUCTURAL // Ganancia Total Capturada: +115 Pips ($11,500 USD).", "log-inflow");
                    document.getElementById('botStatus').innerText = "CICLO INSTITUCIONAL COMPLETADO";
                    document.getElementById('botStatus').style.color = "#39ff14";
                    document.getElementById('botStatus').style.borderColor = "#39ff14";
                }
            }, 1000);
        }
    </script>
</body>
</html>"""

with open(os.path.join(DIR_QUANT, "index.html"), "w") as f:
    f.write(html_quant_pro)

print("✔ MONARCH QUANT TERMINAL ACTUALIZADO CON RADAR INSTITUCIONAL Y TRAILING 30-PIPS.")
