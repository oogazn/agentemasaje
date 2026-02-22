# agentes/meta_explorador.py
import os
import pandas as pd
from googlesearch import search

class MetaExplorador:
    def __init__(self):
        self.ruta_crudo = "datos/crudo/datos_brutos.csv"
        os.makedirs("datos/crudo", exist_ok=True)

    def ejecutar_busqueda(self, query, num_results=10):
        print(f"\n🔍 AGENTE A: Iniciando búsqueda activa para: {query}")
        leads_encontrados = []
        
        try:
            # Ejecuta la búsqueda real en Google (Dorks de Facebook/Instagram)
            for resultado in search(query, num_results=num_results, lang="es"):
                leads_encontrados.append({"texto": resultado, "fuente": "Google_Search_Chile"})
            
            if leads_encontrados:
                self.guardar_datos(leads_encontrados)
            else:
                print("⚠️ No se hallaron resultados nuevos en esta pasada.")
                
        except Exception as e:
            print(f"❌ Error de conexión o bloqueo: {e}")

    def guardar_datos(self, nuevos_leads):
        df_nuevo = pd.DataFrame(nuevos_leads)
        
        if os.path.exists(self.ruta_crudo):
            df_existente = pd.read_csv(self.ruta_crudo)
            df_final = pd.concat([df_existente, df_nuevo]).drop_duplicates().reset_index(drop=True)
        else:
            df_final = df_nuevo

        df_final.to_csv(self.ruta_crudo, index=False, encoding='utf-8')
        
        # --- REPORTE DE ESCRITURA OBLIGATORIO (Oscar) ---
        print("-" * 60)
        print(f"📊 REPORTE DE ESCRITURA EN PANTALLA")
        print(f"✅ Se capturaron {len(nuevos_leads)} posibles leads nuevos.")
        print(f"📁 Ubicación: {self.ruta_crudo}")
        print(f"⚖️ Tamaño del archivo: {os.path.getsize(self.ruta_crudo) / 1024:.2f} KB")
        print("-" * 60)
        input(">>> ENTER para continuar al Clasificador...")
