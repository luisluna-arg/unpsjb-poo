import multiprocessing
from datetime import datetime

class SistemaVentaEntradas:
    def __init__(self, entradas_totales):
        self.__entradas_disponibles = multiprocessing.Value('i', entradas_totales)
        self.__lock = multiprocessing.Lock()

    def comprar_entrada(self, id_comprador):
        with self.__lock:
            if self.__entradas_disponibles.value > 0:
                self.__entradas_disponibles.value -= 1
                print(f"El comprador \"{id_comprador:02d}\" compró una entrada. Disponibles: {self.__entradas_disponibles.value} - Hora: {datetime.now().strftime('%H:%M:%S.%f')[:-3]}")
                return True
            else:
                print(f"El comprador \"{id_comprador:02d}\" intentó comprar, pero no quedaban entradas. - Hora: {datetime.now().strftime('%H:%M:%S.%f')[:-3]}")
                return False