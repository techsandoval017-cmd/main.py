import os

ruta = "productos/sprime_kinetic_auto/landing.html"
os.makedirs(os.path.dirname(ruta), exist_ok=True)

html_mecanica_real = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S-Prime Kinetic | Reconstrucción FT 150G</title>
    <style>
        body { background-color: #0d0d0d; color: #ffffff; font-family: 'Courier New', monospace; margin: 0; padding: 0; }
        header { background: #1a1a1a; padding: 20px; text-align: center; border-bottom: 2px solid #ff4500; }
        h1 { color: #ff4500; text-transform: uppercase; letter-spacing: 2px; }
        .container { max-width: 900px; margin: 40px auto; padding: 20px; }
        .evidence-box { background: #111; border: 1px dashed #ff4500; padding: 20px; margin: 20px 0; text-align: center; }
        .btn { display: inline-block; background: #ff4500; color: #fff; padding: 15px 30px; text-decoration: none; font-weight: bold; font-size: 1.2em; text-transform: uppercase; margin-top: 20px; border-radius: 5px; }
        .btn:hover { background: #cc3700; }
        .proveedores { background: #222; padding: 15px; margin-top: 20px; border-left: 4px solid #ff4500; }
    </style>
</head>
<body>
    <header>
        <h1>S-Prime Kinetic: Motocicletas</h1>
        <p>Aprende, repara y capitaliza. De cero a experto.</p>
    </header>
    <div class="container">
        <h2>🔥 MASTERCLASS: RECONSTRUCCIÓN MOTOR FT 150G</h2>
        <p>Un mecánico te cobraría $1,800 MXN solo por abrirlo. Aquí te enseñamos cómo lo desarmamos pieza por pieza desde cero. Sin teoría vacía, pura grasa y fierros.</p>
        
        <div class="evidence-box">
            <h3>[ESPACIO PARA TUS FOTOS/VIDEOS DEL MOTOR]</h3>
            <p style="color: #666;">(Aquí incrustaremos tus videos de TikTok o archivos subidos del motor desarmado)</p>
        </div>

        <div class="proveedores">
            <h3>Nuestros Proveedores Oficiales (Donde compramos las piezas)</h3>
            <ul>
                <li>Alessia / Sayto (Refacciones Internas)</li>
                <li>Roda (Baleros y Tracción)</li>
                <li>Italika Original (Empaques y Sellos)</li>
            </ul>
        </div>

        <div style="text-align: center;">
            <a href="#" class="btn">💳 Descargar Manual Completo ($450 MXN)</a>
            <p style="margin-top: 15px; font-size: 0.9em; color: #888;">¿No tienes tarjeta? <a href="#" style="color: #ff4500;">Tramita una aquí y usa el saldo.</a></p>
        </div>
    </div>
</body>
</html>"""

with open(ruta, "w", encoding="utf-8") as f:
    f.write(html_mecanica_real)

print("✅ Landing Page de Mecánica actualizada para alojar tus videos de la FT 150G.")
