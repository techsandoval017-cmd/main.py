import csv
import sqlite3
import os

DB_PATH = "sprime_boveda_codigo/codigo_central.db"
OUTPUT_CSV = "shopify_sprime_catalogo.csv"

# Conectar a la bóveda local
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

try:
    c.execute("SELECT nicho, curso, curso_precio, software, software_precio, fisico, fisico_precio FROM catalogo_ventas")
    productos = c.fetchall()
except sqlite3.OperationalError:
    print("Error: La tabla no existe aún o el catálogo está vacío.")
    productos = []

# Formato estandarizado de Shopify
cabeceras = ['Handle', 'Title', 'Body (HTML)', 'Vendor', 'Type', 'Tags', 'Published', 'Variant Price', 'Variant Compare At Price', 'Variant Inventory Tracker', 'Variant Inventory Qty']

filas_csv = []
vendor = "S-Prime Corp"

for p in productos:
    nicho, curso, p_curso, software, p_software, fisico, p_fisico = p
    
    # Formatear precios (quitar $ y MXN)
    p_curso_clean = p_curso.replace('$', '').replace(' MXN', '').replace(',', '').strip()
    p_soft_clean = p_software.split('/')[0].replace('$', '').replace(' MXN', '').replace(',', '').strip()
    p_fis_clean = p_fisico.replace('$', '').replace(' MXN', '').replace(',', '').strip()

    # 1. Producto Educativo (Tier 1)
    filas_csv.append([f"curso-{nicho}", curso, f"Acceso inmediato al manual operativo de {nicho}.", vendor, "Curso Digital", f"Educacion, {nicho}, Tier1", "TRUE", p_curso_clean, "", "", ""])
    
    # 2. Software (Tier 2)
    filas_csv.append([f"software-{nicho}", software, f"Licencia de software operativo S-Prime para {nicho}.", vendor, "SaaS", f"Software, {nicho}, Tier2", "TRUE", p_soft_clean, "", "", ""])
    
    # 3. Producto Físico (Tier 3)
    filas_csv.append([f"fisico-{nicho}", fisico, f"Equipamiento de alta precisión para {nicho}.", vendor, "Hardware", f"Hardware, {nicho}, Tier3", "TRUE", p_fis_clean, "", "shopify", "100"])

with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(cabeceras)
    writer.writerows(filas_csv)

print("="*60)
print(f"🚀 CATÁLOGO EXPORTADO: {OUTPUT_CSV}")
print("Sube este archivo directamente a tu panel de Shopify (Productos -> Importar).")
print("="*60)
