import os
import time

BASE_DIR = "productos/sprime_kinetic_auto/Enciclopedia_Tecnica"

# ==========================================
# 1. TOYOTA 22R (1986+ PICKUP)
# ==========================================
DIR_22R = os.path.join(BASE_DIR, "Toyota_22R_Pickup")
os.makedirs(DIR_22R, exist_ok=True)

motor_22r = """# ⚙️ MÓDULO 1: MOTOR Y ESPECIFICACIONES (TOYOTA 22R 2.4L)
## 1.1 Datos Técnicos Generales
- **Orden de Encendido:** 1-3-4-2
- **Calibración de Bujías:** 0.031" (0.8 mm) - Usar NGK BPR5EY.
- **Capacidad de Aceite:** 5.0 Cuartos (Con filtro). Viscosidad 10W-30 o 20W-50 (climas cálidos).
- **Calibración de Válvulas (Motor Caliente):** Admisión: 0.20 mm (0.008") | Escape: 0.30 mm (0.012").

## 1.2 Especificaciones de Torque (Apriete Crítico)
*Nota: Usar siempre llave dinamométrica calibrada.*
- **Tornillos de Cabeza (Head Bolts):** 58 ft-lbs (Apretar en 3 pases en espiral: 22 -> 43 -> 58 ft-lbs).
- **Bancada Principal (Main Bearings):** 76 ft-lbs.
- **Bielas (Rod Bearings):** 46 ft-lbs.
- **Polea del Cigueñal:** 116 ft-lbs.
- **Múltiple de Admisión:** 14 ft-lbs.
- **Múltiple de Escape:** 33 ft-lbs.

## 1.3 Procedimiento Crítico: Cambio de Cadena de Tiempo
La falla mortal del 22R son las guías de plástico originales. 
**Pasos de desmontaje:**
1. Drenar refrigerante y aceite. Retirar radiador y mangueras.
2. Quitar polea del cigueñal (Dado 19mm o 22mm, usar extractor).
3. Quitar bomba de agua y bomba de aceite.
4. Retirar tapa de distribución (Timing Cover). Cuidado con el tornillo oculto bajo el engrane del distribuidor.
**Instalación:** Alinear el eslabón brillante de la cadena con el punto del engrane del árbol de levas a las 12 en punto, y el cigueñal a las 6 en punto. Instalar GUÍAS DE METAL (LCE Performance).
"""

transmision_frenos_22r = """# ⚙️ MÓDULO 2: TRANSMISIÓN, FRENOS Y SUSPENSIÓN (22R PICKUP)

## 2.1 Transmisión (Manual W56 5-Velocidades)
- **Fluido:** Aceite para engranajes GL-4 75W-90 (NUNCA usar GL-5, destruye los sincronizadores de bronce).
- **Capacidad:** 2.6 Cuartos.
- **Torque Volante Motriz (Flywheel):** 80 ft-lbs.
- **Torque Prensa de Embrague (Clutch Cover):** 14 ft-lbs.
- **Mejora Tuning:** Instalar un embrague Aisin CKT-011 y un volante motriz aligerado de LCE Performance para mayor respuesta.

## 2.2 Sistema de Frenos
- **Configuración:** Discos delanteros, tambores traseros.
- **Líquido:** DOT 3 o DOT 4.
- **Secuencia de Purgado:** Trasero Derecho -> Trasero Izquierdo -> Delantero Derecho -> Delantero Izquierdo (Siempre del más lejano al más cercano al cilindro maestro).

## 2.3 Suspensión y Dirección
- **Amortiguadores (Upgrade):** Bilstein 4600 (Uso rudo/Calle) o Bilstein 5100 (Para pickups levantadas).
- **Engrasado:** Inyectar grasa de litio en todas las rótulas y terminales de dirección cada 10,000 millas.
"""

proveedores_22r = """# ⚙️ MÓDULO 3: RED DE PROVEEDORES (TOYOTA 22R)

## 3.1 Compras Locales (AutoZone / O'Reilly / Napa)
*Úsalo solo para fluidos y empaques de emergencia.*
- Aceite, Anticongelante, Líquido de Frenos.
- Empaques básicos (Marca Fel-Pro).
- Renta de herramientas (Extractores de polea, Torquímetros).

## 3.2 Compras en Línea (RockAuto) - [Mejor Precio OEM]
*Ideal para piezas de reemplazo estándar.*
- Bomba de Agua (Marca Aisin) - Aprox $40 USD.
- Kit de Embrague (Marca Aisin) - Aprox $120 USD.
- Bujías, cables y rotores (Marca Denso o NGK).

## 3.3 Proveedores de Tuning y Performance (Especializados)
*Aquí es donde el cliente gasta el dinero fuerte.*
- **LCE Performance (LC Engineering):** Los reyes del motor 22R. 
  - Piezas a comprar: Kit de Cadena de Tiempo doble rodillo con guías de acero ($180 USD), Headers de acero inoxidable ($350 USD), Árbol de levas Pro Torquer ($160 USD).
- **Marlin Crawler:** Especialistas en transmisiones y cajas de transferencia para 4x4.
"""

with open(os.path.join(DIR_22R, "01_Motor_Especificaciones.md"), "w") as f: f.write(motor_22r)
with open(os.path.join(DIR_22R, "02_Transmision_Frenos_Suspension.md"), "w") as f: f.write(transmision_frenos_22r)
with open(os.path.join(DIR_22R, "03_Proveedores_y_Precios.md"), "w") as f: f.write(proveedores_22r)

# ==========================================
# 2. TOYOTA CAMRY 1991 (MOTOR 3S-FE 2.0L)
# ==========================================
DIR_CAMRY = os.path.join(BASE_DIR, "Toyota_Camry_1991_3SFE")
os.makedirs(DIR_CAMRY, exist_ok=True)

motor_camry = """# ⚙️ MÓDULO 1: MOTOR Y ESPECIFICACIONES (CAMRY 91 - 3S-FE 2.0L)
## 1.1 Datos Técnicos Generales
- **Configuración:** 2.0L, 4-cilindros, DOHC, 16 Válvulas.
- **Diseño de Válvulas:** "Non-Interference" (Una rotura de banda no destruye el motor).
- **Capacidad de Aceite:** 4.0 Cuartos (5W-30 o 10W-30).

## 1.2 Especificaciones de Torque
- **Tornillos de Cabeza:** 43 ft-lbs, seguido de un giro adicional de 90 grados (Uso de medidor de ángulo es obligatorio).
- **Múltiple de Admisión:** 14 ft-lbs.
- **Polea del Árbol de Levas:** 43 ft-lbs.

## 1.3 Procedimiento: Reemplazo Banda de Tiempo
1. Alinear polea del cigueñal a 0 grados TDC (Punto Muerto Superior).
2. El orificio de la polea del árbol de levas debe coincidir con la marca en la tapa de las chumaceras.
3. Cambiar siempre: Banda, Tensor, Polea loca, y Sellos (Retenes) de árbol de levas y cigueñal. Si no cambias los retenes, fugará aceite y destruirá la banda nueva.
"""
with open(os.path.join(DIR_CAMRY, "01_Motor_y_Mantenimiento.md"), "w") as f: f.write(motor_camry)

print("=== [ITACHI / RANGO S] ENCICLOPEDIA TÉCNICA GENERADA CON ÉXITO ===")
print("Revisa la carpeta 'productos/sprime_kinetic_auto/Enciclopedia_Tecnica/'")
