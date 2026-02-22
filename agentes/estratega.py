# agentes/estratega.py

import pandas as pd
import numpy as np

class AgenteEstratega:
    def __init__(self):
        """
        Nombre del archivo: agentes/estratega.py
        """
        # Base de datos de coordenadas referenciales actualizada con Maipú
        self.coordenadas_comunas = {
            'providencia': (-33.4312, -70.6122),
            'las condes': (-33.4121, -70.5694),
            'santiago': (-33.4489, -70.6693),
            'ñuñoa': (-33.4541, -70.6003),
            'vitacura': (-33.4006, -70.5750),
            'la reina': (-33.4430, -70.5484),
            'lo barnechea': (-33.3545, -70.5134),
            'maipu': (-33.5111, -70.7523) # Agregada coordenada núcleo Maipú
        }

    def calcular_punto_optimo(self, ruta_csv):
        """
        Realiza un análisis de densidad por comuna incluyendo el nodo Maipú.
        """
        try:
            df = pd.read_csv(ruta_csv)
            if df.empty:
                return {"error": "No hay datos para analizar"}

            df['comuna_detectada'] = df['comuna_detectada'].str.lower().str.strip()
            resumen_comunas = df['comuna_detectada'].value_counts()

            comunas_validas = resumen_comunas.drop('desconocida', errors='ignore')
            
            if not comunas_validas.empty:
                comuna_top = comunas_validas.idxmax()
                conteo_top = comunas_validas.max()
            else:
                comuna_top = "Santiago (General)"
                conteo_top = len(df)

            latitudes, longitudes, pesos = [], [], []
            for comuna, count in resumen_comunas.items():
                if comuna in self.coordenadas_comunas:
                    lat, lon = self.coordenadas_comunas[comuna]
                    latitudes.append(lat)
                    longitudes.append(lon)
                    pesos.append(count)

            if latitudes:
                lat_avg = np.average(latitudes, weights=pesos)
                lon_avg = np.average(longitudes, weights=pesos)
            else:
                lat_avg, lon_avg = -33.4489, -70.6693 

            return {
                "comuna_sugerida": comuna_top.upper(),
                "total_leads": len(df),
                "leads_en_comuna": int(conteo_top),
                "lat": round(lat_avg, 4),
                "lon": round(lon_avg, 4),
                "distribucion": resumen_comunas.to_dict()
            }
        except Exception as e:
            return {"error": str(e)}