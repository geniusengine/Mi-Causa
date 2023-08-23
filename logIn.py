import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont, QPixmap

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Inicio de sesión")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,50)


        
        password_label = QLabel(self)
        password_label.setText("Contraseña")
        password_label.setFont(QFont('Arial', 10))
        password_label.move(20,86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(90,82)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
