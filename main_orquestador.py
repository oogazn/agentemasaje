# main_orquestador.py
import os
import sys
import pandas as pd
from dotenv import load_dotenv
from agentes.meta_explorador import MetaExplorador
from agentes.explorador import AgenteExplorador
from agentes.clasificador import AgenteClasificador

load_dotenv()
API_KEY = os.getenv('KEY_1')
PATH_CRUDO = "datos/crudo/datos_brutos.csv"
PATH_PROCESADO = "datos/procesado/leads_calificados.csv"

def reporte_paso(titulo, detalle):
    print(f"\n{'━'*65}\n📊 {titulo}\n{'━'*65}\n{detalle}\n{'━'*65}")
    if input(">>> ENTER para continuar / 'exit' para salir: ").lower().strip() == 'exit': sys.exit()

def obtener_resumen(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        return f"{len(df)} registros ({os.path.getsize(path)/1024:.2f} KB)"
    return "Archivo no existe"

def iniciar():
    os.makedirs("datos/crudo", exist_ok=True)
    os.makedirs("datos/procesado", exist_ok=True)

    try:
        # FASE 0: Estrategia
        a0 = MetaExplorador(API_KEY)
        plan = a0.descubrir_fuentes()
        reporte_paso("AGENTE 0 - ESTRATEGIA DE CALIDAD", f"FUENTES: {plan['fuente_prioritaria']}\nCOMANDOS: {plan['comandos_busqueda']}")

        # FASE 1: Exploración
        a1 = AgenteExplorador()
        # Intentamos Reddit y si está vacío, el usuario puede cargar manual en el CSV crudo
        datos = a1.buscar_en_reddit(plan['terminos_pareto'])
        
        if not datos and os.path.exists(PATH_CRUDO):
            print("💡 No hay nuevos en Reddit. Cargando datos previos del archivo crudo...")
            datos = pd.read_csv(PATH_CRUDO).to_dict('records')

        if datos:
            pd.DataFrame(datos).to_csv(PATH_CRUDO, index=False)
            reporte_paso("AGENTE A - EXPLORACIÓN", f"Registros en memoria: {len(datos)}\n💾 ARCHIVO CRUDO: {obtener_resumen(PATH_CRUDO)}")
        else:
            reporte_paso("AGENTE A - EXPLORACIÓN", "AVISO: 0 datos encontrados. Agregue leads en datos/crudo/datos_brutos.csv manualmente."); return

        # FILTRO HISTORIAL
        vistos = set(pd.read_csv(PATH_PROCESADO)['texto'].astype(str).tolist()) if os.path.exists(PATH_PROCESADO) else set()
        por_procesar = [d for d in datos if str(d['texto']) not in vistos]
        reporte_paso("FILTRO HISTORIAL", f"Nuevos para procesar: {len(por_procesar)} (Saltados: {len(datos)-len(por_procesar)})")

        if not por_procesar: return

        # FASE 2: Clasificación
        cla = AgenteClasificador(API_KEY)
        calificados = []
        for i, d in enumerate(por_procesar):
            print(f"🧹 Clasificando {i+1}/{len(por_procesar)}...", end="\r")
            res = cla.validar_relevancia(d['texto'])
            if res.get('es_relevante'):
                d.update(res); calificados.append(d)

        # FASE 3: Guardado
        if calificados:
            df = pd.DataFrame(calificados)
            df.to_csv(PATH_PROCESADO, mode='a', header=not os.path.exists(PATH_PROCESADO), index=False)
            reporte_paso("AGENTE A.1 - FINALIZADO", f"Leads calificados hoy: {len(calificados)}\n💾 ARCHIVO PROCESADO: {obtener_resumen(PATH_PROCESADO)}")
        else:
            reporte_paso("AGENTE A.1 - FINALIZADO", "Ningún lead nuevo fue relevante.")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        input("\n>>> [FIN] ENTER para cerrar terminal...")

if __name__ == "__main__":
    iniciar()