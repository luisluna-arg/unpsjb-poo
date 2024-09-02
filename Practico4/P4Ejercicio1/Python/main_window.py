from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.resize(400, 200)
        self.center()

        self.setWindowTitle("Mi aplicación")

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        boton_confirmar = QPushButton("Confirmar eliminación")
        boton_confirmar.clicked.connect(self.eliminar_usuario)
        layout.addWidget(boton_confirmar)
        
        boton_leer_entrada = QPushButton("Leer entrada")
        boton_leer_entrada.clicked.connect(self.leer_entrada)
        layout.addWidget(boton_leer_entrada)

    def eliminar_usuario(self):
        dialogo = QMessageBox()
        dialogo.setWindowTitle("Confirmación")
        dialogo.setText("¿Está seguro que quiere dar de baja al usuario?")
        dialogo.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        response = dialogo.exec()

        dialogo = QMessageBox()
        dialogo.setWindowTitle("Resultado")
        dialogo.setText("Usuario dado de baja" if response == QMessageBox.StandardButton.Ok else "Operación cancelada")
        dialogo.exec()
        
    def leer_entrada(self):
        text, ok = QInputDialog.getText(self, "Ingrese Texto", "Por favor ingrese un texto:")

        if ok and text:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Texto Ingresado")
            msg_box.setText(f"Usted ingresó: {text}")
            msg_box.exec()
            
    def center(self):
        geometry = self.frameGeometry()
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())
