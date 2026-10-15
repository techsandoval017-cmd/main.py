import os, json, time

print("="*80)
print("👁️🔥 [ARISE] DESPERTANDO EJÉRCITO DE AGENTES: DIVISIÓN MEGA-NICHOS 🔥👁️")
print("="*80)
time.sleep(1)

ecosistemas = [
    {
        "nicho": "Clínicas y Odontólogos",
        "producto": "S-Prime HealthCore",
        "precio_usd": 499,
        "incluye": "Agenda WhatsApp IA, Recordatorios anti-ausencias, Expediente Digital Cifrado.",
        "ahorro_cliente": "Ahorra $3,000 USD en agencias y secretarias."
    },
    {
        "nicho": "Logística y Flotillas (Motos/Repartidores)",
        "producto": "S-Prime Fleet Radar",
        "precio_usd": 699,
        "incluye": "Rastreo por Telegram, Asignación de rutas automáticas, Bot de check-in para choferes.",
        "ahorro_cliente": "Sustituye sistemas de rastreo caros y despachadores humanos."
    },
    {
        "nicho": "Bienes Raíces / Inmobiliarias",
        "producto": "S-Prime RealEstate AI",
        "precio_usd": 599,
        "incluye": "Tour virtual automatizado, Bot calificador de créditos, CRM en Notion conectado a WhatsApp.",
        "ahorro_cliente": "Ahorra meses de sueldo en asesores filtrando clientes curiosos."
    },
    {
        "nicho": "Talleres Automotrices VIP",
        "producto": "S-Prime AutoFix Engine",
        "precio_usd": 450,
        "incluye": "Sistema OBD2 integrado, Órdenes de trabajo digitales, Actualización de estado del coche al cliente por WhatsApp.",
        "ahorro_cliente": "Moderniza el taller, justifica precios altos y elimina reclamos."
    },
    {
        "nicho": "Restaurantes & Dark Kitchens",
        "producto": "S-Prime Kitchen Sync",
        "precio_usd": 399,
        "incluye": "Menú QR dinámico, Comandas directas a la cocina sin mesero, Control de inventario en tiempo real.",
        "ahorro_cliente": "Elimina errores de meseros y plataformas que cobran 30% de comisión (UberEats)."
    }
]

dir_nichos = "ecosistemas_high_ticket"
os.makedirs(dir_nichos, exist_ok=True)

for eco in ecosistemas:
    nombre_archivo = f"{eco['nicho'].replace(' ', '_').replace('/', '')}.json"
    ruta = os.path.join(dir_nichos, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(eco, f, indent=4, ensure_ascii=False)
    print(f"🪖 Agente asignado a {eco['nicho']} ➔ Ecosistema [ {eco['producto']} ] forjado.")
    time.sleep(0.5)

print("\n🚀 [RANGO S TOTAL] Los 5 Ecosistemas han sido estructurados.")
print("La Academia entrenará a los alumnos regionales para instalar estos sistemas. Tú cobras, ellos operan.")
