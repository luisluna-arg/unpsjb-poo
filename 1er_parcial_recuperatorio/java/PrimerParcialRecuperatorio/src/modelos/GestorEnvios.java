package modelos;

import java.util.List;
import java.util.Comparator;

public class GestorEnvios {

    public void gestionarEnvio(List<Transporte> transportes, Paquete paquete, double distancia) {
        System.out.println("Gestionando el envio del paquete pesado:");

        if (transportes.isEmpty()) {
            resolverTransporteNoDisponible();
            return;
        }

        // Filter the available transport options based on weight limits
        List<Transporte> transportesDisponibles = transportes.stream()
            .filter(transporte -> transporte.getPesoMax() >= Math.max(paquete.getPeso(), paquete.calcularPesoVolumetrico()))
            .toList();

        if (transportesDisponibles.isEmpty()) {
            System.out.println("No hay transportes disponibles para este tipo de paquete.");
            return;
        }

        // Select the best transport option based on the given factors
        Transporte mejorTransporte = transportesDisponibles.stream()
            .max(Comparator.comparing(transporte -> transporte.transportarPaquete(distancia, Math.max(paquete.getPeso(), paquete.calcularPesoVolumetrico()))))
            .orElseThrow();

        double factor = mejorTransporte.transportarPaquete(distancia, Math.max(paquete.getPeso(), paquete.calcularPesoVolumetrico()));
        double tiempo = mejorTransporte.tiempoEstimado(distancia);
        double costo = mejorTransporte.costoEstimado(distancia);

        System.out.println("El mejor transporte para el paquete es " + mejorTransporte.getNombre() + " con un factor de " + factor +
            ". Tiempo: " + tiempo + " horas, Costo: " + costo);
    }

    private void resolverTransporteNoDisponible() {
        // Implement logic to handle the case where no transport is available
        System.out.println("No hay transportes disponibles.");
    }
}
