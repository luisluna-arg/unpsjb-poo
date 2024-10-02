class Paquete:

    def __init__(self, peso, volumen):
        self.__peso = peso
        self.__volumen = volumen

    @property
    def peso(self):
        return self.__peso

    def calcular_peso_volumetrico(self):
        return self.__volumen / 5000

    def __str__(self):
        return (
            f"Peso: {self.__peso}\n"
            f"Volumen: {self.__volumen}\n"
            f"Peso volumétrico: {self.calcular_peso_volumetrico()}"
        )
