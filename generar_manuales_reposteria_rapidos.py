import os

OUT_DIR = "productos/nichos/manuales"
os.makedirs(OUT_DIR, exist_ok=True)

ITEMS = [
    {
        "file": "guia_galletas_ny.html",
        "titulo": "Mini Negocio: Galletas Gigantes Estilo New York",
        "sub": "Inversión baja, alta densidad y 72% de margen neto",
        "img": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?auto=format&fit=crop&w=900&q=80",
        "costo": "$18.00 MXN",
        "venta": "$65.00 MXN",
        "ganancia": "$47.00 MXN (72%)",
        "ingredientes": "200g mantequilla fría, 150g azúcar mascabado, 100g azúcar blanca, 2 huevos, 350g harina trigo, 1 cdta polvo hornear, 250g chispas chocolate 54%.",
        "proceso": "Bolear esferas de 140g. Congelar mínimo 2 horas a -18°C. Hornear directo del congelador a 200°C por 10 a 11 minutos exactos. Empacar en bolsa celofán con etiqueta circular."
    },
    {
        "file": "guia_pay_individual.html",
        "titulo": "Mini Negocio: Pay Frío de Queso & Limón (Sin Horno)",
        "sub": "Cero gasto de gas, producción en serie en formato 8oz",
        "img": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=900&q=80",
        "costo": "$23.00 MXN",
        "venta": "$65.00 MXN",
        "ganancia": "$42.00 MXN (65%)",
        "ingredientes": "Base: 80g galleta triturada + 40g mantequilla derretida. Relleno: 1 barra queso crema (190g), 1 lata leche condensada, zumo de 3 limones frescos.",
        "proceso": "Compactar galleta al fondo del vaso domo. Licuar queso, condensada y jugo de limón. Verter en moldes. Refrigerar 4 horas antes de vender. Decorar con ralladura de limón."
    },
    {
        "file": "guia_bento_cake.html",
        "titulo": "Mini Negocio: Bento Cakes Minimalistas",
        "sub": "Pasteles individuales de 10cm en caja ecológica para regalo",
        "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80",
        "costo": "$40.50 MXN",
        "venta": "$160.00 MXN",
        "ganancia": "$119.50 MXN (74%)",
        "ingredientes": "Bizcocho esponja 10cm, emulsión tres leches (evaporada, condensada, crema), relleno mermelada/cajeta, cobertura crema chantilly vegetal.",
        "proceso": "Hornear en molde circular 10cm a 165°C por 22 min. Dejar reposar en frío 12 horas. Armar, humectar con jarabe tres leches, embetunar liso y decorar con frases en letras finas. Colocar en caja de hamburguesa con papel encerado."
    }
]

for item in ITEMS:
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{item['titulo']}</title>
<style>
  body {{ font-family: Arial, sans-serif; max-width: 750px; margin: 30px auto; padding: 20px; color: #222; line-height: 1.6; }}
  h1 {{ color: #111; margin-bottom: 5px; }}
  .sub {{ color: #666; font-size: 14px; margin-bottom: 20px; }}
  img {{ width: 100%; height: 320px; object-fit: cover; border-radius: 8px; margin-bottom: 20px; }}
  .box {{ background: #f4f6f8; border-left: 4px solid #28a745; padding: 15px; margin-bottom: 20px; border-radius: 4px; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
  th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
  th {{ background: #eee; }}
  .cta {{ display: block; text-align: center; background: #28a745; color: #fff; padding: 14px; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 25px; }}
</style>
</head>
<body>
  <h1>{item['titulo']}</h1>
  <div class="sub">{item['sub']}</div>
  <img src="{item['img']}" alt="{item['titulo']}">
  
  <div class="box">
    <strong>Estructura Financiera Rápida:</strong>
    <table>
      <tr><th>Costo de Elaboración + Empaque</th><td>{item['costo']}</td></tr>
      <tr><th>Precio de Venta Sugerido</th><td><strong>{item['venta']}</strong></td></tr>
      <tr><th>Ganancia Neta por Pieza</th><td><strong style="color: #28a745;">{item['ganancia']}</strong></td></tr>
    </table>
  </div>

  <h3>Ingredientes Estandarizados:</h3>
  <p>{item['ingredientes']}</p>

  <h3>Proceso Operativo:</h3>
  <p>{item['proceso']}</p>

  <a class="cta" href="https://wa.me/?text=Hola%2C%20quiero%20ordenar%20mi%20pedido%20de%20{item['titulo']}">Hacer Pedido por WhatsApp</a>
</body>
</html>"""
    path = os.path.join(OUT_DIR, item['file'])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✔ Generado: {path}")

print("\n🚀 LISTO: Entra a tu navegador en http://127.0.0.1:8050/nichos/manuales/guia_galletas_ny.html para verlos.")
