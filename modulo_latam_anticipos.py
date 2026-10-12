import json
import time

MOCK_CITAS = []

def registrar_cita_con_anticipo(cliente: str, telefono: str, servicio: str, monto_total: float):
    anticipo = round(monto_total * 0.50, 2)
    folio_spei = f"TS-{int(time.time())}"
    cita = {
        "folio": folio_spei,
        "cliente": cliente,
        "telefono": telefono,
        "servicio": servicio,
        "total": monto_total,
        "anticipo_requerido": anticipo,
        "estado": "PENDIENTE_ANTICIPO",
        "mensaje_whatsapp": (
            f"Hola {cliente}! Para confirmar tu cita de {servicio}, "
            f"se requiere un anticipo de ${anticipo} MXN. "
            f"Transfiere por SPEI/Mercado Pago con concepto '{folio_spei}'."
        )
    }
    MOCK_CITAS.append(cita)
    return cita

if __name__ == "__main__":
    test = registrar_cita_con_anticipo("Carlos Gomez", "+526531234567", "Corte + Barba", 350.0)
    print("✅ MÓDULO LATAM OPERATIVO:")
    print(json.dumps(test, indent=2, ensure_ascii=False))
