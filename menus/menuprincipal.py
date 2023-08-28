"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: danie(mitchel.dmch@gmail.com) 
menuprincipal.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  samedi 26 août 2023 à 18:44:12 
Dernière modification : samedi 26 août 2023 à 18:44:16
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menú Principal")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        image_label = QLabel(self)
        pixmap = QPixmap("path_to_your_image.png")  # Cambia esto por la ruta de tu imagen
        pixmap = pixmap.scaledToWidth(300)  # Ajusta el tamaño de la imagen
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        login_button = QPushButton("Ingresar al Login")
        login_button.clicked.connect(self.open_login)
        layout.addWidget(login_button)

        register_button = QPushButton("Ir al Registro")
        register_button.clicked.connect(self.open_register)
        layout.addWidget(register_button)

        self.central_widget.setLayout(layout)

    def open_login(self):
        login_window = LoginWindow()
        login_window.show()

    def open_register(self):
        register_window = RegisterWindow()
        register_window.show()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana de Inicio de Sesión")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Página de Inicio de Sesión"))

        self.setLayout(layout)

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana de Registro")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Página de Registro"))

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())