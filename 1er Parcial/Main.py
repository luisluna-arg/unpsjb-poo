import random
from Modelos.Tipos import Tipos
from Modelos.Fuego import Fuego
from Modelos.Agua import Agua
from Modelos.Hierba import Hierba
from Modelos.Entrenador import Entrenador

cant_pokemon = 11

intentos = 10

tipos = [Tipos.AGUA, Tipos.FUEGO, Tipos.HIERBA]
pokemon_salvajes = []
for i in range(cant_pokemon):
    tipo = tipos[random.randint(0, len(tipos) - 1)]    
    nombre = f"{tipo} {i + 1}"
    if (tipo == Tipos.AGUA):
        pokemon_salvajes.append(Agua(nombre)) 
    elif (tipo == Tipos.FUEGO):
        pokemon_salvajes.append(Fuego(nombre)) 
    elif (tipo == Tipos.HIERBA):
        pokemon_salvajes.append(Hierba(nombre)) 
    
random.shuffle(pokemon_salvajes)
    
entrenador = Entrenador("El Ash", pokemon_salvajes.pop())

for i in range(10):
    indice = random.randint(0, len(pokemon_salvajes) - 1)
    pokemon = pokemon_salvajes.pop(indice)
    if (not(entrenador.atrapar(pokemon))):
        pokemon_salvajes.append(pokemon)
        
entrenador.imprimir()