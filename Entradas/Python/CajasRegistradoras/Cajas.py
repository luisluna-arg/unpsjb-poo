# Clase que representa a un empleado encargado del cierre de caja
import threading


class EmpleadoCierre(threading.Thread):
    def __init__(self, nombre):
        super().__init__(name=nombre)

    def run(self):
        global cajas_abiertas
        while True:
            with lock:  # Sincronización
                if cajas_abiertas >= 0:
                    print(f"{self.name} cierra la caja registradora {cajas_abiertas}")
                    cajas_abiertas -= 1
                    time.sleep(1)  # Simula el tiempo que lleva cerrar la caja
                else:
                    break
