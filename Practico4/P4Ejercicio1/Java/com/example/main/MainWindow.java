package com.example.main;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JOptionPane;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MainWindow extends JFrame {

    public MainWindow() {
        setTitle("Mi aplicación");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        centerWindow();

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

        JButton btnConfirmar = new JButton("Confirmar eliminación");
        btnConfirmar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                eliminarUsuario();
            }
        });
        panel.add(btnConfirmar);

        JButton btnLeerEntrada = new JButton("Leer entrada");
        btnLeerEntrada.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                leerEntrada();
            }
        });
        panel.add(btnLeerEntrada);

        add(panel, BorderLayout.CENTER);
    }

    private void eliminarUsuario() {
        int response = JOptionPane.showConfirmDialog(this,
                "¿Está seguro que quiere dar de baja al usuario?",
                "Confirmación",
                JOptionPane.OK_CANCEL_OPTION,
                JOptionPane.QUESTION_MESSAGE);

        JOptionPane.showMessageDialog(this,
                response == JOptionPane.OK_OPTION ? "Usuario dado de baja" : "Operación cancelada",
                "Resultado",
                JOptionPane.INFORMATION_MESSAGE);
    }

    private void leerEntrada() {
        String input = JOptionPane.showInputDialog(this,
                "Por favor ingrese un texto:",
                "Ingrese Texto",
                JOptionPane.PLAIN_MESSAGE);

        if (input != null && !input.isEmpty()) {
            JOptionPane.showMessageDialog(this,
                    "Usted ingresó: " + input,
                    "Texto Ingresado",
                    JOptionPane.INFORMATION_MESSAGE);
        }
    }

    private void centerWindow() {
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        Dimension frameSize = getSize();
        int x = (screenSize.width - frameSize.width) / 2;
        int y = (screenSize.height - frameSize.height) / 2;
        setLocation(x, y);
    }
}
