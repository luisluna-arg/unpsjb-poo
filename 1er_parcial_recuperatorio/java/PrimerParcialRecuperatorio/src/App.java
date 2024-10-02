import java.util.ArrayList;
import modelos.Bicicleta;
import modelos.Furgoneta;
import modelos.GestorEnvios;
import modelos.Paquete;
import modelos.Transporte;


public class App {
    public static void main(String[] args) {
        GestorEnvios gestorEnvios = new GestorEnvios();

        Paquete paqueteLiviano = new Paquete(10, 20);
        Paquete paquetePesado = new Paquete(400, 400);

        System.out.println(paqueteLiviano);
        System.out.println(paquetePesado);

        ArrayList<Transporte> transportes = new ArrayList<>();
        transportes.add(new Bicicleta("Bicicleta"));
        transportes.add(new Furgoneta("Furgoneta"));

        gestorEnvios.gestionarEnvio(transportes, paqueteLiviano, 20);
        gestorEnvios.gestionarEnvio(transportes, paquetePesado, 2000);
    }
}
