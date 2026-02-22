# agentes/estratega.py
class AgenteEstratega:
    def __init__(self):
        self.nombre = "Agente 0 - Estratega de Calidad"

    def generar_dorks(self):
        # Restaurando tu lista original de búsqueda para Chile
        return [
            "site:facebook.com/groups 'necesito masaje' Chile",
            "site:instagram.com 'masaje descontracturante' Chile",
            "site:doctoralia.cl 'masaje' Santiago",
            "site:reclamos.cl 'masajista' Chile",
            "site:portalnet.cl 'masajes' Chile"
        ]
