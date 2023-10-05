"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: danie(danie.pro@gmail.com) 
estampados.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  mercredi 4 octobre 2023 à 21:16:55 
Dernière modification : mercredi 4 octobre 2023 à 21:27:07
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPainter, QPixmap, QImage, QPen, QColor
from PyQt6.QtCore import Qt

class FichaDeRolApp(QMainWindow):
    def init(self):
        super().init()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ficha de Rol con Estampados Judiciales")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel(self)
        layout.addWidget(self.label)

        self.addButton = QPushButton("Agregar Estampado Judicial", self)
        layout.addWidget(self.addButton)
        self.addButton.clicked.connect(self.agregarEstampado)

        self.canvas = QImage(self.size(), QImage.Format_RGBA8888)
        self.canvas.fill(Qt.GlobalColor.white.value)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.canvas)

    def agregarEstampado(self):
        # Simplemente, dibujemos una línea roja como ejemplo de estampado judicial.
        painter = QPainter(self.canvas)
        painter.setPen(QPen(QColor(Qt.GlobalColor.red)))
        painter.drawLine(50, 50, 200, 200)
        painter.end()

        self.update()

def main():
    app = QApplication(sys.argv)
    window = FichaDeRolApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
