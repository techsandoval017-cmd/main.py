import requests, time

# Configura tu bot de Telegram aquí (cuando lo crees en BotFather)
TELEGRAM_BOT_TOKEN = "TU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = "TU_CHAT_ID_AQUI"

def enviar_alerta(mensaje):
    if TELEGRAM_BOT_TOKEN != "TU_TOKEN_AQUI":
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": mensaje})
    print(mensaje)

def vigia_mercado():
    print("👁️ [S-PRIME VIGÍA] Radar automático activado. Escaneando cada 15 min...")
    while True:
        try:
            datos = requests.get("https://api.binance.com/api/v3/ticker/24hr").json()
            for moneda in datos:
                if moneda['symbol'] in ['SOLUSDT', 'BTCUSDT', 'XRPUSDT']:
                    if abs(float(moneda['priceChangePercent'])) > 5.0:
                        alerta = f"🚨 ALERTA S-PRIME 🚨\n{moneda['symbol']} se movió un {moneda['priceChangePercent']}%. \nPrecio: {moneda['lastPrice']}\n¡Revisa tu HFM!"
                        enviar_alerta(alerta)
        except Exception:
            pass
        time.sleep(900) # Duerme 15 minutos y vuelve a buscar

if __name__ == "__main__":
    vigia_mercado()
