package modelos;

public class Paquete {

    private double peso;
    private double volumen;

    public Paquete(double peso, double volumen) {
        this.peso = peso;
        this.volumen = volumen;
    }

    public double getPeso() {
        return peso;
    }

    public double calcularPesoVolumetrico() {
        return volumen / 5000;
    }

    @Override
    public String toString() {
        return "Peso: " + peso + "\n" +
               "Volumen: " + volumen + "\n" +
               "Peso volumétrico: " + calcularPesoVolumetrico();
    }
}
