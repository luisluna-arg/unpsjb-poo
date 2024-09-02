from abc import ABC, abstractmethod

class Idioma(ABC):
    @abstractmethod
    def saludar(self):
        pass

    @abstractmethod
    def despedirse(self):
        pass

    @abstractmethod
    def perdon(self):
        pass

    @abstractmethod
    def pedirCafe(self):
        pass

    @abstractmethod
    def cuantoCuesta(self):
        pass

    @abstractmethod
    def dondeQueda(self):
        pass
