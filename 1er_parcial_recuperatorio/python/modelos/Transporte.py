from abc import ABC, abstractmethod


class Transporte(ABC):

# En el caso de los transportes, 
# se hace uso de una abstracción que permite abstraer al paquete de las implementaciones 
# específicas. Los métodos que define son: 
# transportarPaquete(double distancia, double pesoPaquete) que devuelve un Double. 
# getNombre() que devuelve un String que es el nombre que identifica al transporte. 
# tiempoEstimado(double distancia); que devuelve un Double con el tiempo estimado de envío. 
# costoEstimado(double distancia); que devuelve un Double con el costo estimado.


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
