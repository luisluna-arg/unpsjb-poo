import random
from Modelos.Tipos import Tipos
from Modelos.Pokemon import Pokemon

class Fuego(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre, Tipos.FUEGO, Tipos.AGUA)

    def defender(self, danio):
        super().defender(danio)
        self._vida = (danio - self._defensa)
        
        self._validar_vida()

    def atacar(self, oponente):
        super().atacar(oponente)
        if (oponente.debilidad == self._tipo and random.random() <= 0.4):
            oponente.defender(self._ataque * 1.3)
        else:
            oponente.defender(self._ataque)

# Ataque: Si ataca a un Pokémon débil a este tipo 
#     (por ejemplo, un Pokémon de tipo Hierba), 
#     hay un 40% de probabilidad de realizar un ataque crítico, 
#     lo que aumentará el ataque normal en un 30%.
# Defensa: Podrá defenderse de los ataques de cualquier tipo.