import random
from Modelos.Base.CartaEspecialBase import CartaEspecialBase

class Especial(CartaEspecialBase):
    
    def __init__(self, nombre, equipo, pais):
        super().__init__(nombre, equipo, pais)
        self.min_atributo = 89
        self.max_atributo = 99
        
    def generar_atributo(self):
        atributo = random.randint(89, 99)
        atributo = int(atributo + (atributo * 0.02))
        return atributo if atributo <= 99 else 99
    
    def calcular_quimica(self):
        return 100
    
    @property
    def habilidades_especiales(self):
        return self._habilidades_especiales

    
    def agregar_habilidad_especial(self, habilidad_especial):
        self._habilidades_especiales.append(habilidad_especial)