import sys
from Idiomas.Espanol import Espanol
from Idiomas.Frances import Frances
from Idiomas.Ingles import Ingles
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QTextEdit
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Traductor de Idiomas")
        self.resize(400, 300)
        self.center()

        # Create layout and widgets
        layout = QVBoxLayout()
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)

        self.language_combo = QComboBox()
        self.language_combo.addItems(["Inglés", "Francés", "Portugués"])

        show_button = QPushButton("Mostrar")
        show_button.clicked.connect(self.show_translation)

        layout.addWidget(self.language_combo)
        layout.addWidget(show_button)
        layout.addWidget(self.text_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Default language
        self.idioma = Ingles()

    def show_translation(self):
        if self.language_combo.currentText() == "Inglés":
            self.idioma = Ingles()
        elif self.language_combo.currentText() == "Francés":
            self.idioma = Frances()
        elif self.language_combo.currentText() == "Portugués":
            self.idioma = Espanol()

        message = (f"Saludar: {self.idioma.saludar()}\n"
            f"Despedirse: {self.idioma.despedirse()}\n"
            f"Perdón: {self.idioma.perdon()}\n"
            f"Pedir café: {self.idioma.pedirCafe()}\n"
            f"Cuánto cuesta: {self.idioma.cuantoCuesta()}\n"
            f"Dónde queda: {self.idioma.dondeQueda()}")
        self.text_area.setText(message)

    def center(self):
        # Center the window on the screen
        screen = QApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
