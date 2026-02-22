# agentes/mensajero.py

import google.generativeai as genai
import json

class AgenteMensajero:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("Se requiere una API Key para el Mensajero")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def redactar_propuesta(self, lead):
        prompt = f"""
        Actua como un terapeuta experto en Chile. Redacta un mensaje de WhatsApp empatico.
        CLIENTE: {lead.get('perfil_cliente')}
        PROBLEMA: {lead.get('razon_terapeutica')}
        CATEGORIA: {lead.get('categoria')}
        Usa un tono cercano y profesional. Maximo 3 parrafos cortos.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error al redactar: {e}"