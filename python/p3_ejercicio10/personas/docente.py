from models.categoria import Categoria
from personas.persona import Persona

class Docente(Persona):

    def __init__(self):
        super().__init__()    
        self.categoria = Categoria.get_categoria()
    
