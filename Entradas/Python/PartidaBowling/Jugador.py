import multiprocessing
import time

class Jugador(multiprocessing.Process):
    _lock = multiprocessing.Lock()  # Lock compartido entre procesos
    _turno = multiprocessing.Value('i', 1)  # Turno compartido inicializado en 1

    def __init__(self, nombre, id_turno):
        super().__init__(name=nombre)
        self._id_turno = id_turno  # Identificador de turno para cada jugador

    def run(self):
        for tiro in range(1, 6):
            while True:
                with Jugador._lock:
                    if Jugador._turno.value == self._id_turno:
                        print(f"{self.pid}: {self.name} hace el tiro n° {tiro}")
                        # Cambia el turno al otro jugador
                        Jugador._turno.value = 2 if self._id_turno == 1 else 1
                        break
                time.sleep(1)  # Breve espera antes de reintentar

