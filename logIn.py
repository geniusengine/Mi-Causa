import sys
import sqlite3
from passlib.hash import bcrypt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.init_db()

    def init_ui(self):
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.username_label = QLabel("Usuario:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.clicked.connect(self.authenticate)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)

        self.central_widget.setLayout(self.layout)

    def init_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("usuarios.db")

        if not db.open():
            print("Error al conectar a la base de datos.")
            sys.exit(1)

        self.query = QSqlQuery()

    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()

        
        if self.query.exec("SELECT password FROM usuarios WHERE username = ?", (username,)) and self.query.next():
            stored_password = self.query.value(0)
            if bcrypt.verify(password, stored_password):
                print("Inicio de sesión exitoso.")
            else:
                print("Contraseña incorrecta.")
        else:
            print("Usuario no encontrado.")

def main():
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()

    # Cierra la conexión de la base de datos cuando se cierra la aplicación
    app.aboutToQuit.connect(login_app.close_db_connection)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
