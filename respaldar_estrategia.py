import sqlite3
import os

DB_PATH = "sprime_boveda_codigo/codigo_central.db"
os.makedirs("sprime_boveda_codigo", exist_ok=True)

ideas = [
    ("Estrategia 3D", "Venta de Smart Spaces (Rick, Itachi) vía impresión On-Demand. Triangulación de capital para comprar impresoras propias."),
    ("Embudo Barbería/Nichos", "Landing pages en Shopify. Si el cliente no tiene capital, se le ofrecen enlaces de 'Financiamiento Tech' (Nu, Stori) como afiliado."),
    ("Monarch Quant", "Bot de trading institucional HFM. SL corto, breakeven a +15 pips, trailing a +30 pips. Objetivo: Pagar Prueba de Fondeo automáticamente."),
    ("Academia & Software B2B", "Cursos en Udemy como gancho masivo. La verdadera ganancia es vender la 'Golden Suite' y el software con Kill-Switch (corte por falta de pago)."),
    ("S-Prime Next Gen", "Apps educativas interactivas para niños con grabación de voz de los padres. Recompensas en figuras 3D.")
]

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS vault_ideas
             (id INTEGER PRIMARY KEY, categoria TEXT, descripcion TEXT, fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

for categoria, descripcion in ideas:
    # Verificar que no se duplique
    c.execute("SELECT id FROM vault_ideas WHERE categoria = ?", (categoria,))
    if not c.fetchone():
        c.execute("INSERT INTO vault_ideas (categoria, descripcion) VALUES (?, ?)", (categoria, descripcion))

conn.commit()
conn.close()
print("✔ [ITACHI DB] TODAS LAS IDEAS ESTRATÉGICAS HAN SIDO GUARDADAS EN TU BASE DE DATOS LOCAL (SQLite).")
