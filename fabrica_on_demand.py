import os
import time

# Base de datos de la cola de producción (Los 9 productos restantes)
productos = [
    {
        "id": "02_vacio_purpura_gojo",
        "nombre": "Stand Audífonos: Vacío Púrpura",
        "nicho": "Gamer / Home Office",
        "precio": "60.00",
        "desc_corta": "Busto minimalista con integración de iluminación LED violeta hacia la diadema.",
        "features": [
            ("Iluminación Integrada", "Esfera de resina translúcida con LED reactivo interno."),
            ("Centro de Gravedad", "Base de metal fundido o resina de alta densidad para evitar caídas."),
            ("Estética Minimalista", "Diseño limpio, negro mate con detalles púrpuras.")
        ],
        "copy_redes": "¿Tus audífonos de $200 USD tirados en la mesa? Eleva tu dominio con el Vacío Púrpura. Iluminación LED y manufactura 3D premium.",
        "costo_fabrica": "22.00"
    },
    {
        "id": "03_magsafe_tsukuyomi_itachi",
        "nombre": "Cargador MagSafe: Tsukuyomi",
        "nicho": "Apple Users / Tech",
        "precio": "35.00",
        "desc_corta": "Placa táctica de carga inalámbrica. Textura de metal oscuro con iluminación LED roja reactiva.",
        "features": [
            ("Compatibilidad MagSafe", "Ranura exacta de 56mm para insertar el disco cargador de Apple."),
            ("Reactividad", "El perímetro carmesí se ilumina sutilmente al detectar el dispositivo."),
            ("Acabado Táctico", "Textura industrial anti-deslizante y estética Akatsuki oscura.")
        ],
        "copy_redes": "Cargar tu teléfono no debería ser aburrido. Placa MagSafe Tsukuyomi. Resina industrial y LEDs reactivos. Rango S.",
        "costo_fabrica": "12.00"
    },
    {
        "id": "04_organizador_sombras_jinwoo",
        "nombre": "Organizador: Ejército de Sombras",
        "nicho": "Productividad / Escritorios",
        "precio": "40.00",
        "desc_corta": "Gestor de escritorio táctico. Diseño de fantasía oscura urbana con yelmos emergiendo.",
        "features": [
            ("Gestión Total", "Compartimentos medidos para Apple Pencil, memorias USB y cables tipo C."),
            ("Detalles Fluorescentes", "Las garras y ojos de las sombras brillan en la oscuridad (Pintura UV)."),
            ("Diseño Monolítico", "Base pesada y angular que impone orden en tu espacio de trabajo.")
        ],
        "copy_redes": "El caos en tu escritorio debilita tu enfoque. Organiza tus herramientas con el Ejército de Sombras. Levántate.",
        "costo_fabrica": "15.00"
    },
    {
        "id": "05_dock_reloj_nave_rick",
        "nombre": "Dock Smartwatch: Nave C-137",
        "nicho": "Wearables / Sci-Fi",
        "precio": "30.00",
        "desc_corta": "Réplica a escala de la nave. El Apple Watch/Galaxy Watch actúa como el parabrisas.",
        "features": [
            ("Ingeniería de Cables", "Túneles internos diseñados para ocultar el cable de carga por completo."),
            ("Modo Mesita de Noche", "Mantiene el reloj en ángulo horizontal perfecto para ver la hora en la oscuridad."),
            ("Pintura Automotriz", "Acabado plateado metalizado resistente a rayaduras.")
        ],
        "copy_redes": "No dejes tu smartwatch tirado. Conviértelo en el parabrisas de la Nave C-137. Dock de carga impreso en 3D.",
        "costo_fabrica": "10.00"
    },
    {
        "id": "06_caja_cables_nube_goku",
        "nombre": "Caja de Cables: Nube Voladora",
        "nicho": "Setup Limpio / Organización",
        "precio": "45.00",
        "desc_corta": "Oculta tus regletas bajo la icónica nube dorada texturizada. Adiós al desorden de cables.",
        "features": [
            ("Termo-Resistente", "Impreso en material ABS/PETG para soportar el calor de los cargadores."),
            ("Capacidad XXL", "Espacio suficiente para una regleta de 6 tomas y múltiples cargadores de laptop."),
            ("Estética Nostálgica", "La tapa es un modelo 3D detallado de la nube voladora en dorado mate.")
        ],
        "copy_redes": "El enemigo #1 de un setup limpio: Los cables. Ocúltalos con la Nube Voladora. Ingeniería y nostalgia unidas.",
        "costo_fabrica": "18.00"
    },
    {
        "id": "07_soporte_gpu_nichirin",
        "nombre": "Soporte GPU: Nichirin Blade",
        "nicho": "PC Builders / Master Race",
        "precio": "25.00",
        "desc_corta": "Evita que tu tarjeta gráfica se doble con esta Katana de resina hecha a medida.",
        "features": [
            ("Altura Ajustable", "Sistema de rosca oculta en la empuñadura para adaptarse a cualquier gabinete."),
            ("Anti-Vibración", "Almohadillas de goma en la punta y la base para proteger el hardware."),
            ("Forjado en Resina", "Resistencia estructural superior al plástico inyectado barato.")
        ],
        "copy_redes": "¿Tu RTX 4090 se está doblando por el peso? Protégela con la Nichirin Blade. Soporte para GPU de grado industrial.",
        "costo_fabrica": "8.00"
    },
    {
        "id": "08_paneles_led_akatsuki",
        "nombre": "Paneles LED: Nubes Akatsuki",
        "nicho": "Decoración / Iluminación",
        "precio": "80.00",
        "desc_corta": "Paneles hexagonales de pared con siluetas huecas. Iluminación reactiva al sonido.",
        "features": [
            ("Modularidad", "Piezas magnéticas que se conectan entre sí. Arma tu propio patrón."),
            ("Control Inteligente", "Microcontrolador WiFi compatible con Alexa y efectos de sonido reactivos."),
            ("Difusión Perfecta", "Cristal acrílico esmerilado impreso en 3D para evitar deslumbramiento LED.")
        ],
        "copy_redes": "Transforma la pared vacía de tu cuarto en la guarida de Akatsuki. Paneles modulares LED reactivos.",
        "costo_fabrica": "35.00"
    },
    {
        "id": "09_lampara_sistema_sololeveling",
        "nombre": "Light-Box: Requisitos Diarios",
        "nicho": "Iluminación / Motivación",
        "precio": "50.00",
        "desc_corta": "Lámpara holográfica azul con el mensaje del sistema: 'Has completado los requisitos diarios'.",
        "features": [
            ("Acrílico Grabado", "Placa cortada con láser iluminada desde una base impresa en 3D."),
            ("Alimentación USB-C", "Conexión moderna, encendido táctil en la base oscura."),
            ("Ambiente Nocturno", "Luz azul fría ideal para escritorios nocturnos o modo lectura.")
        ],
        "copy_redes": "El Sistema te está llamando. Termina tus tareas y enciende tu recompensa. Light-Box exclusiva Obsidian.",
        "costo_fabrica": "18.00"
    },
    {
        "id": "10_base_monitor_mprime",
        "nombre": "Base Elevadora M-Prime",
        "nicho": "Ergonomía / Setups Premium",
        "precio": "90.00",
        "desc_corta": "Soporte de monitor modular de grado industrial con ranuras para exhibir miniaturas.",
        "features": [
            ("Acero y Polímero", "Alma de aluminio recubierta por piezas texturizadas impresas en 3D."),
            ("Ranuras de Exhibición", "Espacios iluminados integrados para colocar tus figuras de colección Rango S."),
            ("Ergonomía", "Eleva el monitor 12cm, previniendo fatiga cervical en jornadas largas.")
        ],
        "copy_redes": "Tu monitor no debe estar sobre una pila de libros. Base M-Prime: Ingeniería ergonómica + Exhibición de colección.",
        "costo_fabrica": "40.00"
    }
]

print("[GOKU / JINWOO / RICK] - Ensamblando archivos de producción en disco...\n")

for prod in productos:
    folder = f"productos_obsidian/{prod['id']}"
    os.makedirs(folder, exist_ok=True)
    
    print(f"➜ Procesando: {prod['nombre']}...")
    
    # 1. GENERAR LANDING PAGE (HTML)
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{prod['nombre']} | Obsidian Smart Spaces</title>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --obsidian-red: #ff003c; --bg-dark: #050505; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Rajdhani', sans-serif; }}
        body {{ background: var(--bg-dark); color: #fff; line-height: 1.6; }}
        .hero {{ height: 100vh; display: flex; align-items: center; justify-content: center; background: radial-gradient(circle at center, #1a0005 0%, #000 80%); padding: 20px; text-align: center; border-bottom: 1px solid rgba(255,0,60,0.2); }}
        .hero-content {{ max-width: 800px; }}
        .badge {{ background: rgba(255,0,60,0.1); color: var(--obsidian-red); padding: 8px 16px; border: 1px solid var(--obsidian-red); border-radius: 20px; font-weight: bold; letter-spacing: 2px; margin-bottom: 20px; display: inline-block; }}
        h1 {{ font-size: 3.5rem; text-transform: uppercase; margin-bottom: 15px; text-shadow: 0 0 20px rgba(255,0,60,0.4); }}
        p.subtitle {{ font-size: 1.2rem; color: #aaa; margin-bottom: 40px; }}
        .price-tag {{ font-size: 2.5rem; font-weight: bold; color: #fff; margin-bottom: 30px; }}
        .btn-checkout {{ background: var(--obsidian-red); color: #fff; padding: 20px 50px; font-size: 1.5rem; font-weight: bold; border: none; border-radius: 6px; cursor: pointer; text-transform: uppercase; box-shadow: 0 0 30px rgba(255,0,60,0.5); transition: 0.3s; width: 100%; max-width: 400px; }}
        .btn-checkout:hover {{ background: #fff; color: var(--obsidian-red); box-shadow: 0 0 40px #fff; }}
        .features {{ padding: 80px 20px; max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }}
        .feature-box {{ background: #0a0a0a; border: 1px solid #222; padding: 30px; border-radius: 8px; }}
        .feature-box h3 {{ color: var(--obsidian-red); font-size: 1.5rem; margin-bottom: 15px; }}
        .feature-box p {{ color: #888; }}
    </style>
</head>
<body>
    <div class="hero">
        <div class="hero-content">
            <div class="badge">MANUFACTURA 3D ON-DEMAND</div>
            <h1>{prod['nombre']}</h1>
            <p class="subtitle">{prod['desc_corta']}</p>
            <div class="price-tag">${prod['precio']} USD</div>
            <button class="btn-checkout">Adquirir Ahora</button>
        </div>
    </div>
    <div class="features">
        <div class="feature-box"><h3>{prod['features'][0][0]}</h3><p>{prod['features'][0][1]}</p></div>
        <div class="feature-box"><h3>{prod['features'][1][0]}</h3><p>{prod['features'][1][1]}</p></div>
        <div class="feature-box"><h3>{prod['features'][2][0]}</h3><p>{prod['features'][2][1]}</p></div>
    </div>
</body>
</html>"""
    with open(os.path.join(folder, "landing.html"), "w") as f:
        f.write(html_content)

    # 2. GENERAR CAMPAÑA DE MARKETING (TXT)
    campana_content = f"""======================================================
Campaña de Marketing: {prod['nombre']}
======================================================
[COPY PARA REDES SOCIALES]
{prod['copy_redes']}
👉 Se fabrica bajo demanda y llega directo a tu puerta. Link en la bio.
#SmartSpaces #ObsidianPrime #Impresion3D #SetupGamer

[ESTRUCTURA DE VIDEO REELS/TIKTOK]
- Seg 0-3: Problema visual (Ej: audífonos tirados, cables enredados, escritorio feo).
- Seg 3-5: Transición oscura glitch.
- Seg 5-12: Toma cinematográfica del producto '{prod['nombre']}' resolviendo el problema con iluminación épica.
- Seg 12-15: Call to Action. "Hardware Rango S. Consíguelo en Obsidian".
"""
    with open(os.path.join(folder, "campana_redes.txt"), "w") as f:
        f.write(campana_content)

    # 3. GENERAR SPECS DE PRODUCCIÓN Y FINANZAS (MD)
    specs_content = f"""# ESPECIFICACIONES DE PRODUCCIÓN: {prod['nombre']}

## Análisis Financiero (Por Unidad)
- **Precio de Venta Público:** ${prod['precio']} USD
- **Costo de Fabricación (On-Demand / Local):** ~${prod['costo_fabrica']} USD
- **Margen de Ganancia Bruto:** ~${float(prod['precio']) - float(prod['costo_fabrica']):.2f} USD

## Instrucciones de Modelado 3D
1. Mantener tolerancias de 0.2mm en uniones o ensambles.
2. Evitar voladizos mayores a 45 grados para imprimir sin soportes excesivos.
3. El archivo final `.STL` debe subirse al servidor de Obsidian para conectarlo con la API de Craftcloud o enviarlo a impresión local.
"""
    with open(os.path.join(folder, "specs_produccion.md"), "w") as f:
        f.write(specs_content)
        
    time.sleep(0.5) # Simulando el procesamiento en cola

print("\n✔ [S-PRIME AI] Operación finalizada. Los 10 productos de Smart Spaces han sido empaquetados y guardados en tu disco local bajo 'productos_obsidian/'.")
