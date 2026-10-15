from fpdf import FPDF
import os

class SPrimePDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(255, 69, 0) # Naranja Kinetic
        self.cell(0, 10, 'S-PRIME KINETIC CORP', 0, 1, 'C')
        self.set_font('Arial', 'B', 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, 'MODULO EXTRA: DIGITALIZACION CERO COSTOS', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, 'Gremio de las Sombras | S-Prime Corp', 0, 0, 'C')

# Inicializar PDF
pdf = SPrimePDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Cuerpo del texto (Tier 1 - Hábitos Gratuitos)
pdf.set_font('Arial', '', 11)
pdf.set_text_color(0, 0, 0)

texto_base = (
    "Un negocio que se maneja en una libreta de papel es un negocio destinado a estancarse "
    "o quebrar por fugas de dinero. Antes de invertir en sistemas caros, debes dominar tu "
    "operacion con las herramientas gratuitas que ya tienes en tu bolsillo:\n\n"
    "1. Google Calendar (Tu Agendador Anti-Caos):\n"
    "Nunca mas aceptes una cita de palabra. Crea un calendario exclusivo para el negocio. "
    "Cada vez que un cliente pida un servicio, registralo ahi. Si no te confirma, se borra. "
    "Tu tiempo es dinero.\n\n"
    "2. Google Sheets (Tu Cotizador e Inventario en la Nube):\n"
    "Abre una hoja de calculo en tu celular. Usa la Pestana 1 para tu Inventario (que tienes "
    "y cuanto costo) y la Pestana 2 para tu Cotizador. Acostumbrate a registrar cada peso que "
    "entra y sale.\n\n"
    "En menos de un mes, veras como tu margen de ganancia aumenta solo por tener orden."
)
pdf.multi_cell(0, 8, texto_base)
pdf.ln(15)

# EL ANZUELO (Call to Action)
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(255, 69, 0) # Resaltado
pdf.cell(0, 10, '>>> SIGUIENTE NIVEL <<<', 0, 1, 'C')
pdf.ln(5)

pdf.set_font('Arial', '', 11)
pdf.set_text_color(0, 0, 0)
texto_anzuelo = (
    "Llegara un punto donde tendras tantos clientes que llenar el Google Calendar y el "
    "Google Sheets a mano te quitara tiempo valioso y no podras cobrar anticipos automaticos.\n\n"
    "Cuando llegues a ese nivel, en S-Prime hemos desarrollado Software Tier 2 y Hardware Tier 3 "
    "(Obsidian Prime) especifico para tu industria:\n"
    "- Agendadores Anti-Fantasmas (con cobro de anticipo)\n"
    "- Cotizadores de paquetes exactos\n"
    "- Estaciones de trabajo y Smartspaces\n\n"
    "Haz clic en el enlace de nuestra tienda o envianos un WhatsApp cuando estes listo para "
    "dejar de operar como autoempleado y empezar a operar como Sistema."
)
pdf.multi_cell(0, 8, texto_anzuelo)

# Guardar archivo
ruta_salida = "Modulo_Siguiente_Nivel.pdf"
pdf.output(ruta_salida, 'F')

print("="*60)
print(f"🚀 PDF GENERADO CON ÉXITO: {ruta_salida}")
print("El anzuelo está listo para ser adjuntado a todos tus cursos Tier 1.")
print("="*60)
