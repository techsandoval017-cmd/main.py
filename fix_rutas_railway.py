import os

archivo_backend = "backend/main.py"

if os.path.exists(archivo_backend):
    with open(archivo_backend, "r") as f:
        codigo = f.read()
    
    # Inyectar StaticFiles si no existe
    if "StaticFiles" not in codigo:
        lineas = codigo.split("\n")
        insert_idx = 0
        for i, linea in enumerate(lineas):
            if "from fastapi import" in linea:
                insert_idx = i + 1
                break
        
        if insert_idx > 0:
            lineas.insert(insert_idx, "from fastapi.staticfiles import StaticFiles")
            lineas.insert(insert_idx + 1, "import os")
            
            codigo_nuevo = "\n".join(lineas)
            
            # Montar la carpeta protegiendo que exista en el contenedor
            codigo_nuevo += "\n\n# Montaje de Ecosistema Tier 2 (Railway)\n"
            codigo_nuevo += "if os.path.exists('entregables_reales'):\n"
            codigo_nuevo += "    app.mount('/tier2', StaticFiles(directory='entregables_reales', html=True), name='tier2')\n"
            
            with open(archivo_backend, "w") as f:
                f.write(codigo_nuevo)
            print("✅ Inyección exitosa en el servidor de producción (backend/main.py).")
        else:
            print("⚠️ No se encontró la importación de FastAPI en backend/main.py")
else:
    print("⚠️ El archivo backend/main.py no existe en esta ruta.")
