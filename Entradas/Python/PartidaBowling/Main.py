# Archivo main.py
from Jugador import Jugador

def main():
    jugador1 = Jugador("Jugador 1", 1)
    jugador2 = Jugador("Jugador 2", 2)

    jugador1.start()
    jugador2.start()

    jugador1.join()
    jugador2.join()

    print("Partida de bowling completada")

if __name__ == "__main__":
    main()
