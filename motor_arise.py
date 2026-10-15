import os
import time
import json

# Directorio de producción
BASE_DIR = "productos"
os.makedirs(BASE_DIR, exist_ok=True)

# Catálogo B2B de Alta Demanda (Estructura de Datos)
catalogo = [
    {
        "id": "autofix_engine",
        "nombre": "AutoFix Engine (San Diego Edition)",
        "precio_shopify": "199.00",
        "precio_landing": "129.00",
        "desc": "Software integral para Talleres. Gestión de inventario, citas, finanzas y publicador de ofertas automatizado para empleados.",
        "prompts_video": "Visual: Pantalla dividida. Izquierda: Un taller desorganizado. Derecha: Un monitor mostrando un dashboard oscuro (AutoFix) ordenando citas. Audio: Motor acelerando seguido de un 'ding' de caja registradora. Herramienta recomendada: Canva Pro Video Template + DALL-E para el fondo del taller."
    },
    {
        "id": "toyota_honda_lib",
        "nombre": "Librería Técnica Toyota & Honda",
        "precio_shopify": "89.00",
        "precio_landing": "49.00",
        "desc": "El Santo Grial de los motores eternos. PDF ilustrado para Toyota 22R, Camry 1991 2.0L y software de diagnóstico OBD2 japonés.",
        "prompts_video": "Visual: Un motor sucio de Toyota 22R. Escáner 3D lo limpia y muestra el diagrama de encendido perfecto. Texto en pantalla: 'Domina los motores que nunca mueren'. Herramienta recomendada: ChatGPT Plus (DALL-E 3) para generar diagramas hiperrealistas."
    },
    {
        "id": "smart_carpentry",
        "nombre": "Ecosistema Smart Carpentry",
        "precio_shopify": "120.00",
        "precio_landing": "79.00",
        "desc": "Plantillas de corte de melamina con Inteligencia Artificial. Cero desperdicio de madera, máximas ganancias por mueble.",
        "prompts_video": "Visual: Animación 3D de una plancha de madera cortándose sola con líneas láser verdes (estilo Kinetic) armando un escritorio M-Prime. Herramienta recomendada: Google Veo / Runway Gen-2."
    },
    {
        "id": "golden_blade_barber",
        "nombre": "The Golden Blade VIP",
        "precio_shopify": "150.00",
        "precio_landing": "99.00",
        "desc": "Sistema de agendamiento AI para Barberías de Élite. Cálculos de comisiones y agenda anti-cancelaciones.",
        "prompts_video": "Visual: Una navaja dorada de barbero brillando sobre una toalla negra. Transición a un celular donde caen notificaciones de cobro Stripe. Herramienta recomendada: Canva Pro Video."
    }
]

print("=== INICIANDO MOTOR ARISE: CREACIÓN EN BUCLE ===\n")

for prod in catalogo:
    prod_dir = os.path.join(BASE_DIR, prod["id"])
    os.makedirs(prod_dir, exist_ok=True)
    print(f"[RANGO A - ARQUITECTO] Forjando producto: {prod['nombre']}...")
    
    # 1. Crear Landing Page (Directa sin Shopify)
    html_landing = f"""<!DOCTYPE html>
<html>
<head>
    <title>{prod['nombre']} | S-Prime</title>
    <style>
        body {{ background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 50px; }}
        h1 {{ color: #39ff14; }}
        .precio {{ font-size: 2rem; color: #ff003c; }}
        .btn {{ background: #39ff14; color: #000; padding: 15px 30px; font-size: 1.2rem; font-weight: bold; text-decoration: none; border-radius: 5px; display: inline-block; margin-top: 20px; }}
    </style>
</head>
<body>
    <h1>{prod['nombre']}</h1>
    <p>{prod['desc']}</p>
    <p>Precio Oficial Shopify: <s>${prod['precio_shopify']}</s></p>
    <p class="precio">Precio S-Prime B2B: ${prod['precio_landing']} USD</p>
    <a href="#" class="btn">Comprar Licencia B2B</a>
</body>
</html>"""
    with open(os.path.join(prod_dir, "landing.html"), "w") as f:
        f.write(html_landing)

    # 2. Crear Instrucciones y Prompts para YouTube/Redes (Para Canva/DALL-E)
    instrucciones = f"""# ESTRATEGIA DE CONTENIDO: {prod['nombre']}

## Prompt para DALL-E 3 (Miniaturas de YouTube):
"Genera una miniatura de YouTube en formato 16:9, calidad 8K, estilo hyper-realista corporativo oscuro. Fondo: {prod['nombre']}. Colores predominantes: Negro, verde neón (#39ff14) y rojo carmesí. Que tenga un aire de tecnología avanzada y negocio escalable."

## Instrucciones para Creación de Video (Canva Pro / Google):
{prod['prompts_video']}

## Operativa de Venta (Shopify vs Landing):
El tráfico que venga de los videos de YouTube DEBE dirigirse al link de la Landing local (precio: ${prod['precio_landing']}) para evadir las comisiones de Shopify.
"""
    with open(os.path.join(prod_dir, "estrategia_video_prompts.md"), "w") as f:
        f.write(instrucciones)

    # Simulación de subida a Shopify a través de API
    print(f"[RANGO S - ORQUESTADOR] Analizando variables de entorno para enviar {prod['nombre']} a Shopify Store...")
    time.sleep(1) # Simulación de carga
    print(f"➜ Paquetes locales construidos. Esperando credenciales en archivo .env para PUSH a la nube.\n")

print("=== BUCLE DE ESTRUCTURA FINALIZADO. REVISAR HUB DEL DIRECTOR ===")
