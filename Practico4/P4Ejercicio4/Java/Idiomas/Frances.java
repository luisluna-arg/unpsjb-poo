package P4Ejercicio4.Java.Idiomas;

public class Frances implements Idioma {
    @Override
    public String saludar() {
        return "Bonjour";
    }

    @Override
    public String despedirse() {
        return "Au revoir";
    }

    @Override
    public String perdon() {
        return "Désolé";
    }

    @Override
    public String pedirCafe() {
        return "Puis-je avoir un café ?";
    }

    @Override
    public String cuantoCuesta() {
        return "Combien ça coûte ?";
    }

    @Override
    public String dondeQueda() {
        return "Où est-ce ?";
    }
}
