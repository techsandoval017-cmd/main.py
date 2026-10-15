import os

archivo_main = "main.py"
if os.path.exists(archivo_main):
    with open(archivo_main, "r") as f:
        codigo = f.read()
    
    if "StaticFiles" not in codigo:
        lineas = codigo.split("\n")
        for i, linea in enumerate(lineas):
            if "from fastapi import" in linea:
                lineas.insert(i+1, "from fastapi.staticfiles import StaticFiles")
                break
        
        codigo_nuevo = "\n".join(lineas)
        # Esto hace que la carpeta sea pública bajo la ruta /tier2
        codigo_nuevo += "\n\n# Montaje de la suite publica S-Prime Tier 2\napp.mount('/tier2', StaticFiles(directory='entregables_reales', html=True), name='tier2')\n"
        
        with open(archivo_main, "w") as f:
            f.write(codigo_nuevo)
        print("✅ Rutas publicas montadas en el servidor.")
