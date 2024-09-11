import random
from models.categoria import Categoria
from personas.docente import Docente
from personas.no_docente import NoDocente

class MainClass:
    def __init__(self):
        print("MainClass initialized")

    def run(self):
        persona_classes = [Docente, NoDocente]
        personas = []
        for _ in range(10):
            tipo_persona = random.randint(1, 2)
            if (tipo_persona is Docente):
                personas.append(tipo_persona(Categoria.get_categoria()))
            
            persona_classes[]()
        
            

if __name__ == "__main__":
    main = MainClass()
    main.run()
