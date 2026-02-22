# agentes/meta_explorador.py
import os
import pandas as pd

class MetaExplorador:
    def __init__(self, nombre="Agente A"):
        self.nombre = nombre
        self.ruta_crudo = "datos/crudo/datos_brutos.csv"
        os.makedirs("datos/crudo", exist_ok=True)

    def descubrir_fuentes(self, query):
        print(f"\n🔍 {self.nombre}: Procesando comando -> {query}")
        # Simulamos la captura para asegurar que el archivo se cree y crezca
        nuevo_lead = {"texto": f"Resultado para {query}", "fuente": "Busqueda_Activa"}
        self.guardar_datos([nuevo_lead])

    def guardar_datos(self, datos):
        df = pd.DataFrame(datos)
        df.to_csv(self.ruta_crudo, mode='a', header=not os.path.exists(self.ruta_crudo), index=False)
        
        # REPORTE DE ESCRITURA EN PANTALLA
        peso = os.path.getsize(self.ruta_crudo) / 1024
        print(f"✅ [REPORTE] Archivo actualizado: {self.ruta_crudo}")
        print(f"⚖️ Tamaño: {peso:.2f} KB")
        print("-" * 40)
