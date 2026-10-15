import os
import requests
import time

# Toma las credenciales que YA existen en tu servidor/bóveda
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_alerta(mensaje):
    if TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": mensaje})
    else:
        print("⚠️ No se encontraron las variables en el entorno, pero el escaneo sigue activo.")

def vigia_mercado():
    print("👁️ [S-PRIME VIGÍA] Conectado al Bot de Telegram existente. Escaneando HFM...")
    while True:
        try:
            datos = requests.get("https://api.binance.com/api/v3/ticker/24hr").json()
            for moneda in datos:
                if moneda['symbol'] in ['SOLUSDT', 'BTCUSDT']:
                    if abs(float(moneda['priceChangePercent'])) > 5.0:
                        alerta = f"🚨 ALERTA S-PRIME 🚨\n{moneda['symbol']} se movió fuerte.\nPrecio: {moneda['lastPrice']}\n¡Revisa tu app de HFM!"
                        enviar_alerta(alerta)
        except Exception:
            pass
        time.sleep(900) # Revisa cada 15 minutos

if __name__ == "__main__":
    vigia_mercado()
