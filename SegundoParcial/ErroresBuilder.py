class Car:
    def __init__(self, marca, modelo, color, tipo_motor, tipo_caja_direccion):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__tipo_motor = tipo_motor
        self.__tipo_caja_direccion = tipo_caja_direccion

    def __str__(self):
        return (f"Auto {self.__marca} {self.__modelo}, "
                f"Color: {self.__color}, "
                f"Motor: {self.__tipo_motor}, "
                f"Transmisión: {self.__tipo_caja_direccion}")


class CarBuilder:
    def __init__(self, marca, model):
        # Requeridos
        self.__marca = marca
        self.__model = model
        # Opcionales con valores predeterminados
        self.__color = "Blanco"
        self.__tipo_motor = "Gasolina"
        self.__tipo_caja_direccion = "Manual"

    def set_color(self, color):
        self.__color = color
        return self

    def set_tipo_motor(self, tipo_motor):
        self.__tipo_motor = tipo_motor
        return self

    def set_tipo_caja_direccion(self, tipo_caja_direccion):
        self.__tipo_caja_direccion = tipo_caja_direccion
        return self

    def construir(self):
        return Car(self.__marca, self.__model, self.__color, self.__tipo_motor, self.__tipo_caja_direccion)


class Director:
    def __init__(self, builder):
        self.__builder = builder

    def contruir_deportivo(self):
        return (self.__builder.set_color("Rojo")
                .set_tipo_motor("V8")
                .set_tipo_caja_direccion("Automática")
                .construir())

    def construir_sedan(self):
        return (self.__builder.set_color("Azul")
                .set_tipo_motor("Híbrido")
                .set_tipo_caja_direccion("Manual")
                .construir())


# Uso del Director con el Builder
builder = CarBuilder("Toyota", "Supra")
director = Director(builder)

# Construir un auto deportivo
sports_car = director.contruir_deportivo()
print(sports_car)

# Construir un auto de ciudad
city_car = director.construir_sedan()
print(city_car)

