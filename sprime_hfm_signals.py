import requests
import time
from datetime import datetime

def generar_senales_hfm():
    print("="*75)
    print("🎯 [S-PRIME QUANT] GENERADOR DE SEÑALES PARA HFM & METATRADER 🎯")
    print(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | San Luis Río Colorado, Sonora")
    print("="*75)
    
    url = "https://api.binance.com/api/v3/ticker/24hr"
    try:
        respuesta = requests.get(url, timeout=10)
        datos = respuesta.json()
        
        print("🔍 Analizando volatilidad para operaciones apalancadas (Bono 100%)...\n")
        
        oportunidades = []
        for moneda in datos:
            simbolo = moneda['symbol']
            # Filtramos pares que usualmente están en HFM (BTC, ETH, SOL, XRP)
            if simbolo in ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'XRPUSDT', 'ADAUSDT']:
                cambio_pct = float(moneda['priceChangePercent'])
                precio = float(moneda['lastPrice'])
                
                # Si hay movimiento mayor al 3%, es operable en scalping
                if abs(cambio_pct) > 3.0:
                    direccion = "COMPRA (LONG) 🟢" if cambio_pct > 0 else "VENTA (SHORT) 🔴"
                    # Cálculo de Stop Loss ajustado (1.5%) y Take Profit abierto (4.5%) - Ratio 1:3
                    if cambio_pct > 0:
                        sl = precio * 0.985
                        tp = precio * 1.045
                    else:
                        sl = precio * 1.015
                        tp = precio * 0.955
                        
                    oportunidades.append({
                        "par": simbolo.replace('USDT', 'USD'), # Formato HFM
                        "dir": direccion,
                        "entrada": precio,
                        "sl": sl,
                        "tp": tp
                    })
        
        if oportunidades:
            print("🚀 SEÑALES LISTAS PARA COPIAR EN HFM (APP MÓVIL):")
            for op in oportunidades:
                print(f"• PAR: {op['par']}")
                print(f"• ACCIÓN: {op['dir']}")
                print(f"• ENTRADA: {op['entrada']:.4f}")
                print(f"• STOP LOSS (¡Cortar pérdidas!): {op['sl']:.4f}")
                print(f"• TAKE PROFIT (¡Dejar correr!): {op['tp']:.4f}")
                print("-" * 50)
            
            print("\n📲 COPIA ESTO EN TU CANAL DE TELEGRAM Y USA TU LINK DE REFERIDO.")
        else:
            print("⏳ El mercado está consolidando. No hay operaciones de alta probabilidad ahora. Protege tu capital de $20.")
            
    except Exception as e:
        print(f"⚠️ Error de red: {e}")

if __name__ == "__main__":
    generar_senales_hfm()
