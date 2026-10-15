"""
S-PRIME MONARCH QUANT // PUENTE OFICIAL A HFM (HF MARKETS) VÍA MT5
Estrategia: Detección Institucional + Trailing Stop +30 Pips
"""
import time
try:
    import MetaTrader5 as mt5
except ImportError:
    print("⚠️ MetaTrader5 no instalado en el venv. Instalar con: pip install MetaTrader5 (en entorno compatible con MT5)")
    mt5 = None

# Configuración de cuenta HFM (Sustituir con credenciales reales)
HFM_CONFIG = {
    "login": 12345678,                    # Número de cuenta MT5 de HFM
    "password": "TU_PASSWORD_HFM",        # Contraseña de trading
    "server": "HFMarketsGlobal-Demo",     # O 'HFMarketsGlobal-Live'
    "symbol": "EURUSD",
    "lot": 0.10,
    "sl_pips": 12,                        # Stop Loss inicial ajustado
    "be_trigger_pips": 15,                # Pasar a Breakeven a los 15 pips
    "trailing_step_pips": 30              # Ajustar trailing cada 30 pips
}

def conectar_hfm():
    if not mt5:
        print("[ERROR] Módulo MT5 no disponible en este sistema.")
        return False

    if not mt5.initialize():
        print(f"[ERROR] initialize() falló: {mt5.last_error()}")
        return False

    autorizado = mt5.login(HFM_CONFIG["login"], password=HFM_CONFIG["password"], server=HFM_CONFIG["server"])
    if autorizado:
        print(f"✔ CONEXIÓN ESTABLECIDA CON HFM: Cuenta {HFM_CONFIG['login']} en {HFM_CONFIG['server']}")
        return True
    else:
        print(f"[ERROR] Falló autenticación con HFM: {mt5.last_error()}")
        return False

def ejecutar_caza_institucional():
    """
    Ejemplo de lógica para enviar orden con SL ajustado y gestión dinámica:
    """
    if not conectar_hfm():
        return

    symbol = HFM_CONFIG["symbol"]
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask

    sl = price - (HFM_CONFIG["sl_pips"] * 10 * point)

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": HFM_CONFIG["lot"],
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": sl,
        "tp": 0.0,  # Sin TP fijo: dejamos correr la tendencia
        "deviation": 10,
        "magic": 777001,
        "comment": "S-Prime Monarch Institucional",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    print(f"➜ Transmitiendo orden a HFM en {price} con SL a {sl}...")
    resultado = mt5.order_send(request)
    print(f"Resultado del broker: {resultado.retcode}")

if __name__ == "__main__":
    print("=== MONARCH QUANT // S-PRIME CORP ===")
    print("Para operar en vivo con HFM, configure sus credenciales en este archivo.")
