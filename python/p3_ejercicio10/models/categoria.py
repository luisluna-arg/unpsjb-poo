from random import random

class Categoria:

    CATEGORIAS = []

    def __init__(self, name, horas):
        self.name = name
        self.horas = horas
        
    @classmethod
    def get_categoria(cls):
        if (len(Categoria.CATEGORIAS) == 0):
            Categoria.CATEGORIAS.append(Categoria("Exclusiva", 4))
            Categoria.CATEGORIAS.append(Categoria("Semiexclusiva", 20))
            Categoria.CATEGORIAS.append(Categoria("Simple", 10)    )
            
        return Categoria.CATEGORIAS[random.randint(0, 2)]
