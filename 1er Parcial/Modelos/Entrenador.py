import random

class Entrenador:
    
    SEPARADOR = "========================="
    SEPARADOR_1 = "+++++++++++++++++++++++++"
    
    def __init__(self, nombre, pokemon_inicial):
        self.__nombre = nombre
        self.__nivel = random.randint(1, 100)
        self.__pokedex = [pokemon_inicial]
        
    @property
    def pokedex(self):
        return self.__pokedex

    def atrapar(self, pokemon_objetivo):
        print(f"{Entrenador.SEPARADOR}")
        print(f"Batalla\n")
        print(f"Nivel entrenador {self.__nivel} Salvajismo objetivo: {pokemon_objetivo.salvajismo}")
        if (pokemon_objetivo.salvajismo <= self.__nivel):
            for item in range(3):
                print(f"Round {item + 1}")
                pokemon = self.__pokedex[random.randint(0, len(self.__pokedex)-1)]
                pokemon.atacar(pokemon_objetivo)
                if (pokemon_objetivo.vida <= 0):
                    print(f"Pokemon perdido {pokemon_objetivo.nombre} Vida = 0")
                    return ## El pokemon se quedo sin vida
                
            if (pokemon_objetivo.vida > 0):
                self.__pokedex.append(pokemon_objetivo)
                print(f"Pokemon atrapado {pokemon_objetivo.nombre}")
                return True
        
        print(f"Pokemon perdido {pokemon_objetivo.nombre}")
        
        print(f"{Entrenador.SEPARADOR}")
        print(f"")
        return False


    def imprimir(self):
        print(f"Entrenador")
        print(f"{Entrenador.SEPARADOR}")
        print(f"nivel: {self.__nivel}")
        print(f"")
        print(f"{Entrenador.SEPARADOR_1}")
        print(f"Pokedex:")
        print(f"")
        
        for pokemon in self.__pokedex:
            pokemon.imprimir()
            print("")
    
    
    
    
    
