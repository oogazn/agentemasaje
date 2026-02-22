# main_orquestador.py
import os
import sys
from agentes.meta_explorador import MetaExplorador

def pausa_reporte(titulo, mensaje):
    """Genera un bloqueo visual en pantalla para revisión de Oscar"""
    print(f"\n{'━'*60}")
    print(f"📋 REPORTE DE PASO: {titulo}")
    print(f"🔹 ESTADO: {mensaje}")
    print(f"{'━'*60}")
    input(">>> [CONTROL] Presione ENTER para continuar al siguiente paso...")

def iniciar_sistema():
    print(f"\n🚀 ECOSISTEMA DE AGENTES - MODO PASO A PASO (Usuario: Oscar)")
    
    # --- PASO 1: INSTANCIACIÓN ---
    try:
        agente_a = MetaExplorador(nombre="Agente A - Explorador")
        pausa_reporte("INICIALIZACIÓN", "Agentes cargados y listos para operar.")
    except Exception as e:
        print(f"❌ Error al cargar agentes: {e}")
        return

    # --- PASO 2: BÚSQUEDA ---
    dork = "site:facebook.com/groups 'necesito masaje' Chile"
    print(f"\n🛰️ Solicitando búsqueda activa...")
    agente_a.descubrir_fuentes(dork)
    
    # Nota: El Agente A ya tiene su propio ENTER interno para el reporte de KB,
    # pero este refuerza el fin de la fase de búsqueda.
    pausa_reporte("FUEGO DE BÚSQUEDA", "Fase de exploración completada. Datos guardados en crudo.")

    # --- PASO 3: FINALIZACIÓN ---
    print(f"\n✅ CICLO COMPLETADO EXITOSAMENTE")
    print(f"📁 Los leads están disponibles en datos/crudo/datos_brutos.csv")
    input("\n>>> [FIN DEL PROCESO] Presione ENTER para cerrar la terminal...")

if __name__ == "__main__":
    iniciar_sistema()
