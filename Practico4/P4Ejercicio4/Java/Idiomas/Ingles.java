package P4Ejercicio4.Java.Idiomas;

public class Ingles implements Idioma {
    @Override
    public String saludar() {
        return "Hello";
    }

    @Override
    public String despedirse() {
        return "Goodbye";
    }

    @Override
    public String perdon() {
        return "Sorry";
    }

    @Override
    public String pedirCafe() {
        return "Can I have a coffee?";
    }

    @Override
    public String cuantoCuesta() {
        return "How much does it cost?";
    }

    @Override
    public String dondeQueda() {
        return "Where is it?";
    }
}
