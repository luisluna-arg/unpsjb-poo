from modelos.Transporte import Transporte


class Furgoneta(Transporte):

    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__peso_max = 100  # KG
        self.__velocidad_promedio = 60  # Km/h
        self.__valor_por_km = 1000  # pesos

    def transportar_paquete(self, distancia, pesoPaquete):
        if (pesoPaquete > self.__peso_max):
            return -1

        indicador_conveniencia = 0.7 * self.tiempo_estimado(distancia) + 0.3 * \
            self.costo_estimado(distancia)

        return indicador_conveniencia

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def peso_max(self):
        return self.__peso_max

    def tiempo_estimado(self, distancia):
        return distancia / self.__velocidad_promedio  # Horas

    def costo_estimado(self, distancia):
        return distancia * self.__valor_por_km
