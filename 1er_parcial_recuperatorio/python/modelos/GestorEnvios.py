class GestorEnvios:
    pass

    def gestionar_envio(self, transportes, paquete, distancia):
        print("Gestionando el envio del paquete pesado:")

        if (len(transportes) == 0):
            self.__resolver_transporte_no_disponible()
            
        transportes_disponibles = list(filter(lambda transporte: transporte.peso_max >= max(paquete.peso, paquete.calcular_peso_volumetrico()), transportes))

        if (len(transportes_disponibles) == 0):
            print("No hay transportes disponibles para este tipo de paquete.")
            return

        mejor_transporte = sorted(
            transportes_disponibles,
            reverse=True, 
            key=lambda obj: obj.transportar_paquete(distancia, max(paquete.peso, paquete.calcular_peso_volumetrico()))
            )[0]

        factor = mejor_transporte.transportar_paquete(distancia, max(paquete.peso, paquete.calcular_peso_volumetrico()))
        tiempo = mejor_transporte.tiempo_estimado(distancia)    
        costo = mejor_transporte.costo_estimado(distancia)

        print(f"El mejor transporte para el paquete es {mejor_transporte.nombre} con un "
            f"factor de {factor}. Tiempo: {tiempo} horas, Costo: {costo}")