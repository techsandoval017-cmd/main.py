import csv
import os

OUTPUT_CSV = "shopify_sprime_catalogo.csv"
cabeceras = ['Handle', 'Title', 'Body (HTML)', 'Vendor', 'Type', 'Tags', 'Published', 'Variant Price', 'Variant Compare At Price', 'Variant Inventory Tracker', 'Variant Inventory Qty']

# Catálogo inyectado directamente para no depender de la BD
filas_csv = [
    ["curso-reposteria", "Mini Negocio: Repostería y Dark Kitchen", "Acceso inmediato al manual operativo", "S-Prime Corp", "Curso Digital", "Educacion, Tier1", "TRUE", "299", "", "", ""],
    ["curso-impresion3d", "S-Prime 3D Forge (Modelos)", "Catálogo de modelos 3D y parámetros", "S-Prime Corp", "Curso Digital", "Educacion, Tier1", "TRUE", "349", "", "", ""],
    ["curso-mecanica", "S-Prime Kinetic: Reparación de Motos", "Manual de ajuste y diagnóstico", "S-Prime Corp", "Curso Digital", "Educacion, Tier1", "TRUE", "450", "", "", ""]
]

with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(cabeceras)
    writer.writerows(filas_csv)

print("✔ Archivo shopify_sprime_catalogo.csv generado con éxito.")
