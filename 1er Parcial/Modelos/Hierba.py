import random
from Modelos.Pokemon import Pokemon
from Modelos.Tipos import Tipos


class Hierba(Pokemon):

    def __init__(self, nombre):
        super().__init__(nombre, Tipos.HIERBA, Tipos.FUEGO)

    def defender(self, danio):
        super().defender(danio)
        if self._velocidad > 50 and random.random() > 0.5:
            return # No hay daño
        
        if self._velocidad < 50:
            self._vida -= danio
        elif random.random() <= 0.5:
            danio_local = danio - self._defensa
            if danio_local < 0:
                danio_local = 0

            self._vida -= danio_local

        self._validar_vida()

    def atacar(self, oponente):
        super().atacar(oponente)
        if oponente.debilidad == self._tipo and random.random() < 0.8:
            oponente.defender(self._ataque * 1.5)
        else:
            oponente.defender(self._ataque)
