import multiprocessing
from datetime import datetime

class SistemaVentaEntradas:
    def __init__(self, entradas_totales):
        self.__entradas_disponibles = multiprocessing.Value(entradas_totales)

    def comprar_entrada(self, id_comprador):
        if self.__entradas_disponibles > 0:
            self.__entradas_disponibles -= 1
            print(f"\"{id_comprador:02d}\" compró una entrada. Disponibles: {self.__entradas_disponibles}")
            return True
        else:
            print(f"\"{id_comprador:02d}\" intentó comprar, pero no quedaban entradas.")
            return False