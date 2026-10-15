import os

base_dir = "entregables_reales"
os.makedirs(base_dir, exist_ok=True)

print("="*60)
print("⚡ [S-PRIME FORGE] INYECTANDO NICHO 5 AL 10 (RANGO S) ⚡")
print("="*60)

# ==========================================
# 5. HERRERÍA Y SOLDADURA (Para tu primo)
# ==========================================
dir_herreria = os.path.join(base_dir, "05_Soldadura_Herreria")
os.makedirs(dir_herreria, exist_ok=True)
html_herreria = """<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>S-Prime Iron | Cotizador</title>
<style>body{background:#1a1a1a;color:#fff;font-family:monospace;padding:20px;} h1{color:#ff5500;border-bottom:1px solid #ff5500;} input,button{padding:10px;margin:5px;background:#000;color:#fff;border:1px solid #ff5500;} button{background:#ff5500;color:#000;font-weight:bold;cursor:pointer;}</style></head>
<body><h1>🔥 S-PRIME IRON WORKS - COTIZADOR</h1>
<h3>Proyecto Estructural / Herrería</h3>
<input type="number" id="mat" placeholder="Costo Materiales (Metales/Electrodos) $">
<input type="number" id="dias" placeholder="Días estimados de trabajo">
<input type="number" id="pago_dia" placeholder="Cobro por día (Mano de obra) $">
<button onclick="calc()">Generar Presupuesto</button>
<p id="res" style="color:#00ffcc;font-size:1.2em;"></p>
<script>
function calc(){
    let mat = parseFloat(document.getElementById('mat').value);
    let obra = document.getElementById('dias').value * document.getElementById('pago_dia').value;
    let subtotal = mat + obra;
    let total = subtotal * 1.30; // 30% margen de ganancia del taller
    document.getElementById('res').innerText = `Material: $${mat} | Mano Obra: $${obra} | PRESUPUESTO CLIENTE: $${total.toFixed(2)}`;
}
</script></body></html>"""
with open(os.path.join(dir_herreria, "SPrime_Iron_App.html"), "w", encoding="utf-8") as f: f.write(html_herreria)

# ==========================================
# 6. CARPINTERÍA (Para tu tío)
# ==========================================
dir_carp = os.path.join(base_dir, "06_Carpinteria_Melamina")
os.makedirs(dir_carp, exist_ok=True)
html_carp = """<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>S-Prime Wood | Optimizador</title>
<style>body{background:#2c221a;color:#fff;font-family:monospace;padding:20px;} h1{color:#ffaa00;border-bottom:1px solid #ffaa00;} input,button{padding:10px;margin:5px;background:#1a140f;color:#fff;border:1px solid #ffaa00;} button{background:#ffaa00;color:#000;font-weight:bold;cursor:pointer;}</style></head>
<body><h1>🪚 S-PRIME WOODCRAFT - MELAMINA</h1>
<h3>Cotizador de Muebles a Medida</h3>
<input type="number" id="hojas" placeholder="Hojas de Melamina">
<input type="number" id="precio_hoja" placeholder="Precio x Hoja $">
<input type="number" id="herrajes" placeholder="Costo Total Herrajes (Bisagras/Rieles) $">
<button onclick="calc()">Calcular Mueble</button>
<p id="res" style="color:#00ffcc;font-size:1.2em;"></p>
<script>
function calc(){
    let costo_tableros = document.getElementById('hojas').value * document.getElementById('precio_hoja').value;
    let herr = parseFloat(document.getElementById('herrajes').value);
    let costo_base = costo_tableros + herr;
    let precio_venta = costo_base * 2.5; // Regla general de carpintería
    document.getElementById('res').innerText = `Costo Producción: $${costo_base} | PRECIO AL CLIENTE: $${precio_venta.toFixed(2)} | Tu Ganancia: $${(precio_venta - costo_base).toFixed(2)}`;
}
</script></body></html>"""
with open(os.path.join(dir_carp, "SPrime_Wood_App.html"), "w", encoding="utf-8") as f: f.write(html_carp)

# ==========================================
# 7. REPARACIÓN DE PC / LAPTOPS
# ==========================================
dir_pc = os.path.join(base_dir, "07_Reparacion_PC")
os.makedirs(dir_pc, exist_ok=True)
html_pc = """<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>S-Prime PC Builder</title>
<style>body{background:#001122;color:#fff;font-family:monospace;padding:20px;} h1{color:#00ccff;border-bottom:1px solid #00ccff;} select,button{padding:10px;margin:5px;background:#000;color:#fff;border:1px solid #00ccff;} button{background:#00ccff;color:#000;font-weight:bold;cursor:pointer;}</style></head>
<body><h1>💻 S-PRIME PC FIX - TICKET GENERATOR</h1>
<h3>Selecciona Servicios:</h3>
<select id="serv1"><option value="0">Ninguno</option><option value="400">Formateo + Win11 ($400)</option><option value="600">Mantenimiento Térmico ($600)</option></select>
<select id="serv2"><option value="0">Ninguno</option><option value="800">Instalación SSD ($800)</option><option value="1500">Reballing GPU ($1500)</option></select>
<button onclick="calc()">Emitir Ticket</button>
<p id="res" style="color:#00ffcc;font-size:1.2em;"></p>
<script>
function calc(){
    let s1 = parseFloat(document.getElementById('serv1').value);
    let s2 = parseFloat(document.getElementById('serv2').value);
    document.getElementById('res').innerText = `TOTAL SERVICIOS: $${s1 + s2} MXN`;
}
</script></body></html>"""
with open(os.path.join(dir_pc, "SPrime_PC_Ticket.html"), "w", encoding="utf-8") as f: f.write(html_pc)

# ==========================================
# 8. REPARACIÓN DE CELULARES
# ==========================================
dir_cel = os.path.join(base_dir, "08_Reparacion_Celulares")
os.makedirs(dir_cel, exist_ok=True)
html_cel = html_pc.replace("PC FIX", "MOBILE TECH").replace("Formateo + Win11 ($400)", "Cambio Centro de Carga ($350)").replace("Mantenimiento Térmico ($600)", "Cambio Pantalla Gral ($1200)").replace("Instalación SSD ($800)", "Microsoldadura SMD ($900)").replace("Reballing GPU ($1500)", "Rescate por Agua ($800)")
with open(os.path.join(dir_cel, "SPrime_Mobile_App.html"), "w", encoding="utf-8") as f: f.write(html_cel)

# ==========================================
# 9. IMPRESIÓN 3D (S-Prime Forge)
# ==========================================
dir_3d = os.path.join(base_dir, "09_Impresion_3D")
os.makedirs(dir_3d, exist_ok=True)
html_3d = """<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>S-Prime 3D Forge</title>
<style>body{background:#110022;color:#fff;font-family:monospace;padding:20px;} h1{color:#cc00ff;border-bottom:1px solid #cc00ff;} input,button{padding:10px;margin:5px;background:#000;color:#fff;border:1px solid #cc00ff;} button{background:#cc00ff;color:#000;font-weight:bold;cursor:pointer;}</style></head>
<body><h1>🧊 S-PRIME 3D FORGE - PRINT CALCULATOR</h1>
<input type="number" id="gramos" placeholder="Gramos de Filamento (Cura)">
<input type="number" id="horas" placeholder="Horas de Impresión">
<button onclick="calc()">Calcular Costo Final</button>
<p id="res" style="color:#00ffcc;font-size:1.2em;"></p>
<script>
function calc(){
    let costo_mat = document.getElementById('gramos').value * 0.40; // $0.40 por gramo aprox
    let costo_luz_desgaste = document.getElementById('horas').value * 10; // $10 por hora
    let costo_total = costo_mat + costo_luz_desgaste;
    document.getElementById('res').innerText = `Costo Producción: $${costo_total.toFixed(2)} | Véndelo en: $${(costo_total * 4).toFixed(2)}`;
}
</script></body></html>"""
with open(os.path.join(dir_3d, "SPrime_3D_App.html"), "w", encoding="utf-8") as f: f.write(html_3d)

# ==========================================
# 10. MECATRÓNICA / ELECTRÓNICA
# ==========================================
dir_meca = os.path.join(base_dir, "10_Mecatronica")
os.makedirs(dir_meca, exist_ok=True)
html_meca = html_3d.replace("3D FORGE - PRINT CALCULATOR", "KINETIC LABS - MECATRÓNICA").replace("Gramos de Filamento (Cura)", "Costo de Componentes ($)").replace("Horas de Impresión", "Horas de Diseño (PCB/Código)").replace("0.40", "1").replace("10", "350")
with open(os.path.join(dir_meca, "SPrime_Mecatronica_App.html"), "w", encoding="utf-8") as f: f.write(html_meca)

print("✔ Despliegue completado. Las 10 herramientas funcionales están en /entregables_reales")
