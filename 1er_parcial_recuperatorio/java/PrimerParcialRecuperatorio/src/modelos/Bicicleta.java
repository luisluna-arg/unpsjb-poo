package modelos;

public class Bicicleta implements Transporte {

    private String nombre;
    private final double pesoMax = 5; // KG
    private final double velocidadPromedio = 12; // Km/h
    private final double valorPorKm = 200; // pesos

    public Bicicleta(String nombre) {
        this.nombre = nombre;
    }

    public double transportarPaquete(double distancia, double pesoPaquete) {
        if (pesoPaquete > pesoMax) {
            return -1;
        }

        double indicadorConveniencia = 0.2 * tiempoEstimado(distancia) + 0.8 * costoEstimado(distancia);

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
