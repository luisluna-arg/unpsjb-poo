from utils.faker import Faker

class Persona:

    def __init__(self):
        self.nombre = Faker.get_nombre()
        self.apellido = Faker.get_apellido()
