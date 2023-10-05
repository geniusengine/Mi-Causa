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
Dernière modification : mercredi 4 octobre 2023 à 21:31:37
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from login import LoginApp
from formularios.registro import RegisterApp

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Menú Principal")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.clicked.connect(self.open_login)
        self.register_button = QPushButton("Registro (Usuario y Contraseña Designados)")
        self.register_button.clicked.connect(self.open_registro)

        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)

        self.central_widget.setLayout(self.layout)

    def open_login(self):
        self.login_app = LoginApp()
        self.login_app.show()

    def open_registro(self):
        #Verificar usuario y contraseña designados aquí
        usuario_designado = "usuario_designado"
        contrasena_designada = "contrasena_designada"

        usuario_ingresado, contrasena_ingresada = self.get_usuario_contraseña()

        if usuario_ingresado == usuario_designado and contrasena_ingresada == contrasena_designada:
            self.registro_app = RegisterApp()
            self.registro_app.show()
        else:
            print("Usuario y/o contraseña incorrectos.")

    def get_usuario_contraseña(self):
        # Implementar la obtención de usuario y contraseña aquí
        # Puedes usar un cuadro de diálogo, por ejemplo.
        usuario = "usuario_ingresado"
        contraseña = "contraseña_ingresada"
        return usuario, contraseña

def main():
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
