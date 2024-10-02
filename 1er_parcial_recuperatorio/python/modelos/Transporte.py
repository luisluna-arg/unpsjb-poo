from abc import ABC, abstractmethod

class Transporte(ABC):

    @abstractmethod
    def transportar_paquete(self, distancia, pesoPaquete):
        pass

    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def tiempo_estimado(self, distancia):
        pass

    @abstractmethod
    def costo_estimado(self, distancia):
        pass
