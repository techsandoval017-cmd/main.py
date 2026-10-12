import os, sys, json, time
from datetime import datetime

ROOT = "/workspaces/main.py"
DATASET_PATH = os.path.join(ROOT, "dataset_entrenamiento_ia.jsonl")
PROMPTS_FALTANTES_PATH = os.path.join(ROOT, "prompts_requerimientos_pendientes.txt")

SYSTEM_PROMPT_CORE = (
    "Eres el Meta-Agente Creador y Orquestador Supremo de Tech Sandoval Holding LLC. "
    "Tu función es diseñar, auditar, generar código en Python y publicar productos de software "
    "y micro-SaaS en Shopify mediante GraphQL, asegurando el cumplimiento legal (Nuevo México LLC) "
    "y fiscal (SAT México), optimizando el gasto de tokens al mínimo."
)

def registrar_interaccion(user_prompt: str, assistant_solution: str, etiquetas: list):
    """Guarda un registro supervisado en formato JSONL para fine-tuning."""
    entrada = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "etiquetas": etiquetas,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_CORE},
            {"role": "user", "content": user_prompt.strip()},
            {"role": "assistant", "content": assistant_solution.strip()}
        ]
    }
    with open(DATASET_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entrada, ensure_ascii=False) + "\n")
    print(f"✅ Interacción registrada en dataset para entrenamiento. Etiquetas: {etiquetas}")

def auditar_conocimiento_y_pedir_prompts():
    """Analiza qué procedimientos faltan y genera los prompts para solicitarlos."""
    areas_cubiertas = set()
    total_registros = 0

    if os.path.exists(DATASET_PATH):
        with open(DATASET_PATH, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.strip():
                    total_registros += 1
                    data = json.loads(linea)
                    areas_cubiertas.update(data.get("etiquetas", []))

    areas_necesarias = {
        "shopify_graphql": "Procedimiento de mutación productCreate y gestión de variantes de precios.",
        "sat_compliance": "Reglas de retención fiscal en México, facturación 4.0 y validación de RFC/SPEI.",
        "seguridad_owasp": "Firma HMAC de webhooks de pago y validación de tokens sin exponer secretos.",
        "stripe_pagos": "Captura y conciliación automática de suscripciones recurrentes USD.",
        "canva_bulk": "Generación de CSVs escalables para creativos masivos sin cuellos de botella."
    }

    faltantes = {k: v for k, v in areas_necesarias.items() if k not in areas_cubiertas}

    with open(PROMPTS_FALTANTES_PATH, "w", encoding="utf-8") as f:
        f.write("# TECH SANDOVAL - REQUERIMIENTOS DE INFORMACIÓN PARA ENTRENAMIENTO DE IA\n")
        f.write(f"# Generado el: {datetime.utcnow().isoformat()}Z\n")
        f.write(f"# Total de registros actuales: {total_registros}\n\n")
        
        if not faltantes:
            f.write("ESTADO: Todas las áreas fundamentales cuentan con al menos un procedimiento base.\n")
        else:
            f.write("La IA requiere que alimentes los siguientes procedimientos para completar su aprendizaje:\n\n")
            for tag, descripcion in faltantes.items():
                f.write(f"[ÁREA FALTANTE: {tag}]\n")
                f.write(f"Descripción: {descripcion}\n")
                f.write(f"PROMPT SUGERIDO PARA AGREGAR:\n")
                f.write(f"\"IA, genera y documenta el procedimiento estándar de {descripcion} para Tech Sandoval\"\n\n")

    return total_registros, faltantes

# Inicialización con los procedimientos reales ya validados en esta sesión
if __name__ == "__main__":
    # Cargar procedimientos de prueba probados hoy si el dataset no existe
    if not os.path.exists(DATASET_PATH) or os.path.getsize(DATASET_PATH) == 0:
        registrar_interaccion(
            user_prompt="¿Cómo conectar de forma segura a Shopify Admin API mediante GraphQL en Python?",
            assistant_solution="Se usa urllib.request con endpoint /admin/api/2024-10/graphql.json, pasando el header X-Shopify-Access-Token desde credenciales_maestras.env, ejecutando mutaciones tipadas y aislando la clave sin exponerla en repositorios.",
            etiquetas=["shopify_graphql", "seguridad_owasp"]
        )
        registrar_interaccion(
            user_prompt="¿Cómo sincronizar los creativos publicitarios entre la factoría y Canva sin dependencias de API de pago?",
            assistant_solution="Se estructura un dataset CSV (canva_bulk_saas_300.csv) con columnas Producto, Gancho_Viral, Subtitulo, Precio_USD y Llamado_Accion para ser consumido mediante Canva Bulk Create de manera instantánea.",
            etiquetas=["canva_bulk"]
        )
        registrar_interaccion(
            user_prompt="¿Cuál es la separación jurídica entre Nuevo México y el SAT para Tech Sandoval?",
            assistant_solution="Tech Sandoval Holding LLC (Nuevo México) cobra vía Stripe USD suscripciones de software internacional; Tech Sandoval Latam Ops gestiona transferencias SPEI y Mercado Pago para México, con emisión y conciliación de CFDI 4.0 ante el SAT.",
            etiquetas=["sat_compliance"]
        )

    registros, faltan = auditar_conocimiento_y_pedir_prompts()
    print("===================================================================")
    print("🧠 NÚCLEO DE MEMORIA & AUTOAPRENDIZAJE ACTIVADO")
    print("===================================================================")
    print(f"• Registros de Procedimientos : {registros} acumulados en dataset_entrenamiento_ia.jsonl")
    print(f"• Áreas Pendientes de Prompt  : {len(faltan)}")
    if faltan:
        print(f"• Requerimientos guardados en : {PROMPTS_FALTANTES_PATH}")
    print("===================================================================")
