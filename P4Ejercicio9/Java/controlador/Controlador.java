import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Controlador {
    private CSV modelo;
    private Vista vista;
    private String rutaArchivo;

    public Controlador(CSV modelo, Vista vista) {
        this.modelo = modelo;
        this.vista = vista;

        // Action listeners for buttons
        vista.getBotonSeleccionarArchivo().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                seleccionarArchivo();
            }
        });

        vista.getBotonLeerArchivo().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cargarArchivo();
            }
        });

        this.rutaArchivo = null;
    }

    public Vista getVista()
    {
        return vista;
    }

    private void seleccionarArchivo() {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setDialogTitle("Seleccionar archivo CSV");
        int result = fileChooser.showOpenDialog(vista);
        if (result == JFileChooser.APPROVE_OPTION) {
            rutaArchivo = fileChooser.getSelectedFile().getAbsolutePath();
            vista.getMensajeError().setText("Archivo seleccionado: " + rutaArchivo);
        }
    }

    private void cargarArchivo() {
        if (rutaArchivo == null) {
            vista.getMensajeError().setText("Primero debe seleccionar un archivo.");
            return;
        }

        try {
            leerArchivo(rutaArchivo);
            mostrarDatosEnTabla();
            vista.getMensajeError().setText("");
        } catch (Exception e) {
            vista.getMensajeError().setText(e.getMessage());
        }
    }

    private void leerArchivo(String rutaArchivo) throws Exception {
        try (BufferedReader br = new BufferedReader(new FileReader(rutaArchivo))) {
            String encabezado = br.readLine();
            if (!encabezado.equals(String.join(",", DataLabels.FIELDS))) {
                throw new Exception("El archivo no tiene el formato de encabezado correcto.");
            }

            String linea;

            while ((linea = br.readLine()) != null) {
                String[] datos = linea.split(",");

                if (datos.length != DataLabels.FIELDS.size()) {
                    throw new Exception("Línea no cumple con el formato esperado: " + linea);
                }

                for (int i = 0; i < DataLabels.FIELDS.size(); i++) {
                    modelo.getData().add(new ArrayList<String>(Arrays.asList(DataLabels.FIELDS.get(i), datos[i])));
                }
            }
        }
    }

    private void mostrarDatosEnTabla() {
        DefaultTableModel tableModel = (DefaultTableModel) vista.getTableModel();
        tableModel.setRowCount(0);  // Limpiar la tabla

        for (ArrayList<String> fila : modelo.getData()) {
            Object[] rowData = new Object[DataLabels.FIELDS.size()];
            for (int i = 0; i < DataLabels.FIELDS.size(); i++) {
                rowData[i] = fila.get(i);
            }
            tableModel.addRow(rowData);
        }
    }
}
