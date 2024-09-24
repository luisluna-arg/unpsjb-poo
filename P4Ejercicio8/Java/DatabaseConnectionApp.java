import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnectionApp extends JFrame {
    private JTextField hostInput;
    private JTextField portInput;
    private JTextField dbInput;
    private JTextField userInput;
    private JPasswordField passwordInput;
    private JButton testButton;

    public DatabaseConnectionApp() {
        setTitle("PostgreSQL Connection Test");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(6, 2));

        // Labels and text fields
        add(new JLabel("Host:"));
        hostInput = new JTextField();
        add(hostInput);

        add(new JLabel("Port:"));
        portInput = new JTextField();
        add(portInput);

        add(new JLabel("Database:"));
        dbInput = new JTextField();
        add(dbInput);

        add(new JLabel("User:"));
        userInput = new JTextField();
        add(userInput);

        add(new JLabel("Password:"));
        passwordInput = new JPasswordField();
        add(passwordInput);

        // Button
        testButton = new JButton("Test Connection");
        add(testButton);

        // Action Listener for the button
        testButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                testDbConnection();
            }
        });

        pack();
        setLocationRelativeTo(null); // Center the window
    }

    // Function to test connection to PostgreSQL
    private void testDbConnection() {
        String host = hostInput.getText();
        String port = portInput.getText();
        String dbname = dbInput.getText();
        String user = userInput.getText();
        String password = new String(passwordInput.getPassword());

        String url = "jdbc:postgresql://" + host + ":" + port + "/" + dbname;
        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            JOptionPane.showMessageDialog(this, "Database connection successful!", "Connection Successful", JOptionPane.INFORMATION_MESSAGE);
        } catch (SQLException ex) {
            JOptionPane.showMessageDialog(this, "Error connecting to the database: " + ex.getMessage(), "Connection Failed", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            DatabaseConnectionApp app = new DatabaseConnectionApp();
            app.setVisible(true);
        });
    }
}
