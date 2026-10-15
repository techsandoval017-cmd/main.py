import os
import json
import subprocess

base_dir = os.path.expanduser("~/sprime_cloud_core/entregables_ataque")
output_media = os.path.join(base_dir, "multimedia_viral")
output_ventas = os.path.join(base_dir, "archivos_para_shopify")
os.makedirs(output_media, exist_ok=True)
os.makedirs(output_ventas, exist_ok=True)

print("="*80)
print("🎙️ [S-PRIME AI] INICIANDO SÍNTESIS DE AUDIO VIRAL Y EMPAQUE RANGO S")
print("="*80)

# --- FASE 1: SÍNTESIS DE AUDIO NEURONAL PARA REELS ($0 COSTO) ---
guiones_path = os.path.join(base_dir, "guiones_viral_sprime.json")
if os.path.exists(guiones_path):
    with open(guiones_path, "r", encoding="utf-8") as f:
        guiones = json.load(f)
    
    for i, reel in enumerate(guiones, 1):
        texto_completo = f"{reel['gancho']} {reel['cuerpo']} {reel['cta']}"
        archivo_mp3 = os.path.join(output_media, f"Reel_0{i}_Audio_Viral.mp3")
        print(f"\n[+] Generando Audio Neuronal para: {reel['titulo']}...")
        # Usamos la voz masculina de México (es-MX-JorgeNeural) 100% gratis
        comando = f'edge-tts --voice "es-MX-JorgeNeural" --text "{texto_completo}" --write-media "{archivo_mp3}"'
        subprocess.run(comando, shell=True)
        print(f"  ✔ Audio guardado en: {archivo_mp3}")

# --- FASE 2: EMPAQUETADO DE ENTREGABLES PARA SHOPIFY Y VUELOS ---
print("\n[+] Ensamblando Archivos Finales de Venta (Cero Vacíos)...")
for archivo in os.listdir(base_dir):
    if archivo.endswith(".json") and archivo.startswith("SPRIME"):
        with open(os.path.join(base_dir, archivo), "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Generar un archivo HTML/Markdown real que se entregará al cliente
        contenido_entregable = f"""# {data['nombre']}
## CORPORACIÓN S-PRIME KINETIC
**Valor:** ${data['precio_mxn']} MXN
**Descripción de Licencia:** {data['descripcion']}

### INSTRUCCIONES DE ACCESO:
1. Tu licencia ha sido registrada en el VÓRTEX de S-Prime AI.
2. Para activar el bot o acceder a la guía legal, entra a la plataforma y usa el correo con el que realizaste la compra.
3. El Agente Sentinel validará tu pago y te dará acceso al código fuente o manual operativo.

*Doctrina Rango S: Soberanía Tecnológica.*
"""
        nombre_final = archivo.replace(".json", "_LICENCIA_Y_ACCESO.md")
        ruta_final = os.path.join(output_ventas, nombre_final)
        with open(ruta_final, "w", encoding="utf-8") as f:
            f.write(contenido_entregable)
        print(f"  ✔ Entregable comercial generado: {nombre_final}")

print("\n🚀 [EXITO] Audios virales y archivos de Shopify listos para el mercado.")
