import multiprocessing
import time
import random
from datetime import datetime

class Comprador(multiprocessing.Process):

    def __init__(self, id_comprador, booking_system):
        super().__init__()
        self.__id_comprador = id_comprador
        self.__sistema_venta_entradas = booking_system
    
    def run(self):
        delay = random.uniform(1, 3)
        print(f"El comprador \"{self.__id_comprador:02d}\" llega a ventanilla. (Delay: {delay:.2f} segundos) - Hora: {datetime.now().strftime('%H:%M:%S.%f')[:-3]}")

        time.sleep(delay) # Simulamos un tiempo de trabajo

        # Attempt to book a ticket
        self.__sistema_venta_entradas.comprar_entrada(self.__id_comprador)