# main_orquestador.py
from agentes.estratega import AgenteEstratega
from agentes.meta_explorador import MetaExplorador

def iniciar_sistema():
    print(f"{'='*50}\n🚀 SISTEMA RESTAURADO - MODO PASO A PASO\n{'='*50}")

    # PASO 1: AGENTE 0
    estratega = AgenteEstratega()
    lista = estratega.generar_dorks()
    print(f"🧠 {estratega.nombre} ha cargado tu lista de respaldo.")
    for i, d in enumerate(lista, 1): print(f"   {i}. {d}")
    input("\n>>> [PASO 1] Lista verificada. Presione ENTER para buscar...")

    # PASO 2: AGENTE A
    explorador = MetaExplorador(nombre="Agente A - Explorador")
    for dork in lista:
        explorador.descubrir_fuentes(dork)
    
    print("\n✅ PROCESO FINALIZADO CON ÉXITO")
    input(">>> Presione ENTER para cerrar la terminal...")

if __name__ == "__main__":
    iniciar_sistema()
