from random import random

class Jornada:

    JORNADAS = []

    def __init__(self, name, horas):
        self.name = name
        self.horas = horas
        
    @classmethod
    def get_jornada(cls):
        if (len(Jornada.JORNADAS) == 0):
            Jornada.JORNADAS.append(Jornada("Completa", 30))
            Jornada.JORNADAS.append(Jornada("Reducida", 20))
        
        return Jornada.JORNADAS[random.randint(0, 1)]
