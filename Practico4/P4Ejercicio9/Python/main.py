import sys
from PyQt6.QtWidgets import QApplication
from modelo.DataLabels import DataLabels
from modelo.CSV import CSV
from vista.Vista import Vista
from controlador.Controlador import Controlador

if __name__ == '__main__':
    app = QApplication(sys.argv)

    data_labels = DataLabels()

    modelo = CSV()
    vista = Vista()
    controlador = Controlador(modelo, vista)

    vista.show()
    sys.exit(app.exec())
