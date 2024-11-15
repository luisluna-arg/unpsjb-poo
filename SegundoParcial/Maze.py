class Laberinto:
    def __init__(self):
        self.__habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.__habitaciones.append(habitacion)

    def __str__(self):
        return f"Laberinto with {len(self.__habitaciones)} habitaciones"


class Habitacion:
    def __init__(self, numero_habitacion):
        self.__numero_habitacion = numero_habitacion
        self.__lados = {}

    def set_lado(self, direccion, pared):
        self.__lados[direccion] = pared

    def __str__(self):
        lados = ", ".join(
            [
                f"{direccion}: {type(pared).__name__}"
                for direccion, pared in self.__lados.items()
            ]
        )
        return f"Habitacion {self.__numero_habitacion} con los lados {lados}"


class Pared:
    pass


class Puerta:
    def __init__(self, habitacion1, habitacion2):
        self.__habitacion1 = habitacion1
        self.__habitacion2 = habitacion2
        self.__abierta = False

    def __str__(self):
        return f"Puerta entre la habitacion {self.__habitacion1.numero_habitacion} y la habitacion {self.__habitacion2.numero_habitacion}"


class ConstructorLaberinto:
    def __init__(self):
        self.__laberinto = Laberinto()

    def __crear_laberinto(self):
        self.__laberinto = Laberinto()

    def __construir_habitacion(self, numero_habitacion):
        habitacion = Habitacion(numero_habitacion)
        habitacion.set_lado("Norte", Pared())
        habitacion.set_lado("Sur", Pared())
        habitacion.set_lado("Este", Pared())
        habitacion.set_lado("Oeste", Pared())
        self.__laberinto.agregar_habitacion(habitacion)
        return habitacion

    def __construir_puerta(self, habitacion1, habitacion2):
        puerta = Puerta(habitacion1, habitacion2)
        habitacion1.set_lado("Este", puerta)
        habitacion2.set_lado("Oeste", puerta)

    def construir_laberinto_simple(self):
        self.__crear_laberinto()
        habitacion1 = self.__construir_habitacion(1)
        habitacion2 = self.__construir_habitacion(2)
        self.__construir_puerta(habitacion1, habitacion2)
        return self.__laberinto


class LaberintoDirector:
    def __init__(self, constructor):
        self.__constructor = constructor

    def construir_laberinto_simple(self):
        return self.__constructor.construir_laberinto_simple()
