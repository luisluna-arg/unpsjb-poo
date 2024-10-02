from modelos.Transporte import Transporte


class Furgoneta(Transporte):

    # Por último, el otro tipo de transporte es Furgoneta,
    # que puede enviar paquetes con un peso menor o igual a 100 kg,
    # tiene una velocidad promedio de 60km/h y el costo por km es de 1000 pesos.
    # El indicador de conveniencia del transporte está dado por la fórmula
    # 0.7 * tiempo +0.3* costo.
    # Tanto tiempo y costo representan lo mismo que en bicicleta.
    # Note que la fórmula de una furgoneta le da más importancia al tiempo y
    # en el caso de la bicicleta al costo.
    # Al igual que Bicicleta, en el caso de no poder transportarlo devuelve un -1.

    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__peso_max = 100  # KG
        self.__velocidad_promedio = 60  # Km/h
        self.__valor_por_km = 1000  # pesos

    def transportar_paquete(self, distancia, pesoPaquete):
        if (pesoPaquete > self.__peso_max):
            return -1

        indicador_conveniencia = 0.7 * self.tiempo_estimado() + 0.3 * \
            self.costo_estimado()

        return indicador_conveniencia

    @property
    def nombre(self):
        return self.__nombre

    def tiempo_estimado(self, distancia):
        return distancia / self.__velocidad_promedio  # Horas

    def costo_estimado(self, distancia):
        return distancia * self.__valor_por_km
