import requests
import time
from datetime import datetime

# ==========================================
# 🛑 CONFIGURACIÓN DE TELEGRAM (Opcional)
# Si tienes tu bot, pon los datos aquí. Si no, déjalo vacío y saldrá en pantalla.
TELEGRAM_BOT_TOKEN = "" 
TELEGRAM_CHAT_ID = ""
# ==========================================

def enviar_telegram(mensaje):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=5)
    except:
        pass

def cazar_institucionales():
    print("="*60)
    print("⚡ [S-PRIME QUANT] CAZA INSTITUCIONAL HFT (TRAILING) ⚡")
    print(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    print("🔍 Escaneando Order Blocks e Ineficiencias de Volumen...\n")

    url = "https://api.binance.com/api/v3/ticker/24hr"
    try:
        respuesta = requests.get(url, timeout=10)
        datos = respuesta.json()
        
        operaciones_encontradas = False
        
        # Pares de alta liquidez para HFM / Bybit
        pares_objetivo = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'XRPUSDT', 'ADAUSDT']
        
        for moneda in datos:
            simbolo = moneda['symbol']
            if simbolo in pares_objetivo:
                cambio_pct = float(moneda['priceChangePercent'])
                precio = float(moneda['lastPrice'])
                
                # Criterio: Movimiento mayor al 3.5% = Inyección/Retiro Institucional
                if abs(cambio_pct) > 3.5:
                    operaciones_encontradas = True
                    direccion = "COMPRA (LONG) 🟢" if cambio_pct > 0 else "VENTA (SHORT) 🔴"
                    
                    # Cálculo de Zonas (Estimación rápida para Scalping)
                    if cambio_pct > 0:
                        sl = precio * 0.990 # Stop ajustado (1%)
                        be_trigger = precio * 1.005 # Breakeven rápido
                        tp_1 = precio * 1.015 # Objetivo inicial (+1.5%)
                        tp_2 = precio * 1.045 # Trailing abierto (+4.5%)
                    else:
                        sl = precio * 1.010 
                        be_trigger = precio * 0.995 
                        tp_1 = precio * 0.985 
                        tp_2 = precio * 0.955 
                    
                    msg = (
                        f"🎯 *ALERTA QUANT: {simbolo.replace('USDT', 'USD')}*\n"
                        f"• ACCIÓN: {direccion}\n"
                        f"• ENTRADA: {precio:.4f}\n"
                        f"• STOP LOSS ESTRICTO: {sl:.4f}\n"
                        f"• MOVER A BREAKEVEN EN: {be_trigger:.4f}\n"
                        f"• TAKE PROFIT 1 (Parciales): {tp_1:.4f}\n"
                        f"• TAKE PROFIT 2 (Dejar correr): {tp_2:.4f}\n"
                        f"⚠️ *Regla Rango S:* Asegura cada 30 pips. No dejes que una ganancia se vuelva pérdida."
                    )
                    
                    print(msg.replace('*', ''))
                    print("-" * 50)
                    enviar_telegram(msg)
                    
        if not operaciones_encontradas:
            msg = "⏳ Mercado lateral / Rango estrecho. Ninguna inyección institucional detectada. Preservación de capital activa."
            print(msg)
            enviar_telegram(f"⚡ *S-Prime Quant:* {msg}")

    except Exception as e:
        print(f"⚠️ Error de red o API: {e}")

if __name__ == "__main__":
    # Ejecuta el escaneo inmediatamente
    cazar_institucionales()
