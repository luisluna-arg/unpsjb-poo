from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    
    def __init__(self, nombre, tipo, debilidad):
        self._nombre = nombre
        self._vida = 100
        self._debilidad = debilidad
        
        self._ataque = self.generar_atributo()
        self._defensa = self.generar_atributo()
        self._velocidad = self.generar_atributo()
        self._salvajismo = self.generar_atributo()
        
        self._tipo = tipo
        
    @property
    def debilidad(self):
        return self._debilidad

    @property
    def nombre(self):
        return self._nombre
        
    @property
    def salvajismo(self):
        return self._salvajismo
    
    @property
    def vida(self):
        return self._vida
    
    @property
    def tipo(self):
        return self._tipo
    
    def generar_atributo(self):
        return random.randint(1, 100)    
    
    def imprimir(self):
        print(
            (
                f"nombre: {self._nombre}\n"
                f"ataque: {self._ataque}\n"
                f"defensa: {self._defensa}\n"
                f"velocidad: {self._velocidad}\n"
                f"salvajismo: {self._salvajismo}\n"
            )
        )

    def _validar_vida(self):
        if (self._vida < 0):
            self._vida = 0
        elif (self._vida > 100): 
            self._vida = 100

    @abstractmethod
    def atacar(self, oponente):
        print("\n>>> atacar")
        print("")
        print(" - atacante")
        self.imprimir()
        print("")
        print(" - oponente")
        oponente.imprimir()
    

    @abstractmethod
    def defender(self, danio):
        print("\n>>> defender")
        print("")
        print(f" - danio: {danio}")
        self.imprimir()
