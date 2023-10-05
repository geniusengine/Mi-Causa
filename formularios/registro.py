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
Dernière modification : mercredi 4 octobre 2023 à 19:00:15
"""
import sys
import sqlite3
from passlib.hash import bcrypt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class RegisterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.init_db()

    def init_ui(self):
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 300, 250)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()
        self.email_label = QLabel("Correo Electrónico:")
        self.email_input = QLineEdit()
        self.username_label = QLabel("Usuario:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_button = QPushButton("Registrar")
        self.register_button.clicked.connect(self.register_user)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.register_button)

        self.central_widget.setLayout(self.layout)

    def init_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("usuarios.db")

        if not db.open():
            print("Error al conectar a la base de datos.")
            sys.exit(1)

        self.query = QSqlQuery()

    def register_user(self):
        name = self.name_input.text()
        email = self.email_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        # Cifrar la contraseña antes de almacenarla
        hashed_password = bcrypt.hash(password)

        # Insertar el nuevo usuario en la base de datos
        if self.query.exec("INSERT INTO usuarios (nombre, email, username, password) VALUES (?, ?, ?, ?)",
                           (name, email, username, hashed_password)):
            print("Registro exitoso.")
        else:
            print("Error al registrar el usuario:", self.query.lastError().text())

def main():
    app = QApplication(sys.argv)
    register_app = RegisterApp()
    register_app.show()

    # Cierra la conexión de la base de datos cuando se cierra la aplicación
    app.aboutToQuit.connect(register_app.close_db_connection)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
