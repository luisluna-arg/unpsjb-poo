package modelos;

public interface Transporte {

    double transportarPaquete(double distancia, double pesoPaquete);
    String getNombre();
    double getPesoMax();
    double tiempoEstimado(double distancia);
    double costoEstimado(double distancia);
}
