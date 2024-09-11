from abc import ABC, abstractmethod

class Carta(ABC):

    def __init__(self, nombre, equipo_fav, pais):
        self._nombre  = nombre
        self._equipo_favorito = equipo_fav
        self._pais = pais
        self._habilidad_especial = ""
        self._valoracion = self.generar_atributo()
        self._velocidad = self.generar_atributo()
        self._tiro = self.generar_atributo()
        self._regate = self.generar_atributo()
        self._defensa = self.generar_atributo()
        self._pase = self.generar_atributo()
        self._fisico = self.generar_atributo()
        self._plantilla = None
    
    @property
    def plantilla(self):
        return self._plantilla

    @plantilla.setter
    def plantilla(self, plantilla):
        self._plantilla = plantilla
       
    
    @abstractmethod
    def generar_atributo(self):
        pass
    
    def calcular_quimica(self):
        if (self._pais == self._plantilla.pais_favorito and self._equipo_favorito == self._plantilla.equipo_favorito):
            return 100
        
        if (self._pais == self._plantilla.pais_favorito or self._equipo_favorito == self._plantilla.equipo_favorito):
            return 80
        
        return 0

    def __str__(self):
        return (
            f"{self._nombre}\n"
            f"Tipo carta: {self.__class__.__name__}\n"
            f"Equipo: {self._equipo_favorito}\n"
            f"Pais: {self._pais}\n"
            f"Velocidad: {self._velocidad}\n"
            f"Tiro: {self._tiro}\n"
            f"Regate: {self._regate}\n"
            f"Defensa: {self._defensa}\n"
            f"Pase: {self._pase}\n"
            f"Fisico: {self._fisico}\n"
        )