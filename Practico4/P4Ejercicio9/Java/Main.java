import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Controlador controlador = new Controlador(new CSV(), new Vista());

            controlador.getVista().setVisible(true);
            controlador.getVista().setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        });
    }
}
