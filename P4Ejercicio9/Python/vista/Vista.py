from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog, QLabel, QHBoxLayout

from modelo.DataLabels import DataLabels

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lector CSV")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout_principal = QVBoxLayout()
        self.layout_botones = QHBoxLayout()

        self.boton_seleccionar_archivo = QPushButton("Seleccionar Archivo CSV")
        self.layout_botones.addWidget(self.boton_seleccionar_archivo)

        self.boton_leer_archivo = QPushButton("Leer Archivo")
        self.layout_botones.addWidget(self.boton_leer_archivo)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(len(DataLabels.LABELS))
        self.tabla.setHorizontalHeaderLabels(DataLabels.LABELS)

        self.mensaje_error = QLabel("")
        self.mensaje_error.setStyleSheet("color: red;")

        self.layout_principal.addLayout(self.layout_botones)
        self.layout_principal.addWidget(self.tabla)
        self.layout_principal.addWidget(self.mensaje_error)

        self.central_widget.setLayout(self.layout_principal)
