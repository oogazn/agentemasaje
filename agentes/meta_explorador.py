# agentes/meta_explorador.py
import os
import pandas as pd
from googlesearch import search

class MetaExplorador:
    def __init__(self, nombre="Agente A - Explorador"):
        """
        Inicializa el agente con capacidad de recibir un nombre desde el orquestador.
        """
        self.nombre = nombre
        self.ruta_crudo = "datos/crudo/datos_brutos.csv"
        # Asegura que la estructura de carpetas exista
        os.makedirs("datos/crudo", exist_ok=True)

    def ejecutar_busqueda(self, query, num_results=10):
        """
        Realiza una búsqueda activa en Google usando los Dorks generados.
        """
        print(f"\n{'━'*60}")
        print(f"🔍 {self.nombre}: Buscando activamente...")
        print(f"🎯 Objetivo: {query}")
        print(f"{'━'*60}")
        
        leads_encontrados = []
        
        try:
            # Ejecuta la búsqueda real
            # Requiere: pip install googlesearch-python
            for resultado in search(query, num_results=num_results, lang="es"):
                leads_encontrados.append({
                    "texto": resultado, 
                    "fuente": "Google_Search_Chile"
                })
            
            if leads_encontrados:
                self.guardar_datos(leads_encontrados)
            else:
                print("⚠️ No se hallaron resultados nuevos en los índices de búsqueda.")
                
        except Exception as e:
            print(f"❌ Error durante la fase de exploración: {e}")

    def guardar_datos(self, nuevos_leads):
        """
        Gestiona la persistencia en CSV y genera el reporte de escritura en pantalla.
        """
        df_nuevo = pd.DataFrame(nuevos_leads)
        
        # Carga historial para evitar duplicar en el archivo crudo
        if os.path.exists(self.ruta_crudo):
            try:
                df_existente = pd.read_csv(self.ruta_crudo)
                df_final = pd.concat([df_existente, df_nuevo]).drop_duplicates().reset_index(drop=True)
            except:
                df_final = df_nuevo
        else:
            df_final = df_nuevo

        # Guarda en disco
        df_final.to_csv(self.ruta_crudo, index=False, encoding='utf-8')
        
        # --- REPORTE EN PANTALLA SOLICITADO POR OSCAR ---
        tamano_kb = os.path.getsize(self.ruta_crudo) / 1024
        
        print(f"\n📊 REPORTE DE ESCRITURA (AGENTE A)")
        print(f"✅ Registros procesados en esta tanda: {len(nuevos_leads)}")
        print(f"📁 Destino: {self.ruta_crudo}")
        print(f"⚖️ Peso actual del archivo: {tamano_kb:.2f} KB")
        print(f"{'━'*60}")
        
        # Pausa obligatoria para revisión
        input(">>> Presione ENTER para continuar con la clasificación...")

# Fin del archivo: agentes/meta_explorador.py
