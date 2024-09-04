import sys
from MainWindow import MemoryGame
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = MemoryGame()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
