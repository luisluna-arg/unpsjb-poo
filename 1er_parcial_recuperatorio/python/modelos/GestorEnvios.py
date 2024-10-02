class GestorEnvios:
    pass

    def gestionar_envio(self, transportes, paquete, distancia):
        print("Gestionando el envio del paquete pesado:")

        if (len(transportes) == 0):
            self.__resolver_transporte_no_disponible()

        for tranporte_disponible in transportes:
            factor = tranporte_disponible.transportar_paquete(
                paquete, distancia)
            if (factor > 0):
                tiempo = tranporte_disponible.tiempo_estimado(distancia)
                costo = tranporte_disponible.costo_estimado(distancia)
                print(
                    f"El mejor transporte para el paquete es Furgoneta con un "
                    f"factor de {factor}.\n"
                    f"Tiempo: {tiempo} horas, Costo: {costo}"
                )
                break
            else:
                print(
                    f"Paquete demasiado pesado para {tranporte_disponible.nombre}")

        self.__resolver_transporte_no_disponible()

    def __resolver_transporte_no_disponible(self):
        print("No hay transportes disponibles para este tipo de paquete.")
