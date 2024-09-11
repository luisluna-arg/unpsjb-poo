import random

from Modelos.BronceEspecial import BronceEspecial
from Modelos.Plantilla import Plantilla
from Modelos.Oro import Oro
from Modelos.Especial import Especial
from Modelos.TipoCartaEnum import TipoCartaEnum

def main():

    habilidades_especiales = ["Ataque", "Pase", "Defensa"]
    clubes = ["Arsenal", "Montevideo City Torque", "Inter Miami", "Manchester City"]
    paises = ["Argentina", "Inglaterra", "Holanda", "Japón"]
    
    cartas = []
    for i in range(22):
        equipo_fav = random.choice(clubes)
        pais = random.choice(paises)
        
        tipo_carta = random.choice(TipoCartaEnum.values())    
        if (tipo_carta == TipoCartaEnum.BronceEspecial):
            habilidad_especial = random.choice(habilidades_especiales)
            carta = BronceEspecial(f"Jugador {i}", equipo_fav, pais)
            carta.habilidad_especial = habilidad_especial
        elif (tipo_carta == TipoCartaEnum.Oro):
            carta = Oro(f"Jugador {i}", equipo_fav, pais)
        elif (tipo_carta == TipoCartaEnum.Especial):
            carta = Especial(f"Jugador {i}", equipo_fav, pais)
            for j in range(1, 3):
                habilidad_especial = random.choice(habilidades_especiales)
                while (habilidad_especial in carta.habilidades_especiales): 
                    habilidad_especial = random.choice(habilidades_especiales)

                carta.agregar_habilidad_especial(habilidad_especial)

        cartas.append(carta)
        
    random.shuffle(cartas)
    
    equipo_1 = Plantilla("Usuario 1", random.choice(paises), random.choice(clubes))
    equipo_2 = Plantilla("Usuario 2", random.choice(paises), random.choice(clubes))
    
    equipo_1.agregar_cartas(cartas[:11])
    equipo_2.agregar_cartas(cartas[11:])
    
    print(equipo_1)
    print(equipo_2)


if __name__ == "__main__":
    main()
