from modelos.Transporte import Transporte


class Bicicleta(Transporte):

    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__peso_max = 5  # KG
        self.__velocidad_promedio = 12  # Km/h
        self.__valor_por_km = 200  # pesos

    def transportar_paquete(self, distancia, pesoPaquete):
        if (pesoPaquete > self.__peso_max):
            return -1

        indicador_conveniencia = 0.2 * self.tiempo_estimado(distancia) + 0.8 * \
            self.costo_estimado(distancia)

        return indicador_conveniencia

    @property
    def nombre(self):
        return self.__nombre

    def tiempo_estimado(self, distancia):
        return distancia / self.__velocidad_promedio  # Horas

    def costo_estimado(self, distancia):
        return distancia * self.__valor_por_km
