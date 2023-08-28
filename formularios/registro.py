"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: danie(mitchel.dmch@gmail.com) 
registro.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  samedi 26 août 2023 à 18:37:13 
Dernière modification : samedi 26 août 2023 à 18:37:47
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class UserRegistrationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de Usuarios")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Registro de Usuarios")
        self.layout.addWidget(self.label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nombre")
        self.layout.addWidget(self.name_input)

        self.lastname_input = QLineEdit()
        self.lastname_input.setPlaceholderText("Apellido")
        self.layout.addWidget(self.lastname_input)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Usuario")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_input)

        self.register_button = QPushButton("Registrar")
        self.register_button.clicked.connect(self.register_user)
        self.layout.addWidget(self.register_button)

        self.central_widget.setLayout(self.layout)

    def register_user(self):
        name = self.name_input.text()
        lastname = self.lastname_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        # este lado para hacer el almacenamiento en la base de datos
        print(f"Usuario registrado:\nNombre: {name}\nApellido: {lastname}\nUsuario: {username}\nContraseña: {password}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserRegistrationApp()
    window.show()
    sys.exit(app.exec())