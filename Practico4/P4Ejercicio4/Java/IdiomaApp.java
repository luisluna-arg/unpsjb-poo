package P4Ejercicio4.Java;

import javax.swing.*;

import P4Ejercicio4.Java.Idiomas.Espanol;
import P4Ejercicio4.Java.Idiomas.Frances;
import P4Ejercicio4.Java.Idiomas.Idioma;
import P4Ejercicio4.Java.Idiomas.Ingles;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class IdiomaApp extends JFrame {

    private Idioma idioma;

    public IdiomaApp() {
        setTitle("Traductor de Idiomas");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Create components
        JComboBox<String> languageComboBox = new JComboBox<>(new String[] { "Inglés", "Francés", "Español" });
        JTextArea messageArea = new JTextArea(10, 30);
        JButton showButton = new JButton("Mostrar");

        // Add components to the frame
        JPanel topPanel = new JPanel();
        topPanel.add(new JLabel("Selecciona el idioma:"));
        topPanel.add(languageComboBox);
        add(topPanel, BorderLayout.NORTH);
        add(new JScrollPane(messageArea), BorderLayout.CENTER);
        add(showButton, BorderLayout.SOUTH);

        // Set the default language
        setIdioma(new Ingles());

        // Add action listener to the button
        showButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                switch (languageComboBox.getSelectedItem().toString()) {
                    case "Inglés":
                        setIdioma(new Ingles());
                        break;
                    case "Francés":
                        setIdioma(new Frances());
                        break;
                    case "Español":
                        setIdioma(new Espanol());
                        break;
                }
                String message = "Saludar: " + idioma.saludar() + "\n"
                        + "Despedirse: " + idioma.despedirse() + "\n"
                        + "Perdón: " + idioma.perdon() + "\n"
                        + "Pedir café: " + idioma.pedirCafe() + "\n"
                        + "Cuánto cuesta: " + idioma.cuantoCuesta() + "\n"
                        + "Dónde queda: " + idioma.dondeQueda();
                messageArea.setText(message);
            }
        });
    }

    private void setIdioma(Idioma idioma) {
        this.idioma = idioma;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            IdiomaApp app = new IdiomaApp();
            app.setVisible(true);
        });
    }
}
