import os

ruta_import = "productos/sprime_import_motors/landing.html"
os.makedirs(os.path.dirname(ruta_import), exist_ok=True)

html_importacion = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S-Prime | Importaciones Motor (China a MEX)</title>
    <style>
        body { background-color: #050505; color: #ffffff; font-family: 'Courier New', monospace; margin: 0; padding: 20px; }
        h1 { color: #00ffcc; text-transform: uppercase; border-bottom: 2px solid #00ffcc; padding-bottom: 10px; text-align: center; }
        .grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 30px; }
        .producto { background: #111; border: 1px solid #333; padding: 20px; width: 300px; border-radius: 8px; text-align: center; }
        .producto h3 { color: #d4af37; }
        .precio { color: #00ffcc; font-size: 1.5em; font-weight: bold; margin: 15px 0; }
        .btn { display: inline-block; background: #00ffcc; color: #000; padding: 10px 20px; text-decoration: none; font-weight: bold; border-radius: 5px; text-transform: uppercase; }
        .btn:hover { background: #00ccaa; }
    </style>
</head>
<body>
    <h1>🚢 S-Prime Import Division: Ensamblaje de Motocicletas</h1>
    <p style="text-align: center; color: #888;">Piezas importadas directamente de fabricantes OEM en China. Arma y multiplica tus ganancias.</p>
    
    <div class="grid">
        <div class="producto">
            <h3>Motor Zongshen 250cc (Enfriado por Aire)</h3>
            <p>Ideal para proyectos Cafe Racer o reemplazos FT 150.</p>
            <div class="precio">$4,500 MXN</div>
            <a href="#" class="btn">Solicitar Cotización</a>
        </div>
        <div class="producto">
            <h3>Kit Suspensión Invertida (Universal)</h3>
            <p>Mejora de alto rendimiento para motos de trabajo.</p>
            <div class="precio">$2,100 MXN</div>
            <a href="#" class="btn">Solicitar Cotización</a>
        </div>
        <div class="producto">
            <h3>Chasis Tubular (Estilo Scrambler)</h3>
            <p>Estructura lista para soldadura y ensamble personalizado.</p>
            <div class="precio">$3,800 MXN</div>
            <a href="#" class="btn">Solicitar Cotización</a>
        </div>
    </div>
</body>
</html>"""

with open(ruta_import, "w", encoding="utf-8") as f:
    f.write(html_importacion)

print("✅ Landing Page de Importación de Motos forjada con éxito.")
