import os
import time
import psutil
from crewai import Agent, Crew, Process, Task, LLM

# Verificación estricta de variables de entorno para evitar fallas en runtime
def verify_environment():
    """Valida que todas las variables de entorno necesarias estén configuradas"""
    required_vars = ['GEMINI_API_KEY']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"⚠️ Variables de entorno faltantes: {', '.join(missing_vars)}")
        print("✅ Por favor, configura estas variables en tu .env")
        return False
    
    print("✅ Todas las variables de entorno están configuradas")
    return True

def get_system_metrics():
    """Obtiene métricas del sistema para auditoría de rendimiento"""
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    metrics = {
        'cpu_usage': f"{cpu_percent}%",
        'memory_used': f"{memory.percent}%",
        'disk_used': f"{disk.percent}%",
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return metrics

def initialize_agents():
    """Inicializa los agentes especializados para la orquestación B2B"""
    
    # Agente 1: Analista de Productos
    product_analyst = Agent(
        role="Analista de Productos B2B",
        goal="Analizar y expandir catálogos de productos para e-commerce y fintech",
        backstory="Experto en estrategia de productos con 10 años en SaaS B2B",
        verbose=True
    )
    
    # Agente 2: Estratega de Monetización
    monetization_strategist = Agent(
        role="Estratega de Monetización",
        goal="Diseñar planes de monetización y estructura de cursos vendibles",
        backstory="Consultor de ingresos recurrentes y modelos de negocio escalables",
        verbose=True
    )
    
    # Agente 3: Arquitecto de Infraestructura
    infrastructure_architect = Agent(
        role="Arquitecto de Infraestructura",
        goal="Diseñar arquitectura modular B2B con 4 módulos de monetización",
        backstory="Ingeniero de sistemas con experiencia en arquitecturas empresariales",
        verbose=True
    )
    
    return [product_analyst, monetization_strategist, infrastructure_architect]

def create_tasks(agents):
    """Define las tareas que ejecutarán los agentes"""
    
    task1 = Task(
        description="Expandir y validar catálogo de productos para plataforma B2B",
        agent=agents[0],
        expected_output="Catálogo completo con 50+ productos estratificados"
    )
    
    task2 = Task(
        description="Diseñar estructura de cursos y planes de monetización",
        agent=agents[1],
        expected_output="Plan de monetización con 5 niveles de precios"
    )
    
    task3 = Task(
        description="Crear arquitectura de 4 módulos: Core, Premium, Enterprise, Consulting",
        agent=agents[2],
        expected_output="Documento de arquitectura con diagramas de integración"
    )
    
    return [task1, task2, task3]

def execute_crew(agents, tasks):
    """Ejecuta la orquestación de agentes con supervisión de rendimiento"""
    
    print("\n" + "="*60)
    print("🚀 INICIANDO FÁBRICA DE AGENTES IA - ORQUESTADOR B2B")
    print("="*60 + "\n")
    
    # Métricas iniciales
    metrics_start = get_system_metrics()
    print(f"📊 Métricas de inicio:")
    for key, value in metrics_start.items():
        print(f"   • {key}: {value}")
    
    start_time = time.time()
    
    try:
        # Crear y ejecutar crew
        crew = Crew(
            agents=agents,
            tasks=tasks,
            process=Process.hierarchical,
            manager_llm=LLM(
                model="gemini-pro",
                api_key=os.getenv('GEMINI_API_KEY')
            ),
            verbose=True
        )
        
        print("\n⚙️  Ejecutando orquestación de agentes...\n")
        result = crew.kickoff()
        
        # Métricas finales
        elapsed_time = time.time() - start_time
        metrics_end = get_system_metrics()
        
        print("\n" + "="*60)
        print("✅ EJECUCIÓN COMPLETADA")
        print("="*60)
        print(f"⏱️  Tiempo total: {elapsed_time:.2f} segundos")
        print(f"📊 Métricas finales:")
        for key, value in metrics_end.items():
            print(f"   • {key}: {value}")
        
        # Generar reporte
        generate_performance_report(metrics_start, metrics_end, elapsed_time, result)
        
        return result
        
    except Exception as e:
        print(f"\n❌ Error en la ejecución: {str(e)}")
        print("Verifica tu GEMINI_API_KEY en el archivo .env")
        return None

def generate_performance_report(metrics_start, metrics_end, elapsed_time, result):
    """Genera reporte de rendimiento en formato markdown y JSON"""
    
    report = f"""
# Reporte de Ejecución - Fábrica de Agentes IA

## Métricas de Rendimiento
- **Tiempo total de ejecución**: {elapsed_time:.2f} segundos
- **CPU (inicio)**: {metrics_start['cpu_usage']} → {metrics_end['cpu_usage']}
- **Memoria (inicio)**: {metrics_start['memory_used']} → {metrics_end['memory_used']}
- **Disco**: {metrics_end['disk_used']}
- **Timestamp**: {metrics_end['timestamp']}

## Estado
✅ Orquestación completada correctamente

## Resultado de Agentes
{result if result else "Pendiente de procesamiento"}
"""
    
    # Guardar reporte
    with open('performance_report.md', 'w') as f:
        f.write(report)
    
    print(f"\n📄 Reporte guardado en: performance_report.md")

def main():
    """Función principal de ejecución"""
    
    # Cargar variables de entorno desde .env
    from dotenv import load_dotenv
    load_dotenv()
    
    # Verificar entorno
    if not verify_environment():
        print("\n⚠️ No se puede continuar sin las variables de entorno requeridas")
        return
    
    # Inicializar agentes
    print("\n🤖 Inicializando agentes especializados...")
    agents = initialize_agents()
    print(f"✅ {len(agents)} agentes cargados\n")
    
    # Crear tareas
    print("📋 Definiendo tareas de orquestación...")
    tasks = create_tasks(agents)
    print(f"✅ {len(tasks)} tareas definidas\n")
    
    # Ejecutar crew
    result = execute_crew(agents, tasks)
    
    print("\n" + "="*60)
    print("🎉 ¡Fábrica de Agentes finalizada!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
