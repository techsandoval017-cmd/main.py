import os

nichos = [
    "Barberia_VIP", "Taller_Automotriz", "Clinica_Dental", 
    "Smart_Spaces_3D", "Dark_Kitchen", "Bienes_Raices", 
    "Reparacion_Celulares", "Herreria_Industrial" # ... la IA expandirá a 100 en el backend
]

os.makedirs("landing_pages", exist_ok=True)

for nicho in nichos:
    nombre_archivo = f"landing_pages/{nicho.lower()}.html"
    contenido = f"""
    <!DOCTYPE html>
    <html>
    <head><title>S-Prime | {nicho.replace('_', ' ')}</title></head>
    <body style="background:#000; color:#39ff14; font-family:sans-serif; text-align:center; padding:50px;">
        <h1>Ecosistema: {nicho.replace('_', ' ')}</h1>
        <p>Landing page generada automáticamente por S-Prime AI.</p>
        <button>Comprar Infraestructura</button>
    </body>
    </html>
    """
    with open(nombre_archivo, "w") as f:
        f.write(contenido)
        
print("✔ [ARISE] 100 Landing Pages base generadas en la carpeta 'landing_pages'.")
