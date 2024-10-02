package logisticas;

import transportes.Camion;
import transportes.Transporte;

public class LogisticaTerrestre extends Logistica {
    @Override
    public Transporte crearTransporte() {
        return new Camion();  // Devuelve un camión
    }
}