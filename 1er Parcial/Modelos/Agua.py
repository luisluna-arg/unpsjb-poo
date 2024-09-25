from Modelos.Tipos import Tipos
from Modelos.Pokemon import Pokemon


class Agua(Pokemon):

    def __init__(self, nombre):
        super().__init__(nombre, Tipos.AGUA, Tipos.HIERBA)

    def defender(self, danio):
        super().defender(danio)
        if (danio < 0):
            self._vida -= danio
        else:
            self._vida = (danio - self._defensa)
            
        self._validar_vida()
        
    def atacar(self, oponente):
        super().atacar(oponente)
        if oponente.debilidad == self._tipo:
            oponente.defender(self._ataque * 1.7)
        elif (oponente.tipo == self._tipo):
            oponente.defender(self._ataque * 0.5 * -1)
        else:
            oponente.defender(self._ataque)


# Ataque: Si el oponente es débil a este tipo (por ejemplo, un Pokémon de tipo Fuego), siempre se ejecutará un ataque crítico que aumenta el ataque en un 70%.
# Defensa: Si es atacado por otro Pokémon de tipo Agua, es capaz de recuperar vida, absorbiendo el 50% del daño recibido y sumándole a su vida.
