import os
import sqlite3
import time

# 1. CREACIÓN DE LA MEMORIA LOCAL PERSISTENTE (Para que los agentes consulten)
os.makedirs("sprime_academia", exist_ok=True)
conn = sqlite3.connect('sprime_academia/memoria_cursos.db')
c = conn.cursor()

# Tabla de Cursos
c.execute('''CREATE TABLE IF NOT EXISTS cursos_generados
             (id INTEGER PRIMARY KEY, titulo TEXT, nicho TEXT, objetivo_caballo_troya TEXT)''')

# Tabla de Feedback (Para aplicar los descuentos del 50%)
c.execute('''CREATE TABLE IF NOT EXISTS feedback_alumnos
             (id INTEGER PRIMARY KEY, curso_id INTEGER, calificacion INTEGER, comentario TEXT, solucion_aplicada TEXT)''')
conn.commit()

# 2. LOS PRIMEROS CURSOS CABALLO DE TROYA (Basado en el algoritmo de Udemy)
cursos_a_forjar = [
    {
        "titulo": "Master en Bases de Datos desde Cero (Práctica Visual)",
        "nicho": "Tecnología / SQL",
        "duracion_minima": "120 minutos",
        "objetivo_caballo_troya": "Vender Obsidian SaaS",
        "contenido": """# ESTRUCTURA DEL CURSO: Master en Bases de Datos
## Módulo 1: La Teoría (Rápida y Visual)
- Qué es una base de datos. (Animación holográfica).
## Módulo 2: Instalación y Práctica
- Cómo usar SQLite y MySQL. Cero código aburrido, pura interfaz visual.
## Módulo 3: El Proyecto Final (La Trampa)
- **Actividad:** Conectar una base de datos a un negocio real.
- **El Gancho:** Mostrar cómo hacerlo a mano toma 5 horas. Luego, mostrar cómo *Obsidian Prime* (Nuestro software) lo hace en 1 clic.
- **Lead Magnet:** PDF con comandos de MySQL + Código QR al descuento de S-Prime Corp.
"""
    },
    {
        "titulo": "Excel Profesional para Gestión de Negocios (Cero a Experto)",
        "nicho": "Negocios / Productividad",
        "duracion_minima": "95 minutos",
        "objetivo_caballo_troya": "Vender The Golden Blade / AutoFix Engine",
        "contenido": """# ESTRUCTURA DEL CURSO: Excel para Negocios
## Módulo 1: Fórmulas que Salvan Vidas
- Tablas dinámicas y condicionales para control de inventario.
## Módulo 2: Finanzas Básicas de Local
- Control de caja, agendamiento de citas a mano.
## Módulo 3: Automatización Extrema (Proyecto Final)
- **Actividad:** Crear un macro en Excel.
- **El Gancho:** "El Excel es bueno, pero si tu negocio crece, colapsará. Mira cómo migrar tus datos de Excel a *The Golden Blade* o *AutoFix* automáticamente".
- **Lead Magnet:** Plantilla de Excel gratis + Enlace oculto a nuestra Landing Page.
"""
    },
    {
        "titulo": "Servidores y Automatización con IA (Nivel Básico)",
        "nicho": "IA / Servidores",
        "duracion_minima": "110 minutos",
        "objetivo_caballo_troya": "Vender Servicios B2B VORTEX",
        "contenido": """# ESTRUCTURA DEL CURSO: Servidores e IA
## Módulo 1: Tu Primer Servidor Local
- Cómo montar un VPS básico y usar Localtunnel.
## Módulo 2: Conectando IAs Gratuitas
- Práctica directa: Cómo enviar un prompt a ChatGPT desde la terminal.
## Módulo 3: La Evolución a Rango S
- **El Gancho:** Mostrar cómo funciona la mente enjambre de S-Prime AI trabajando en sincronía. Invitar a los corporativos a contratar a *VORTEX 7SaaS* para que les construyamos su propio Búnker.
"""
    }
]

print("=== [S-PRIME AI] FORJANDO CABALLOS DE TROYA PARA UDEMY ===")

for curso in cursos_a_forjar:
    print(f"➜ Generando material para: {curso['titulo']}...")
    
    # Guardar en Base de Datos Local
    c.execute("INSERT INTO cursos_generados (titulo, nicho, objetivo_caballo_troya) VALUES (?, ?, ?)",
              (curso['titulo'], curso['nicho'], curso['objetivo_caballo_troya']))
    conn.commit()
    
    # Crear archivo Markdown (Listo para exportar a PDF / Guion)
    filename = curso['titulo'].replace(" ", "_").replace("/", "").lower() + ".md"
    filepath = os.path.join("sprime_academia", filename)
    
    with open(filepath, "w") as f:
        f.write(curso['contenido'])
        f.write("\n\n---\n**Nota Interna S-Prime:** Cualquier reseña menor a 4 estrellas activará el envío de cupón del 50% y la actualización del temario en la base de datos local.\n")
        
    time.sleep(1) # Simulación de renderizado

print("\n✔ Base de datos local actualizada. Guiones y estructuras generados en la carpeta 'sprime_academia'.")
print("=== [S-PRIME AI] OPERACIÓN ARISE COMPLETADA ===")

conn.close()
