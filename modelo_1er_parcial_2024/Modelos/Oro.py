import random
from Modelos.Base.Carta import Carta


class Oro(Carta):

    def __init__(self, nombre, equipo, pais):
        super().__init__(nombre, equipo, pais)

    def generar_atributo(self):
        atributo = random.randint(74, 90)
        return int(atributo + (atributo * 0.05))

