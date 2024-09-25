from random import random
from Modelos.jornada import Jornada
from personas.persona import Persona

class NoDocente(Persona):

    def __init__(self):
        super().__init__()    
        self.__jornada = Jornada.get_jornada()
        self.__cantidad_horas = random.random() > self.__jornada
