import os
from fpdf import FPDF

class SPrimeManualPDF(FPDF):
    def __init__(self, titulo_manual):
        super().__init__()
        self.titulo_manual = titulo_manual

    def header(self):
        # Fondo oscuro corporativo S-Prime
        self.set_fill_color(10, 10, 10)
        self.rect(0, 0, 210, 297, 'F')
        
        # Borde superior carmesí / neón
        self.set_fill_color(255, 0, 60)
        self.rect(0, 0, 210, 3, 'F')
        
        # Cabecera
        self.set_xy(10, 8)
        self.set_font("helvetica", "B", 10)
        self.set_text_color(255, 0, 60)
        self.cell(0, 5, "S-PRIME KINETIC AUTO // DIVISIÓN DE INGENIERÍA", ln=True)
        
        self.set_x(10)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(160, 160, 160)
        self.cell(0, 4, self.titulo_manual, ln=True)
        
        self.set_draw_color(40, 40, 40)
        self.line(10, 18, 200, 18)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_draw_color(40, 40, 40)
        self.line(10, 282, 200, 282)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"DOCUMENTO TÉCNICO OFICIAL - PÁGINA {self.page_no()}/{{nb}} - S-PRIME CORP", align="C")

    def chapter_title(self, text):
        self.set_font("helvetica", "B", 14)
        self.set_text_color(255, 255, 255)
        self.cell(0, 8, text.upper(), ln=True)
        self.set_draw_color(255, 0, 60)
        self.line(self.get_x(), self.get_y(), self.get_x() + 190, self.get_y())
        self.ln(5)

    def section_title(self, text):
        self.set_font("helvetica", "B", 11)
        self.set_text_color(255, 0, 60)
        self.cell(0, 6, text, ln=True)
        self.ln(2)

    def body_text(self, text):
        self.set_font("helvetica", "", 9)
        self.set_text_color(210, 210, 210)
        self.multi_cell(0, 5, text)
        self.ln(3)

    def draw_timing_diagram(self):
        """Genera un esquema vectorial técnico directo en el PDF"""
        self.set_draw_color(0, 210, 255)
        self.set_line_width(0.6)
        
        start_y = self.get_y() + 5
        # Polea Árbol de Levas (Arriba)
        self.circle(105, start_y + 15, 12)
        # Polea Cigueñal (Abajo)
        self.circle(105, start_y + 45, 8)
        # Líneas de cadena / banda
        self.line(93, start_y + 15, 97, start_y + 45)
        self.line(117, start_y + 15, 113, start_y + 45)
        
        # Marcas de sincronización
        self.set_font("helvetica", "B", 8)
        self.set_text_color(57, 255, 20)
        self.text(120, start_y + 10, "MARCA TDC (12:00 en punto)")
        self.text(120, start_y + 45, "MARCA CIGUEÑAL (6:00 en punto)")
        
        self.set_y(start_y + 55)
        self.ln(5)

# ==========================================
# 1. FORJAR PDF: TOYOTA 22R
# ==========================================
print("➜ Forjando Manual Técnico Completo: TOYOTA 22R...")
pdf_22r = SPrimeManualPDF("MANUAL DE RESTAURACIÓN E INGENIERÍA: TOYOTA 22R (1986+)")
pdf_22r.alias_nb_pages()

# PÁGINA 1: ESPECIFICACIONES Y MOTOR
pdf_22r.add_page()
pdf_22r.chapter_title("1. Especificaciones de Planta y Despiece Crítico")
pdf_22r.body_text(
    "El motor Toyota 22R (2.4L SOHC) es reconocido por su robustez extrema, pero posee una debilidad "
    "crítica de diseño en el tren de distribución: la guía izquierda de la cadena de tiempo está hecha de plástico "
    "y se degrada tras 100,000 millas. Al fracturarse, la cadena de acero roza directamente contra la tapa de "
    "distribución de aluminio, perforando las galerías de refrigeración y mezclando agua con aceite."
)

pdf_22r.section_title("Esquema de Sincronización y Puntos de Referencia:")
pdf_22r.draw_timing_diagram()

pdf_22r.section_title("Tabla Maestra de Torques y Calibraciones:")
pdf_22r.body_text(
    "- Tornillos de Cabeza (Culata): 58 ft-lbs (Apretar en 3 fases progresivas: 20 -> 40 -> 58 ft-lbs).\n"
    "- Bancada Principal: 76 ft-lbs.\n"
    "- Bielas: 46 ft-lbs.\n"
    "- Polea de Cigueñal: 116 ft-lbs (Obligatorio dado de 19mm o 22mm según año).\n"
    "- Calibración de Válvulas (Motor Caliente): Admisión 0.008 pulg (0.20 mm) / Escape 0.012 pulg (0.30 mm).\n"
    "- Calibración de Bujías: 0.031 pulg (0.8 mm) - Uso recomendado: NGK BPR5EY."
)

# PÁGINA 2: TRANSMISIÓN Y PROVEEDORES
pdf_22r.add_page()
pdf_22r.chapter_title("2. Transmisión, Suspensión y Proveeduría")
pdf_22r.body_text(
    "Transmisión W56 / G52:\n"
    "ADVERTENCIA CRÍTICA: Nunca utilizar aceite GL-5 en estas transmisiones manuales. El paquete de aditivos "
    "de azufre/fósforo de GL-5 degrada los sincronizadores de bronce. Utilizar exclusivamente lubricante GL-4 75W-90 "
    "(Red Line MT-90 o equivalente). Capacidad de llenado: 2.6 cuartos de galón."
)

pdf_22r.section_title("Desglose Financiero y Red de Proveedores:")
pdf_22r.body_text(
    "1. Kit de Cadena de Tiempo Doble con Guías de Acero:\n"
    "   - Proveedor: LCE Performance (LC Engineering) | Costo: $179.00 USD | Venta S-Prime: $250.00 USD\n\n"
    "2. Bomba de Agua (Aisin OEM):\n"
    "   - Proveedor: RockAuto | Costo: $35.00 USD | Venta S-Prime: $70.00 USD\n\n"
    "3. Kit de Embrague Completo (Aisin CKT-011):\n"
    "   - Proveedor: RockAuto | Costo: $110.00 USD | Venta S-Prime: $190.00 USD\n\n"
    "4. Amortiguadores de Gas Pesado (Bilstein 4600/5100):\n"
    "   - Proveedor: 4 Wheel Parts / Summit Racing | Costo: $360.00 USD | Venta S-Prime: $490.00 USD"
)

out_22r = "productos/sprime_kinetic_auto/Manual_Toyota_22R_Elite.pdf"
pdf_22r.output(out_22r)
print(f"✔ PDF Generado: {out_22r}")


# ==========================================
# 2. FORJAR PDF: TOYOTA CAMRY 1991
# ==========================================
print("➜ Forjando Manual Técnico Completo: TOYOTA CAMRY 1991...")
pdf_camry = SPrimeManualPDF("MANUAL DE RESTAURACIÓN E INGENIERÍA: TOYOTA CAMRY 1991 (3S-FE 2.0L)")
pdf_camry.alias_nb_pages()

pdf_camry.add_page()
pdf_camry.chapter_title("1. Plataforma 3S-FE 2.0L DOHC y Mantenimiento")
pdf_camry.body_text(
    "El Toyota Camry 1991 equipa el motor 3S-FE de 16 válvulas. Su principal característica de ingeniería es que "
    "es un diseño 'Non-Interference': en caso de ruptura de la banda de distribución, las válvulas no impactan "
    "con la corona del pistón. El intervalo de reemplazo preventivo es de 60,000 millas."
)

pdf_camry.section_title("Esquema de Distribución y Sellos:")
pdf_camry.draw_timing_diagram()

pdf_camry.section_title("Especificaciones de Torque y Ajustes:")
pdf_camry.body_text(
    "- Tornillos de Cabeza (TTY): 36 ft-lbs base, seguido de un giro angular de 90 grados.\n"
    "- Engrane de Árbol de Levas: 43 ft-lbs.\n"
    "- Tapa de Válvulas / Punterías: 17 ft-lbs.\n"
    "- Transmisión Automática A140E: Utilizar fluido Dexron II o III. No aplicar fluidos ATF sintéticos modernos.\n"
    "- Cuidado especial: El diferencial de la A140E posee tapón de llenado independiente."
)

pdf_camry.section_title("Costos y Márgenes de Venta:")
pdf_camry.body_text(
    "1. Kit de Banda de Tiempo + Bomba de Agua + Tensores (Aisin TKT-002):\n"
    "   - Costo Proveedor: $85.00 USD | Venta S-Prime: $160.00 USD\n\n"
    "2. Empaque de Tapa de Punterías y Sellos de Bujía (Fel-Pro):\n"
    "   - Costo Proveedor: $22.00 USD | Venta S-Prime: $55.00 USD\n\n"
    "3. Set de Amortiguadores Delanteros y Traseros (KYB Excel-G):\n"
    "   - Costo Proveedor: $160.00 USD | Venta S-Prime: $300.00 USD"
)

out_camry = "productos/sprime_kinetic_auto/Manual_Camry_1991_Elite.pdf"
pdf_camry.output(out_camry)
print(f"✔ PDF Generado: {out_camry}")

print("\n=== [S-PRIME AI] COMPILACIÓN DE DOCUMENTOS COMPLETADA ===")
