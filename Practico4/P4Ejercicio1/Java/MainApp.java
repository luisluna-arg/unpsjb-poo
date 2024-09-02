import javax.swing.SwingUtilities;

import com.example.main.MainWindow;

public class MainApp {

    public static void main(String[] args) {
        // Use SwingUtilities.invokeLater to ensure thread safety
        SwingUtilities.invokeLater(() -> {
            // Create the main window
            MainWindow window = new MainWindow();
            window.setVisible(true);
        });
    }
}
