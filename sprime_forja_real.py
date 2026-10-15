import os

# 1. CREAR LA BÓVEDA DE ENTREGABLES
base_dir = "entregables_reales"
os.makedirs(base_dir, exist_ok=True)

print("="*60)
print("⚡ [S-PRIME FORGE] GENERANDO SOFTWARE Y MANUALES REALES ⚡")
print("="*60)

# ==========================================
# NÚMERO 1: BARBERÍA (Para tu amigo)
# ==========================================
dir_barberia = os.path.join(base_dir, "01_Barberia_VIP")
os.makedirs(dir_barberia, exist_ok=True)

html_barberia = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>S-Prime Barber VIP | Gestor</title>
    <style>
        body { background: #0a0a0a; color: #fff; font-family: monospace; padding: 20px; }
        h1 { color: #d4af37; border-bottom: 1px solid #d4af37; padding-bottom: 10px; }
        .panel { background: #111; padding: 20px; border: 1px solid #333; border-radius: 5px; margin-bottom: 20px; }
        input, button { padding: 10px; margin: 5px; background: #222; color: #fff; border: 1px solid #d4af37; }
        button { cursor: pointer; background: #d4af37; color: #000; font-weight: bold; }
    </style>
</head>
<body>
    <h1>💈 S-PRIME BARBER VIP - TIER 2</h1>
    <div class="panel">
        <h3>Calculadora de Comisiones Diarias</h3>
        <input type="number" id="cortes" placeholder="Número de Cortes">
        <input type="number" id="precio" placeholder="Precio por Corte ($)">
        <input type="number" id="porcentaje" placeholder="% para el Barbero (Ej. 50)">
        <button onclick="calcular()">Calcular Cierre</button>
        <p id="resultado" style="color: #00ffcc; font-size: 1.2em;"></p>
    </div>
    <script>
        function calcular() {
            let c = document.getElementById('cortes').value;
            let p = document.getElementById('precio').value;
            let pct = document.getElementById('porcentaje').value;
            let total = c * p;
            let barbero = total * (pct / 100);
            let casa = total - barbero;
            document.getElementById('resultado').innerText = 
                `Ingreso Total: $${total} | Ganancia Casa: $${casa} | Pago Barbero: $${barbero}`;
        }
    </script>
</body>
</html>"""
with open(os.path.join(dir_barberia, "SPrime_Barber_App.html"), "w", encoding="utf-8") as f: f.write(html_barberia)
with open(os.path.join(dir_barberia, "Manual_Operativo.txt"), "w", encoding="utf-8") as f: 
    f.write("S-PRIME BARBERÍA VIP\n\n1. Modelo de Negocio: Renta de silla vs % de corte.\n2. Insumos clave: Navajas, Minoxidil (Upsell).\n3. Retención: Ofrecer bebida de cortesía aumenta la propina en un 30%.")

# ==========================================
# NÚMERO 2: REPOSTERÍA (Para tus primas)
# ==========================================
dir_reposteria = os.path.join(base_dir, "02_Reposteria_DarkKitchen")
os.makedirs(dir_reposteria, exist_ok=True)

html_reposteria = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>S-Prime Bakery | Costeos</title>
    <style>
        body { background: #1a1015; color: #fff; font-family: monospace; padding: 20px; }
        h1 { color: #ff66b2; border-bottom: 1px solid #ff66b2; }
        .panel { background: #2a1a22; padding: 20px; border: 1px solid #4a2a3a; }
        input, button { padding: 10px; margin: 5px; background: #000; color: #fff; border: 1px solid #ff66b2; }
        button { background: #ff66b2; color: #000; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <h1>🍰 S-PRIME COSTEO EXACTO (Bento Cakes / Galletas)</h1>
    <div class="panel">
        <h3>Cotizador de Receta</h3>
        <input type="number" id="costo_insumos" placeholder="Costo total ingredientes ($)">
        <input type="number" id="tiempo_horas" placeholder="Horas de trabajo">
        <input type="number" id="pago_hora" placeholder="Tu pago por hora ($)">
        <button onclick="calcularPrecio()">Fijar Precio de Venta</button>
        <p id="res" style="color: #00ffcc; font-size: 1.2em;"></p>
    </div>
    <script>
        function calcularPrecio() {
            let insumos = parseFloat(document.getElementById('costo_insumos').value);
            let horas = parseFloat(document.getElementById('tiempo_horas').value);
            let pago = parseFloat(document.getElementById('pago_hora').value);
            let costo_produccion = insumos + (horas * pago);
            let precio_venta = costo_produccion * 3; // Regla de 3 en repostería
            document.getElementById('res').innerText = 
                `Costo Real: $${costo_produccion} | Precio Sugerido de Venta: $${precio_venta} | Ganancia Neta: $${precio_venta - costo_produccion}`;
        }
    </script>
</body>
</html>"""
with open(os.path.join(dir_reposteria, "SPrime_Costeo_Reposteria.html"), "w", encoding="utf-8") as f: f.write(html_reposteria)

# ==========================================
# NÚMERO 3: LLANTERA (Para tu cuñado)
# ==========================================
dir_llantera = os.path.join(base_dir, "03_Llantera_Vulcanizadora")
os.makedirs(dir_llantera, exist_ok=True)

html_llantera = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>S-Prime Vulcan | Manager</title>
    <style>
        body { background: #111; color: #fff; font-family: monospace; padding: 20px; }
        h1 { color: #ff3300; border-bottom: 1px solid #ff3300; }
        .panel { background: #222; padding: 20px; border: 1px dashed #ff3300; }
        input, button { padding: 10px; margin: 5px; background: #000; color: #fff; border: 1px solid #ff3300; }
        button { background: #ff3300; color: #000; font-weight: bold; cursor: pointer;}
    </style>
</head>
<body>
    <h1>⚙️ S-PRIME VULCAN MANAGER</h1>
    <div class="panel">
        <h3>Cotizador de Servicio Rápido</h3>
        <input type="text" id="rodado" placeholder="Rodado (Ej. 15, 17, 20)">
        <input type="number" id="parches" placeholder="Llantas a parchar">
        <input type="number" id="balanceos" placeholder="Llantas a balancear">
        <button onclick="calcularServicio()">Generar Ticket</button>
        <p id="ticket" style="color: #00ffcc; font-size: 1.2em; white-space: pre-line;"></p>
    </div>
    <script>
        function calcularServicio() {
            let parches = document.getElementById('parches').value * 80; // $80 parche
            let balanceos = document.getElementById('balanceos').value * 120; // $120 balanceo
            let total = parches + balanceos;
            document.getElementById('ticket').innerText = 
                `Costo Parches: $${parches}\nCosto Balanceo: $${balanceos}\n----------------\nTOTAL A COBRAR: $${total}`;
        }
    </script>
</body>
</html>"""
with open(os.path.join(dir_llantera, "SPrime_Vulcan_App.html"), "w", encoding="utf-8") as f: f.write(html_llantera)

# ==========================================
# NÚMERO 4: MECÁNICA DE MOTOS
# ==========================================
dir_motos = os.path.join(base_dir, "04_Mecanica_Motos")
os.makedirs(dir_motos, exist_ok=True)
with open(os.path.join(dir_motos, "Checklist_Diagnostico.txt"), "w", encoding="utf-8") as f: 
    f.write("S-PRIME KINETIC MOTOS - CHECKLIST DE INGRESO\n[ ] Voltaje de Batería (Min 12.4V)\n[ ] Estado de Bujías\n[ ] Tensión de Cadena\n[ ] Fugas en Retenes de Suspensión")

print("✔ Entregables Reales Generados en: /entregables_reales")
