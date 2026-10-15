import os
import sqlite3
import time

# ==========================================
# 1. BÓVEDA DE CÓDIGO MULTI-IA
# ==========================================
os.makedirs("sprime_boveda_codigo", exist_ok=True)
conn = sqlite3.connect('sprime_boveda_codigo/codigo_central.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS vault_codigo
             (id INTEGER PRIMARY KEY, autor_ia TEXT, lenguaje TEXT, categoria TEXT, codigo TEXT, fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()

print("=== [ITACHI / RANGO S] BÓVEDA DE CÓDIGO ESTABLECIDA ===")
print("✔ Los agentes ahora pueden almacenar el código de Claude y ChatGPT.")

# ==========================================
# 2. S-PRIME KINETIC AUTO: MANUALES MAESTROS
# ==========================================
DIR_AUTO = "productos/sprime_kinetic_auto/manuales"
os.makedirs(DIR_AUTO, exist_ok=True)

# MANUAL TOYOTA 22R
manual_22r = """# 🔳 S-PRIME KINETIC AUTO 🔳
**MANUAL DE INGENIERÍA Y RESTAURACIÓN: TOYOTA 22R (1986-1995)**

## 1. ESPECIFICACIONES DEL MOTOR
- **Bloque:** 2.4L 4-Cilindros SOHC (2 Válvulas por cilindro).
- **Alimentación:** Carburador (22R) o Inyección Electrónica (22R-E).
- **Reputación:** Indestructible, torque bajo. Ideal para conversiones y off-road.

## 2. FALLAS CRÍTICAS A RESOLVER (EL NEGOCIO)
1. **Cadena de Tiempo (Timing Chain):** Las guías de plástico originales se rompen a las 100k millas, la cadena golpea la tapa de distribución y mezcla agua con aceite.
   - *Solución S-Prime:* Instalar Kit de Cadena con Guías de Metal (Acero).
2. **Junta de Cabeza (Head Gasket):** Fuga común en el cilindro 4 por sobrecalentamiento.

## 3. HERRAMIENTAS Y MEDIDAS EXACTAS
- **Dados Métricos Obligatorios:** 10mm, 12mm, 14mm, 17mm, 19mm, 22mm (Perno del cigueñal).
- **Llave Dinamométrica (Torque Wrench):** Crucial para la cabeza del motor (Torque a 58 ft-lbs en tres pasos).
- **Pistola de Tiempo (Timing Light):** Tiempo base a 5° APMS (Antes del Punto Muerto Superior) con manguera de vacío desconectada.

## 4. LISTA DE PROVEEDORES Y COSTOS (MÁRGENES DE VENTA)
| Pieza | Proveedor Base (Costo) | Proveedor Tuning (Performance) | Precio Venta S-Prime |
| :--- | :--- | :--- | :--- |
| Kit Cadena + Guías Metal | RockAuto ($65 USD) | LCE Performance ($150 USD) | **$120 USD (Standard)** |
| Bomba de Agua (Aisin) | AutoZone/RockAuto ($40 USD) | N/A | **$75 USD** |
| Empaque Cabeza (OEM) | Agencia Toyota / Fel-Pro ($50 USD)| Cometic Gasket ($90 USD) | **$110 USD** |

**Nota de Operación:** Adquiere las piezas en RockAuto para mayor margen. Utiliza este manual como pliego de cobro para el cliente.
"""

# MANUAL TOYOTA CAMRY 1991
manual_camry = """# 🔳 S-PRIME KINETIC AUTO 🔳
**MANUAL DE INGENIERÍA Y RESTAURACIÓN: TOYOTA CAMRY 1991 (MOTOR 3S-FE 2.0L)**

## 1. ESPECIFICACIONES DEL MOTOR
- **Bloque:** 2.0L 4-Cilindros DOHC (16 Válvulas).
- **Transmisión:** Automática A140E (Controlada electrónicamente) o Manual 5 vel.
- **Tipo de Motor:** "Non-Interference" (Si la banda de tiempo se rompe, los pistones NO doblan las válvulas. Gran ventaja de venta para el cliente).

## 2. PUNTOS DE RESTAURACIÓN CRÍTICA
1. **Fugas de Aceite en Tapa de Punterías:** El empaque se tuesta y el aceite cae en las bujías, causando fallas de encendido.
2. **Distribuidor y Rotor:** Desgaste de contactos internos. Provoca tirones en aceleración.
3. **Banda de Tiempo (Timing Belt):** Mantenimiento requerido cada 60k millas.

## 3. HERRAMIENTAS Y MEDIDAS EXACTAS
- **Dados Métricos:** 10mm (Tapa punterías), 12mm, 14mm (Soportes), 21mm (Ruedas/Cigueñal).
- **Calibrador de Lainas (Feeler Gauge):** Para ajustar holgura de válvulas si es necesario.
- **Extractor de Polea (Puller):** Para sacar la polea del cigueñal al cambiar la banda.

## 4. LISTA DE PROVEEDORES Y COSTOS
| Pieza | Proveedor Base (Costo) | Precio Venta S-Prime |
| :--- | :--- | :--- |
| Kit Banda de Tiempo (Aisin/Gates) | RockAuto ($80 USD) | **$160 USD** |
| Empaque Tapa Punterías (Fel-Pro) | AutoZone / O'Reilly ($20 USD) | **$45 USD** |
| Kit Distribuidor (Tapa + Rotor) | RockAuto ($15 USD) | **$40 USD** |
| Filtro de Transmisión + Junta | RockAuto ($12 USD) | **$35 USD** |

**Directriz JDM Tuning:** Este auto es un clásico "Sleeper". Una vez restaurado el motor, venderemos al cliente rines Enkei, coilovers ajustables (BC Racing) y volante Momo, listados en nuestro catálogo S-Prime.
"""

# Escribir los archivos en disco
with open(os.path.join(DIR_AUTO, "MANUAL_TOYOTA_22R.md"), "w") as f:
    f.write(manual_22r)
with open(os.path.join(DIR_AUTO, "MANUAL_CAMRY_1991.md"), "w") as f:
    f.write(manual_camry)

print("✔ Manuales S-Prime Kinetic Auto forjados en disco local.")
print("=== [S-PRIME AI] SISTEMAS EN LÍNEA ===")
conn.close()
