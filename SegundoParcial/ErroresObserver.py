from abc import ABC, abstractmethod


class Monitor(ABC):

    @abstractmethod
    def suscribir(self, dispositivo):
        pass

    @abstractmethod
    def desuscribir(self, dispositivo):
        pass

    @abstractmethod
    def notificar(self, dispositivo):
        pass


class Dispositivo(ABC):

    @abstractmethod
    def actualizar(self, agua, petroleo):
        pass


class MonitorTanque(Monitor):
    def __init__(self):
        self.__dispositivos = []
        self.__nivel_agua = 0
        self.__nivel_petroleo = 0

    def suscribir(self, dispositivo):
        self.__dispositivos.append(dispositivo)

    def desuscribir(self, dispositivo):
        self.__dispositivos.remove(dispositivo)

    def set_levels(self, agua, petroleo):
        self.__nivel_agua = agua
        self.__nivel_petroleo = petroleo
        self.notificar()

    def notificar(self):
        for observer in self.__dispositivos:
            observer.actualizar()

    def actualizar(self, petroleo, agua):
        self.set_levels(petroleo, agua)


class DesemulsificanteAutomatizado(Dispositivo):
    def __init__(self):
        self.__desemulsificante_dosis = 0

    def actualizar(self, petroleo):
        self.__desemulsificante_dosis += 5
        print(f"Dosis de desemulsificante ajustada a: {self.__desemulsificante_dosis}")


class SistemaDeAlerta(Dispositivo):

    def __init__(self, monitorTanque):
        self.__alerta_activada = False
        self.__monitorTanque = monitorTanque

    def actualizar(self):
        if self.__alerta_activada:
            print("Alerta desactivada")
            self.__alerta_activada = False
        else:
            print("Alerta activada")
            self.__alerta_activada = True
