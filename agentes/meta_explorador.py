# agentes/meta_explorador.py
import os
import pandas as pd
from googlesearch import search

class MetaExplorador:
    def __init__(self, nombre="Agente A - Explorador"):
        self.nombre = nombre
        self.ruta_crudo = "datos/crudo/datos_brutos.csv"
        os.makedirs("datos/crudo", exist_ok=True)

    def descubrir_fuentes(self, query): # <--- FUNCIÓN AGREGADA PARA CORREGIR ERROR
        print(f"\n🔍 {self.nombre}: Ejecutando fase de descubrimiento...")
        self.ejecutar_busqueda(query)

    def ejecutar_busqueda(self, query, num_results=10):
        print(f"🎯 Buscando activamente: {query}")
        leads_encontrados = []
        try:
            for resultado in search(query, num_results=num_results, lang="es"):
                leads_encontrados.append({"texto": resultado, "fuente": "Google_Search_Chile"})
            
            if leads_encontrados:
                self.guardar_datos(leads_encontrados)
            else:
                print("⚠️ No se hallaron resultados nuevos.")
        except Exception as e:
            print(f"❌ Error en exploración: {e}")

    def guardar_datos(self, nuevos_leads):
        df_nuevo = pd.DataFrame(nuevos_leads)
        if os.path.exists(self.ruta_crudo):
            try:
                df_existente = pd.read_csv(self.ruta_crudo)
                df_final = pd.concat([df_existente, df_nuevo]).drop_duplicates().reset_index(drop=True)
            except:
                df_final = df_nuevo
        else:
            df_final = df_nuevo

        df_final.to_csv(self.ruta_crudo, index=False, encoding='utf-8')
        
        tamano_kb = os.path.getsize(self.ruta_crudo) / 1024
        print(f"\n📊 REPORTE DE ESCRITURA (AGENTE A)")
        print(f"✅ Registros procesados: {len(nuevos_leads)}")
        print(f"📁 Destino: {self.ruta_crudo}")
        print(f"⚖️ Peso actual: {tamano_kb:.2f} KB")
        print("-" * 60)
        input(">>> Presione ENTER para continuar...")
