
from Comprador import Comprador
from SistemaVentaEntradas import SistemaVentaEntradas

TIME_FORMAT = '%H:%M:%S.%f'
CANTIDAD_COMPRADORES = 17
CANTIDAD_ENTRADAS = 12

# Este if es importante dado que en windows si no hacemos este check, 
# cada vez que se crea un proceso se ejecuta toda la solucion otra vez, incluido el main
# Lo cual genera procesos recursivamente sin fin
# En linux esto no pasa por la diferencia en el funcionamiento de los SO
# Cuando ejecutamos la aplicacion con python Main.py, 
# python le asigna el nombre __main__ al proceso principal, para que se ejecuta una única vez
if __name__ == '__main__':

    booking_system = SistemaVentaEntradas(CANTIDAD_ENTRADAS)

    compradores = []

    for user_id in range(1, CANTIDAD_COMPRADORES + 1):
        comprador = Comprador(user_id, booking_system)
        compradores.append(comprador)
        comprador.start()

    # Esperamos que terminen de comprar todos los usuarios
    for comprador in compradores:
        comprador.join()