package logisticas;

import transportes.Barco;
import transportes.Transporte;

public class LogisticaMaritima extends Logistica {
    @Override
    public Transporte crearTransporte() {
        return new Barco();  // Devuelve un barco
    }
}
