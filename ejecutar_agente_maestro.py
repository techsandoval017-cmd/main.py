import os
import json
import urllib.request
import urllib.error

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("❌ ERROR: GEMINI_API_KEY no encontrada en variables de entorno.")
    exit(1)

def invocar_agente(sistema, tarea):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": f"ROL: {sistema}\n\nORDEN: {tarea}"}]
        }]
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["candidates"][0]["content"]["parts"][0]["text"]
    except urllib.error.HTTPError as e:
        return f"Error {e.code}: {e.read().decode('utf-8')}"

print("===================================================================")
print("🔍 DIAGNÓSTICO DEL SISTEMA Y CAPACIDADES")
print("===================================================================")
print("• Motor: Python nativo (cero dependencias externas requeridas)")
print("• LLM: Gemini API activa")
print("• Entorno: Codespaces / Terminal Linux")
print("• Capacidades: Diseño de flujos, generación de lógica para bots,")
print("  estructuración de catálogos Shopify, lógica de reservas y planes de pricing.")

print("\n===================================================================")
print("🚀 ORDEN 1: BOT DE WHATSAPP + SHOPIFY (VENTA EN AUTOMÁTICO)")
print("===================================================================")
orden_ecom = """
Diseña la arquitectura operativa de un bot de WhatsApp para tienda Shopify que venda en automático.
Entrega exactamente:
1. Flujo conversacional (Captación -> Consulta catálogo -> Carrito/Checkout Link).
2. Las 3 maneras de operar:
   - Casi gratis / Bajo costo: (Stack de herramientas gratuitas/open-source).
   - Vendible / Pyme ($297 USD): (Stack balanceado listo para monetizar).
   - Premium ($597 USD): (Solución enterprise autónoma con recuperación y analítica).
3. Informe de estado y puntos críticos de mejora.
"""
reporte_ecom = invocar_agente("Eres el Agente Especialista en Automatización eCommerce B2B", orden_ecom)
print(reporte_ecom)

print("\n===================================================================")
print("🚀 ORDEN 2: BOT PARA CITAS DE BARBERÍA (RESERVAS AUTOMATIZADAS)")
print("===================================================================")
orden_barber = """
Diseña la arquitectura operativa de un bot de agendamiento y retención para una Barbería local.
Entrega exactamente:
1. Flujo de reserva (Selección de barbero, servicio, fecha/hora y recordatorio anti-ausentismo).
2. Las 3 maneras de operar:
   - Casi gratis / Bajo costo: (Google Calendar + WhatsApp Web/Evolution API).
   - Vendible / Negocio Local ($197 - $297 USD): (Cal.com/Make + Webhooks).
   - Premium ($497 USD): (Agente de voz/IA + sistema de fidelización y cobro de depósito previo).
3. Informe de estado y puntos críticos de mejora.
"""
reporte_barber = invocar_agente("Eres el Agente Especialista en Negocios Locales y Servicios", orden_barber)
print(reporte_barber)

print("\n===================================================================")
print("📋 AUDITORÍA Y MEJORAS DEL META-AGENTE CENTRAL")
print("===================================================================")
orden_mejoras = f"""
Actúa como el Supervisor Maestro de Tech Sandoval.
Revisa los reportes entregados por ambos agentes:
Reporte 1: {reporte_ecom[:500]}...
Reporte 2: {reporte_barber[:500]}...

Entrega:
1. Las 3 acciones inmediatas para comenzar a vender estos productos esta misma semana.
2. Formato de entrega del código de integración.
"""
reporte_final = invocar_agente("Supervisor Maestro Tech Sandoval", orden_mejoras)
print(reporte_final)
