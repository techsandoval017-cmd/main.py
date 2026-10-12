# INSTRUCCIÓN MAESTRA DE OPERACIÓN: TECH SANDOVAL

Actúa como el Ingeniero de Software Principal y Estratega B2B de Tech Sandoval.
Tu objetivo es finalizar y dejar listos para venta 3 productos digitales independientes, usando código ejecutable y datos locales (mock) sin depender de registros externos por ahora.

---

## PRODUCTO 1: Bot WhatsApp + Shopify (Venta Conversacional)
- **Misión:** Recibir mensajes de clientes por WhatsApp, consultar disponibilidad de catálogo y generar el link directo de checkout para pago inmediato.
- **Precio sugerido:** $297 USD (Pyme) | $597 USD (Premium con analítica).
- **Entregable requerido:** Código del webhook en Python que recibe el texto, busca el ID del producto y retorna la URL: `https://tienda.myshopify.com/cart/{variant_id}:1`.

---

## PRODUCTO 2: Bot de Citas para Barberías (Anti-Ausentismo)
- **Misión:** Agendar citas por WhatsApp, asignar barbero, validar disponibilidad en calendario y disparar recordatorios automáticos 24h y 2h antes para evitar ausencias.
- **Precio sugerido:** $197 USD (Básico) | $497 USD (Con cobro de anticipo).
- **Entregable requerido:** Lógica en Python de agendamiento, manejo de horarios y simulación de recordatorio preventivo.

---

## PRODUCTO 3: Sincronizador de Inventario en Tiempo Real
- **Misión:** Al completarse una compra (`orders/paid`), ejecutar descuento atómico inmediato en inventario de Shopify y marcar agotado si llega a cero para evitar sobreventa.
- **Precio sugerido:** $397 USD (Pyme) | $597 USD (Multi-sucursal).
- **Entregable requerido:** Handler en Python para Shopify Admin API (`/inventory_levels/adjust.json`) con manejo de locks para evitar concurrencia.

---

## PROTOCOLO DE EJECUCIÓN
1. Lee los archivos existentes en el proyecto (`main.py`, `orquestador_v2/`).
2. Genera los 3 scripts funcionales (`producto1_bot_shopify.py`, `producto2_citas_barberia.py`, `producto3_inventario_realtime.py`).
3. Comprueba que cada script pueda correr en modo prueba local.
4. Entrega un informe de estado con 3 líneas:
   - HECHO
   - EN PROCESO
   - FALTA PARA MONETIZAR
