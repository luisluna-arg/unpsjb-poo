import threading
import time

# Variable compartida (representa la cantidad de cajas registradoras abiertas)
cajas_abiertas = 3

# Lock para sincronización
lock = threading.Lock()


# Crear y empezar 4 hilos (empleados encargados del cierre de caja)
empleados = [EmpleadoCierre(f"Empleado-{i+1}") for i in range(4)]
for empleado in empleados:
    empleado.start()
for empleado in empleados:
    empleado.join()

print("Todas las cajas registradoras han sido cerradas")
