import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import psycopg2

# Function to test connection to PostgreSQL
def test_connection(host, port, dbname, user, password):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        conn.close()
        return True
    except Exception as e:
        return False, str(e)

# GUI Application
class DatabaseConnectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PostgreSQL Connection Test')
        self.layout = QVBoxLayout()

        # Labels and text fields
        self.host_label = QLabel('Host:')
        self.host_input = QLineEdit()

        self.port_label = QLabel('Port:')
        self.port_input = QLineEdit()

        self.db_label = QLabel('Database:')
        self.db_input = QLineEdit()

        self.user_label = QLabel('User:')
        self.user_input = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Button
        self.test_button = QPushButton('Test Connection')
        self.test_button.clicked.connect(self.test_db_connection)

        # Add widgets to layout
        self.layout.addWidget(self.host_label)
        self.layout.addWidget(self.host_input)

        self.layout.addWidget(self.port_label)
        self.layout.addWidget(self.port_input)

        self.layout.addWidget(self.db_label)
        self.layout.addWidget(self.db_input)

        self.layout.addWidget(self.user_label)
        self.layout.addWidget(self.user_input)

        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        self.layout.addWidget(self.test_button)

        self.setLayout(self.layout)

    def test_db_connection(self):
        # Get input values
        host = self.host_input.text()
        port = self.port_input.text()
        dbname = self.db_input.text()
        user = self.user_input.text()
        password = self.password_input.text()

        # Test connection
        success, message = test_connection(host, port, dbname, user, password)

        if success:
            QMessageBox.information(self, 'Connection Successful', 'Database connection successful!')
        else:
            QMessageBox.critical(self, 'Connection Failed', f'Error connecting to the database: {message}')

# Main entry
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DatabaseConnectionApp()
    window.show()
    sys.exit(app.exec())
