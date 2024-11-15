import multiprocessing
from Empleado import Empleado

def main():
    cajas_abiertas = multiprocessing.Value('i', 5)
    lock = multiprocessing.Lock()

    empleados = []
    for i in range(8):
        empleados.append(Empleado(f"Empleado-{i+1}", cajas_abiertas, lock))

    for empleado in empleados:
        empleado.start()

    for empleado in empleados:
        empleado.join()

    print("Proceso de cierre completado")

if __name__ == "__main__":
    main()
