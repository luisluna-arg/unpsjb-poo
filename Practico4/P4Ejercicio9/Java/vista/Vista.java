import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;

public class Vista extends JFrame {

    private JButton botonSeleccionarArchivo;
    private JButton botonLeerArchivo;
    private JTable tabla;
    private JLabel mensajeError;
    private DefaultTableModel tableModel;

    public Vista() {
        // Configuración de la ventana principal
        setTitle("Lector CSV");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Configuración del layout principal
        JPanel panelCentral = new JPanel();
        panelCentral.setLayout(new BorderLayout());

        JPanel layoutBotones = new JPanel();
        layoutBotones.setLayout(new FlowLayout());

        // Botón de seleccionar archivo
        botonSeleccionarArchivo = new JButton("Seleccionar Archivo CSV");
        layoutBotones.add(botonSeleccionarArchivo);

        // Botón de leer archivo
        botonLeerArchivo = new JButton("Leer Archivo");
        layoutBotones.add(botonLeerArchivo);

        // Añadir botones al panel principal
        panelCentral.add(layoutBotones, BorderLayout.NORTH);

        // Configuración de la tabla
        tableModel = new DefaultTableModel();
        tabla = new JTable(tableModel);
        tableModel.setColumnIdentifiers(DataLabels.LABELS.toArray());  // Configurar encabezados de columna
        
        JScrollPane scrollPane = new JScrollPane(tabla);
        panelCentral.add(scrollPane, BorderLayout.CENTER);

        // Mensaje de error
        mensajeError = new JLabel("");
        mensajeError.setForeground(Color.RED);
        panelCentral.add(mensajeError, BorderLayout.SOUTH);

        // Añadir el panel al marco
        add(panelCentral);
    }

    public JButton getBotonSeleccionarArchivo() {
        return botonSeleccionarArchivo;
    }

    public JButton getBotonLeerArchivo() {
        return botonLeerArchivo;
    }

    public JTable getTabla() {
        return tabla;
    }

    public JLabel getMensajeError() {
        return mensajeError;
    }

    public DefaultTableModel getTableModel() {
        return tableModel;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Vista vista = new Vista();
            vista.setVisible(true);
        });
    }
}