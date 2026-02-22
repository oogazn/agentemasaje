# agentes/meta_explorador.py
import google.generativeai as genai
import json
import re

class MetaExplorador:
    def __init__(self, api_key):
        """Nombre del archivo: agentes/meta_explorador.py"""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        self.fuentes_respaldo = ["facebook.com/groups", "instagram.com", "doctoralia.cl", "reclamos.cl"]
        self.listado_maestro = ["masaje descontracturante", "masaje relajante", "fisioterapia", "dolor lumbar", "lumbago"]

    def descubrir_fuentes(self, fuentes_previas=None):
        prompt = f"Actúa como experto SEO Chile. Fuentes: {self.fuentes_respaldo}. Elige 10 términos Pareto de mi lista y crea 3 comandos site: para Chile. Responde SOLO JSON: {{'terminos_pareto': [], 'comandos_busqueda': [], 'fuente_prioritaria': ''}}"
        try:
            response = self.model.generate_content(prompt)
            match = re.search(r'\{.*\}', response.text, re.DOTALL)
            return json.loads(match.group()) if match else self._respaldo()
        except:
            return self._respaldo()

    def _respaldo(self):
        return {"terminos_pareto": self.listado_maestro, "comandos_busqueda": [f"site:{f} Chile 'masaje'" for f in self.fuentes_respaldo[:2]], "fuente_prioritaria": "Facebook Groups Chile"}