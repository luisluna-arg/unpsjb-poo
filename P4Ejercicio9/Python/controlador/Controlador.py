import csv
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
from modelo.DataLabels import DataLabels

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        
        self.vista.boton_seleccionar_archivo.clicked.connect(self.seleccionar_archivo)
        self.vista.boton_leer_archivo.clicked.connect(self.cargar_archivo)

        self.ruta_archivo = None

    def seleccionar_archivo(self):
        self.ruta_archivo, _ = QFileDialog.getOpenFileName(self.vista, "Seleccionar archivo CSV", "", "CSV Files (*.csv)")
        if self.ruta_archivo:
            self.vista.mensaje_error.setText("Archivo seleccionado: " + self.ruta_archivo)

    def cargar_archivo(self):
        if not self.ruta_archivo:
            self.vista.mensaje_error.setText("Primero debe seleccionar un archivo.")
            return
        
        try:
            self.leer_archivo(self.ruta_archivo)
            self.mostrar_datos_en_tabla()
            self.vista.mensaje_error.setText("")
        except Exception as e:
            self.vista.mensaje_error.setText(str(e))

    def leer_archivo(self, ruta_archivo):
        try:
            with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
                lector = csv.reader(archivo_csv)
                encabezado = next(lector)
                if encabezado != DataLabels.FIELDS:
                    raise ValueError("El archivo no tiene el formato de encabezado correcto.")

                for linea in lector:
                    if len(linea) != len(DataLabels.FIELDS):
                        raise ValueError(f"Línea no cumple con el formato esperado: {linea}")
                    
                    fila_dict = {encabezado[i]: linea[i] for i in range(len(encabezado))}
                    self.modelo.data.append(fila_dict)

        except Exception as e:
            raise e

    def mostrar_datos_en_tabla(self):
        self.vista.tabla.setRowCount(len(self.modelo.data))
        
        for fila, dato in enumerate(self.modelo.data):
            for i in range(len(DataLabels.FIELDS)):
                self.vista.tabla.setItem(fila, i, QTableWidgetItem(dato[DataLabels.FIELDS[i]]))
