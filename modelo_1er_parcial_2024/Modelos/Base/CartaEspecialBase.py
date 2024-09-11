from abc import ABC, abstractmethod

from Modelos.Base.Carta import Carta

class CartaEspecialBase(Carta, ABC):

    def __init__(self, nombre, equipo, pais):
        super().__init__(nombre, equipo, pais)
        self._habilidades_especiales = []

    @abstractmethod
    def generar_atributo(self):
        pass
    
    def __str__(self):
        return (
            f"{super().__str__()}"
            f"Habilidadesespeciales: {", ".join(self._habilidades_especiales)}\n"
        )
