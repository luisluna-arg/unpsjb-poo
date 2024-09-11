import random
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QMessageBox

class MemoryGame(QWidget):
    def __init__(self):
        super().__init__()

        self.__conteo_fila = 4
        self.__conteo_columna = 4
        self.__unidad_tiempo = 1000
        # self.__tiempo_inicio_partida = 15000
        self.__tiempo_inicio_partida = 2000
        self.__color_por_defecto = "gray"
        self.__colores_base = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "lime"]
        self.__cero = "0"
        self.__boton_iniciar_partida_inicial = "Iniciar partida"
        self.__boton_iniciar_partida_jugando = "Jugando"

        self.setWindowTitle("Memo")
        self.setGeometry(100, 100, 450, 300)
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.__boton_iniciar = QPushButton(self.__boton_iniciar_partida_inicial, self)
        self.__boton_iniciar.clicked.connect(self.__iniciar_partida)
        self.layout.addWidget(self.__boton_iniciar, 0, 0, 1, 1)

        self.__etiqueta_tiempo = QLabel(self.__cero, self)
        self.layout.addWidget(self.__etiqueta_tiempo, 0, 1, 1, 3)
        
        self.__cronometro = QTimer()
        self.__cronometro.timeout.connect(self.__actualizar_cronometro)
        self.__tiempo_en_curso = 0
        
        self.__botones = []
        for i in range(self.__conteo_columna):
            fila = []
            for j in range(self.__conteo_fila):
                boton = self.__crear_boton()
                fila.append(boton)
                self.layout.addWidget(boton, i+1, j)
            self.__botones.append(fila)
        
        self.__colores = []
        self.__botones_seleccionados = []
        
    def __crear_boton(self):
        boton = QPushButton(self)
        boton.setFixedSize(100, 100)
        self.__set_fondo_boton(boton, self.__color_por_defecto)
        boton.clicked.connect(self.__mostrar_tarjeta)
        boton.setEnabled(False)
        return boton

    def __iniciar_partida(self):
        self.__boton_iniciar.setText(self.__boton_iniciar_partida_jugando)
        self.__boton_iniciar.setEnabled(False)
        self.__tiempo_en_curso = 0
        self.__cronometro.stop()
        self.__cronometro.start(1000)
        self.__etiqueta_tiempo.setText(self.__cero)
        self.__colores = self.__colores_base * 2
        random.shuffle(self.__colores)
        self.__botones_seleccionados = []
        for fila in self.__botones:
            for boton in fila:
                self.__set_fondo_boton(boton, self.__color_por_defecto)
                boton.setEnabled(True)
        
        for i, fila in enumerate(self.__botones):
            for j, boton in enumerate(fila):
                self.__set_fondo_boton(boton, self.__colores[i * self.__conteo_fila + j])

        QTimer.singleShot(self.__tiempo_inicio_partida + self.__unidad_tiempo, self.__ocultar_tarjetas)
    
    def __ocultar_tarjetas(self):
        self.__cronometro.stop()
        self.__tiempo_en_curso = 0
        
        for row in self.__botones:
            for boton in row:
                self.__set_fondo_boton(boton, "lightgray")
        
        self.__cronometro.start(self.__unidad_tiempo)
    
    def __actualizar_cronometro(self):
        # Update the timer label
        self.__tiempo_en_curso += 1
        self.__etiqueta_tiempo.setText(f"{self.__tiempo_en_curso}")
    
    def __mostrar_tarjeta(self):
        boton = self.sender()
        idx = self.__get_indice_boton(boton)        
        self.__set_fondo_boton(boton, self.__colores[idx])
        self.__botones_seleccionados.append(boton)
        
        if len(self.__botones_seleccionados) == 2:
            self.__verificar()

    def __verificar(self):
        boton1, boton2 = self.__botones_seleccionados
        idx1 = self.__get_indice_boton(boton1)
        idx2 = self.__get_indice_boton(boton2)
        
        print(f"Iguales: {self.__colores[idx1] == self.__colores[idx2]}")
        
        if self.__colores[idx1] == self.__colores[idx2]:
            boton1.setEnabled(False)
            boton2.setEnabled(False)
            if all(not boton.isEnabled() for row in self.__botones for boton in row):
                self.__finalizar()
        else:
            print(f"ocultar")
            QTimer.singleShot(self.__unidad_tiempo, self.__ocultar_tarjetas_seleccionadas)

    def __ocultar_tarjetas_seleccionadas(self):
        for boton in self.__botones_seleccionados:
            print(f"{self.__get_indice_boton(boton)}")
            self.__set_fondo_boton(boton, "lightgray")
        
        self.__botones_seleccionados = []
    
    def __get_indice_boton(self, boton):
        for i, fila in enumerate(self.__botones):
            if boton in fila:
                return i * self.__conteo_fila + fila.index(boton)
        return None
        
    def __set_fondo_boton(self, boton, color):
        boton.setStyleSheet(f"background-color: {color}")
    
    def __finalizar(self):
        self.__cronometro.stop()
        QMessageBox.information(self, "Felicidades!", f"Completaste el juego en {self.__tiempo_en_curso} segundos")