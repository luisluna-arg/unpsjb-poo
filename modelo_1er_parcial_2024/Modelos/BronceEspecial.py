import random
from Modelos.Base.CartaEspecialBase import CartaEspecialBase


class BronceEspecial(CartaEspecialBase):

    def __init__(self, nombre, equipo, pais):
        super().__init__(nombre, equipo, pais)

    def generar_atributo(self):
        return random.randint(49, 65) + 2

    @property
    def habilidad_especial(self):
        return (
            self._habilidades_especiales[0]
            if len(self._habilidades_especiales) > 0
            else ""
        )

    @habilidad_especial.setter
    def habilidad_especial(self, habilidad_especial):
        self._habilidades_especiales = [habilidad_especial]
