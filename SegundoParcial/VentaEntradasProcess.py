from multiprocessing import Process, Queue, Lock
import time
import random

class Comprador(Process):
    def __init__(self, entradas, lock):
        super().__init__()
        self.__entradas = entradas
        self.__lock = lock

    def ejecutar(self):
        time.sleep(random.uniform(0.1, 0.5))
        if not self.__entradas.empty():
            entrada = self.__entradas.get()
            print(f"{self.name} compró la entrada {entrada}!")
        else:
            print(f"{self.name} intentó comprar pero ya no quedan entradas.")

if __name__ == "__main__":
    num_entradas = 10
    entradas = Queue()
    lock = Lock()

    print("Venta de entradas para Recital")

    for i in range(num_entradas):
        entradas.put(f"Entrada {i+1}")

    compradores = [Comprador(entradas, lock) for _ in range(15)]

    for comprador in compradores:
        comprador.start()