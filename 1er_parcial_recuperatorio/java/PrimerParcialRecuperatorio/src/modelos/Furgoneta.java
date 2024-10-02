package modelos;

public class Furgoneta implements Transporte {

    private String nombre;
    private final double pesoMax = 100; // KG
    private final double velocidadPromedio = 60; // Km/h
    private final double valorPorKm = 1000; // pesos

    public Furgoneta(String nombre) {
        this.nombre = nombre;
    }

    public double transportarPaquete(double distancia, double pesoPaquete) {
        if (pesoPaquete > pesoMax) {
            return -1;
        }

        double indicadorConveniencia = 0.7 * tiempoEstimado(distancia) + 0.3 * costoEstimado(distancia);

        return indicadorConveniencia;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPesoMax() {
        return pesoMax;
    }

    public double tiempoEstimado(double distancia) {
        return distancia / velocidadPromedio; // Horas
    }

    public double costoEstimado(double distancia) {
        return distancia * valorPorKm;
    }
}
