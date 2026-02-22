# agentes/clasificador.py
import google.generativeai as genai
import json
import re

class AgenteClasificador:
    def __init__(self, api_key):
        """
        Nombre del archivo: agentes/clasificador.py
        """
        # Configuración estándar estable
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def validar_relevancia(self, texto):
        prompt = f"¿Este texto de CHILE busca masajes o tiene dolor? Responde SOLO JSON: {{'es_relevante': bool, 'comuna_detectada': str}}. Texto: {texto[:800]}"
        try:
            response = self.model.generate_content(prompt)
            match = re.search(r'\{.*\}', response.text, re.DOTALL)
            return json.loads(match.group()) if match else {"es_relevante": False}
        except Exception as e:
            # Captura el 404 para que no se detenga el proceso
            return {"es_relevante": False, "error": str(e)}