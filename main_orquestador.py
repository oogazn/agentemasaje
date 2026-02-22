# main_orquestador.py
import os
from agentes.meta_explorador import MetaExplorador
# Importamos el Agente 0 (Asegúrate de tener este archivo en tu carpeta agentes)
from agentes.estratega import AgenteEstratega 

def pausa(titulo, mensaje):
    print(f"\n{'━'*60}")
    print(f"📋 REPORTE: {titulo}")
    print(f"🔹 {mensaje}")
    print(f"{'━'*60}")
    input(">>> [CONTROL] Presione ENTER para continuar...")

def iniciar_sistema():
    print(f"\n🚀 ECOSISTEMA DE AGENTES - MODO COMPLETO (Usuario: Oscar)")
    
    # --- PASO 1: AGENTE 0 (ESTRATEGIA) ---
    estratega = AgenteEstratega()
    print("\n🧠 Agente 0: Analizando mejores fuentes de Chile...")
    comandos = estratega.generar_dorks() # Genera los links de Facebook/Instagram
    
    pausa("AGENTE 0 - ESTRATEGIA DE CALIDAD", f"Fuentes seleccionadas: {comandos}")

    # --- PASO 2: AGENTE A (EXPLORACIÓN) ---
    explorador = MetaExplorador(nombre="Agente A - Explorador")
    print(f"\n🛰️ Iniciando búsqueda activa...")
    
    # El Agente A ahora usa lo que el Agente 0 decidió
    for dork in comandos:
        explorador.descubrir_fuentes(dork)
    
    pausa("AGENTE A - EXPLORACIÓN", "Fase de búsqueda terminada y datos guardados.")

    # --- PASO 3: FINALIZACIÓN ---
    print(f"\n✅ CICLO COMPLETADO EXITOSAMENTE")
    input("\n>>> [FIN] Presione ENTER para cerrar...")

if __name__ == "__main__":
    iniciar_sistema()
