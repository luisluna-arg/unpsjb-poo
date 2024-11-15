import multiprocessing
import time

class Empleado(multiprocessing.Process):
    def __init__(self, nombre, contador, lock):
        super().__init__(name=nombre)
        self.__contador = contador
        self.__lock = lock

    def run(self):
        while True:
            with self.__lock:
                if self.__contador.value > 0:
                    print(f"{self.pid}: Caja {self.name} cerrada")
                    self.__contador.value -= 1
                else:
                    print(f"{self.pid}: Todas las cajas cerradas")
                    break
            time.sleep(2)
