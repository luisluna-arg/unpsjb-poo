package P4Ejercicio4.Java.Idiomas;

public class Espanol implements Idioma {
    @Override
    public String saludar() {
        return "Hola";
    }

    @Override
    public String despedirse() {
        return "Adiós";
    }

    @Override
    public String perdon() {
        return "Perdón";
    }

    @Override
    public String pedirCafe() {
        return "¿Puedes darme un café?";
    }

    @Override
    public String cuantoCuesta() {
        return "¿Cuanto cuesta esto?";
    }

    @Override
    public String dondeQueda() {
        return "¿Donde queda?";
    }
}
