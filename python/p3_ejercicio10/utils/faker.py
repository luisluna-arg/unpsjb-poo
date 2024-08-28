from random import random


class Faker:
    
    NOMBRES = [
        "Juan",
        "María",
        "Carlos",
        "Ana",
        "José",
        "Laura",
        "Luis",
        "Carmen",
        "Miguel",
        "Sofía"
    ]
    
    APELLIDOS = [
        "García",
        "Rodríguez",
        "López",
        "Pérez",
        "Martínez",
        "Sánchez",
        "Fernández",
        "González",
        "Gómez",
        "Hernández"
    ]
    
    @classmethod
    def get_nombre(cls):
        random.randInt(1, len(Faker.NOMBRES))
        
    @classmethod
    def get_apellido(cls):
        random.randInt(1, len(Faker.APELLIDOS))
