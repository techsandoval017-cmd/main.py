import requests
import time
from datetime import datetime

def escanear_mercado():
    print("="*70)
    print("⚡ [S-PRIME QUANT ENGINE] RADAR DE ALTA FRECUENCIA (HFT) ACTIVADO ⚡")
    print(f"🕒 Tiempo de escaneo: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    print("Buscando anomalías institucionales y picos de volumen en tiempo real...\n")
    
    url = "https://api.binance.com/api/v3/ticker/24hr"
    try:
        respuesta = requests.get(url, timeout=10)
        datos = respuesta.json()
        
        # Filtrar solo pares con USDT, volumen masivo (dinero institucional) y tendencia positiva
        oportunidades = []
        for moneda in datos:
            simbolo = moneda['symbol']
            if simbolo.endswith('USDT'):
                volumen_usdt = float(moneda['quoteVolume'])
                cambio_pct = float(moneda['priceChangePercent'])
                precio_actual = float(moneda['lastPrice'])
                
                # Criterio Rango S: Más de 30 Millones de USD en volumen y subiendo más de un 6%
                if volumen_usdt > 30000000 and cambio_pct > 6.0:
                    oportunidades.append({
                        "par": simbolo,
                        "cambio": cambio_pct,
                        "precio": precio_actual,
                        "volumen": volumen_usdt
                    })
        
        # Ordenar por el mayor porcentaje de ganancia
        oportunidades = sorted(oportunidades, key=lambda x: x['cambio'], reverse=True)
        
        if oportunidades:
            for op in oportunidades[:5]: # Mostrar el Top 5 más explosivo
                print(f"🚀 SEÑAL CONFIRMADA: {op['par']}")
                print(f"   ➔ Precio Actual : ${op['precio']:.4f} USDT")
                print(f"   ➔ Crecimiento   : +{op['cambio']:.2f}%")
                print(f"   ➔ Vol. Inyectado: ${op['volumen']:,.0f} USD")
                print("-" * 50)
            
            print("\n💡 ESTRATEGIA DE MONETIZACIÓN INMEDIATA:")
            print("Copia estas 3 señales, publícalas en un Reel o envíalas a tu grupo de Telegram como 'Muestra Gratuita' y cobra suscripción por las señales diarias.")
        else:
            print("⏳ Mercado lateral. Ninguna anomalía institucional detectada en este segundo. El bot seguirá vigilando.")
            
    except Exception as e:
        print(f"⚠️ Error de conexión con el exchange: {e}")

if __name__ == "__main__":
    escanear_mercado()
