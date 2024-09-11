class Plantilla:
    
    def __init__(self, usuario, pais_favorito, equipo_favorito):
        self.__usuario = usuario
        self.__pais_favorito = pais_favorito
        self.__equipo_favorito = equipo_favorito
        self.__cartas = []

    @property
    def equipo_favorito(self):
        return self.__equipo_favorito
        
    @property
    def pais_favorito(self):
        return self.__pais_favorito
        
    def agregar_carta(self, carta):
        if (len(self.__cartas) <= 11):
            self.__cartas.append(carta)
        else:
            raise "Plantilla completo no se pueden agregar más cartas"
        
    def agregar_cartas(self, cartas):
        if (len(cartas) <= 11):
            self.__cartas = []
            for carta in cartas:
                carta.plantilla = self
                self.__cartas.append(carta)
        else:
            raise "No se pueden agregar más de 11 cartas"
        
    def __calcular_quimica(self):
        quimica = 0
        for carta in self.__cartas:
            quimica += carta.calcular_quimica()
            
        return int(quimica / len(self.__cartas))
    
    def __str__(self):
        result = (f"Usuario: {self.__usuario}\n"
        f"pais favorito: {self.__pais_favorito}\n"
        f"Equipo favorito: {self.__equipo_favorito}\n"
        f"Quimica total: {self.__calcular_quimica()}\n"
        f"\n"
        f"Plantilla\n"
        f"=======\n")
        
        for carta in self.__cartas:
            result += (f"{carta}\n"
            "---------------\n\n")
            
        result += "\n"
        
        return result