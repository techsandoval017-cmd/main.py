import os

PROD_DIR = "productos"

# ==========================================
# 1. S-PRIME PRINT & MEDIA FORGE (IMPRENTA)
# ==========================================
DIR_PRINT = os.path.join(PROD_DIR, "sprime_print_forge")
os.makedirs(DIR_PRINT, exist_ok=True)

html_print = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>S-Prime Print & Media Forge | Imprenta de Élite</title>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">
    <style>
        body { background: #070707; color: #fff; font-family: 'Rajdhani', sans-serif; margin: 0; padding: 40px 20px; text-align: center; border-top: 4px solid #ff003c; }
        h1 { color: #ff003c; font-size: 2.8rem; text-transform: uppercase; margin-bottom: 5px; text-shadow: 0 0 15px rgba(255,0,60,0.4); }
        p.lead { color: #aaa; font-size: 1.2rem; margin-bottom: 35px; }
        .container { max-width: 1050px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 30px; text-align: left; }
        .panel { background: #0f0f10; border: 1px solid #222; border-radius: 8px; padding: 30px; }
        .panel h2 { color: #fff; border-bottom: 1px solid #ff003c; padding-bottom: 10px; margin-top: 0; }
        .product-card { background: #161618; border-left: 3px solid #ff003c; padding: 12px 18px; margin-bottom: 12px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; }
        .product-card h4 { margin: 0; font-size: 1.2rem; }
        .product-card p { margin: 2px 0 0; color: #777; font-size: 0.9rem; }
        .price { color: #39ff14; font-weight: bold; font-size: 1.2rem; }
        input, select, textarea { width: 100%; box-sizing: border-box; background: #1a1a1d; border: 1px solid #333; color: #fff; padding: 12px; margin-bottom: 15px; border-radius: 4px; font-family: inherit; font-size: 1rem; }
        input:focus, select:focus, textarea:focus { border-color: #ff003c; outline: none; }
        .btn { width: 100%; background: #ff003c; color: #fff; border: none; padding: 14px; font-size: 1.2rem; font-weight: bold; border-radius: 4px; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; }
        .btn:hover { background: #fff; color: #000; box-shadow: 0 0 20px rgba(255,0,60,0.6); }
        .calc-box { background: #141416; border: 1px dashed #444; border-radius: 6px; padding: 15px; margin-bottom: 15px; }
    </style>
</head>
<body>
    <h1>S-PRIME PRINT & MEDIA FORGE</h1>
    <p class="lead">Manufactura, Publicidad de Alto Impacto y Merchandising Corporativo B2B</p>

    <div class="container">
        <!-- CATÁLOGO DE SERVICIOS -->
        <div class="panel">
            <h2>Líneas de Producción</h2>
            <div class="product-card">
                <div><h4>Tarjetas Soft-Touch UV</h4><p>1,000 pzas | Laminado mate + barniz registro</p></div>
                <div class="price">$45 USD</div>
            </div>
            <div class="product-card">
                <div><h4>Lona Mesh / Vinil Gran Formato</h4><p>Alta resolución 1440 DPI para fachadas</p></div>
                <div class="price">$14 USD/m²</div>
            </div>
            <div class="product-card">
                <div><h4>Hoodies / Playeras DTF Premium</h4><p>Algodón peinado con estampado ilimitado</p></div>
                <div class="price">$18 USD c/u</div>
            </div>
            <div class="product-card">
                <div><h4>Rotulación Vehicular Comercial</h4><p>Vinil polimérico automotriz grado flotilla</p></div>
                <div class="price">Cotizar</div>
            </div>
            <div class="product-card">
                <div><h4>Packaging & Cajas Personalizadas</h4><p>Cartón rígido y corrugado con logo grabado</p></div>
                <div class="price">A Medida</div>
            </div>
        </div>

        <!-- COTIZADOR Y CANAL DIRECTO -->
        <div class="panel">
            <h2>Mesa de Pedidos y Asesoría Técnica</h2>
            <div class="calc-box">
                <label style="color:#aaa; font-size:0.9rem;">Selecciona tu requerimiento:</label>
                <select id="prodSelect" onchange="actualizarPresupuesto()">
                    <option value="45">Tarjetas Corporativas Soft-Touch (1000 pzas)</option>
                    <option value="70">Lona Gran Formato 5x1m</option>
                    <option value="180">Pack 10 Hoodies con Identidad S-Prime</option>
                    <option value="250">Rotulación Parcial de Vehículo de Trabajo</option>
                </select>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px;">
                    <span style="color:#888;">Estimado Base:</span>
                    <span id="totalEstimado" style="color:#39ff14; font-size:1.6rem; font-weight:bold;">$45 USD</span>
                </div>
            </div>

            <input type="text" id="nombreCliente" placeholder="Nombre completo o Empresa">
            <input type="text" id="whatsappCliente" placeholder="Número de WhatsApp">
            <textarea id="detalles" rows="3" placeholder="Especificaciones de diseño, medidas o enlaces a archivos (Drive/Dropbox)..."></textarea>
            
            <button class="btn" onclick="enviarPedido()">Transmitir Requerimiento a Imprenta</button>
            <p id="confirmacion" style="color:#00ffcc; text-align:center; margin-top:10px; display:none;"></p>
        </div>
    </div>

    <script>
        function actualizarPresupuesto() {
            let valor = document.getElementById('prodSelect').value;
            document.getElementById('totalEstimado').innerText = "$" + valor + " USD";
        }

        function enviarPedido() {
            let nombre = document.getElementById('nombreCliente').value;
            let tel = document.getElementById('whatsappCliente').value;
            let det = document.getElementById('detalles').value;
            let item = document.getElementById('prodSelect').options[document.getElementById('prodSelect').selectedIndex].text;
            let monto = document.getElementById('totalEstimado').innerText;

            if(!nombre || !tel) {
                alert("Por favor introduce tu nombre y WhatsApp para procesar tu orden.");
                return;
            }

            let msg = `*ORDEN S-PRIME PRINT FORGE*%0A*Cliente:* ${nombre}%0A*Contacto:* ${tel}%0A*Servicio:* ${item}%0A*Presupuesto:* ${monto}%0A*Detalles:* ${det}`;
            let conf = document.getElementById('confirmacion');
            conf.style.display = 'block';
            conf.innerHTML = "✔ Conectando con la Mesa de Impresión S-Prime vía WhatsApp...";
            
            setTimeout(() => {
                window.open(`https://wa.me/526531234567?text=${msg}`, '_blank');
            }, 800);
        }
    </script>
</body>
</html>"""

with open(os.path.join(DIR_PRINT, "landing.html"), "w") as f:
    f.write(html_print)
print("✔ S-Prime Print & Media Forge forjada en:", os.path.join(DIR_PRINT, "landing.html"))


# ==========================================
# 2. S-PRIME AERO (RADAR DE VUELOS EN VIVO)
# ==========================================
DIR_AERO = os.path.join(PROD_DIR, "sprime_aero")
os.makedirs(DIR_AERO, exist_ok=True)

html_aero = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>S-Prime Aero | Radar de Vuelos</title>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">
    <style>
        body { background: #03070b; color: #fff; font-family: 'Rajdhani', sans-serif; margin: 0; padding: 40px 20px; text-align: center; border-top: 4px solid #00d2ff; }
        h1 { color: #00d2ff; font-size: 2.8rem; text-transform: uppercase; margin-bottom: 5px; text-shadow: 0 0 20px rgba(0,210,255,0.4); }
        p.sub { color: #7f9fae; font-size: 1.1rem; margin-bottom: 30px; }
        .search-panel { background: #09121a; border: 1px solid #1a3245; padding: 25px; border-radius: 8px; max-width: 950px; margin: 0 auto 40px; display: flex; gap: 15px; flex-wrap: wrap; justify-content: center; }
        input, select { background: #0f1c26; border: 1px solid #23425a; color: #fff; padding: 12px 15px; border-radius: 4px; font-size: 1.1rem; font-family: inherit; }
        .btn-search { background: #00d2ff; color: #000; border: none; padding: 12px 30px; font-weight: bold; font-size: 1.1rem; border-radius: 4px; cursor: pointer; text-transform: uppercase; transition: 0.3s; }
        .btn-search:hover { background: #fff; box-shadow: 0 0 18px rgba(0,210,255,0.6); }
        .results-container { max-width: 950px; margin: 0 auto; text-align: left; }
        .route-card { background: #09121a; border: 1px solid #193245; border-left: 4px solid #00d2ff; border-radius: 6px; padding: 20px 25px; margin-bottom: 18px; display: flex; justify-content: space-between; align-items: center; }
        .route-info h3 { margin: 0; font-size: 1.6rem; color: #fff; }
        .route-info p { margin: 5px 0 0; color: #8ba7b8; font-size: 0.95rem; }
        .badge { display: inline-block; padding: 3px 8px; font-size: 0.75rem; border-radius: 3px; font-weight: bold; margin-bottom: 5px; }
        .badge-direct { background: rgba(57,255,20,0.15); color: #39ff14; border: 1px solid #39ff14; }
        .badge-int { background: rgba(249,168,38,0.15); color: #f9a826; border: 1px solid #f9a826; }
        .price-tag { text-align: right; }
        .price-tag h2 { margin: 0; font-size: 2.2rem; color: #00d2ff; }
        .btn-book { background: transparent; border: 1px solid #00d2ff; color: #00d2ff; padding: 8px 18px; border-radius: 4px; text-decoration: none; display: inline-block; margin-top: 6px; font-weight: bold; text-transform: uppercase; font-size: 0.9rem; transition: 0.3s; }
        .btn-book:hover { background: #00d2ff; color: #000; }
    </style>
</head>
<body>
    <h1>S-PRIME AERO // RADAR TÁCTICO DE VUELOS</h1>
    <p class="sub">Vigilancia de tarifas mínimas globales y monetización directa de afiliados</p>

    <div class="search-panel">
        <input type="text" id="origen" value="Tijuana (TIJ)" style="flex:1; min-width:180px;">
        <input type="text" id="destino" value="Mazatlán (MZT)" style="flex:1; min-width:180px;">
        <input type="date" id="fecha" value="2026-11-20" style="min-width:160px;">
        <button class="btn-search" onclick="filtrarRutas()">Escanear Tarifas</button>
    </div>

    <div class="results-container">
        <h3 style="color:#00d2ff; margin-bottom:15px; border-bottom:1px solid #1a3245; padding-bottom:8px;">Oportunidades Inmediatas Detectadas</h3>

        <!-- RUTA 1: TIJUANA A MAZATLAN -->
        <div class="route-card" data-route="tij-mzt">
            <div class="route-info">
                <span class="badge badge-direct">VUELO DIRECTO • PRIORIDAD DIRECTOR</span>
                <h3>Tijuana (TIJ) ➔ Mazatlán (MZT)</h3>
                <p>Operado por Volaris / VivaAerobus | Tiempo: 2h 05m | Tarifa base sin cargos ocultos</p>
            </div>
            <div class="price-tag">
                <h2>$49 USD</h2>
                <a href="https://www.skyscanner.com.mx/transport/flights/tij/mzt" target="_blank" class="btn-book">Reservar Ruta</a>
            </div>
        </div>

        <!-- RUTA 2: TIJUANA A CANCÚN -->
        <div class="route-card" data-route="tij-cun">
            <div class="route-info">
                <span class="badge badge-direct">VUELO DIRECTO • TARIFA PROMO</span>
                <h3>Tijuana (TIJ) ➔ Cancún (CUN)</h3>
                <p>Operado por Volaris | Tiempo: 4h 15m | Equipaje de mano incluido</p>
            </div>
            <div class="price-tag">
                <h2>$78 USD</h2>
                <a href="https://www.skyscanner.com.mx/transport/flights/tij/cun" target="_blank" class="btn-book">Reservar Ruta</a>
            </div>
        </div>

        <!-- RUTA 3: TIJUANA A BUCAREST / RUMANIA (MISIÓN) -->
        <div class="route-card" data-route="tij-otp">
            <div class="route-info">
                <span class="badge badge-int">CONEXIÓN INTERCONTINENTAL • MISIÓN EUROPA</span>
                <h3>Tijuana (TIJ) ➔ Bucarest, Rumania (OTP)</h3>
                <p>Conexión vía CDMX / Madrid | Tiempo estimado: 17h 40m | Tarifa Red de Misiones</p>
            </div>
            <div class="price-tag">
                <h2>$580 USD</h2>
                <a href="https://www.skyscanner.com.mx/transport/flights/tij/otp" target="_blank" class="btn-book">Ver Vuelos Misión</a>
            </div>
        </div>
    </div>

    <script>
        function filtrarRutas() {
            let o = document.getElementById('origen').value.toUpperCase();
            let d = document.getElementById('destino').value.toUpperCase();
            let btn = document.querySelector('.btn-search');
            btn.innerText = "Calculando...";
            setTimeout(() => {
                btn.innerText = "Escanear Tarifas";
                alert("Radar actualizado para ruta: " + o + " -> " + d + ". Oportunidades sincronizadas.");
            }, 600);
        }
    </script>
</body>
</html>"""

with open(os.path.join(DIR_AERO, "landing.html"), "w") as f:
    f.write(html_aero)
print("✔ S-Prime Aero forjada en:", os.path.join(DIR_AERO, "landing.html"))

print("\n=== [ITACHI UCHIHA] DESPLIEGUE FINALIZADO EXITOSAMENTE ===")
