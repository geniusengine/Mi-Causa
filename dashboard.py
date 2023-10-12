import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt6.uic import loadUi

class DashboardApp(QMainWindow):
    def __init__(self, username):
        super().__init__()

        # Cargar la interfaz desde el archivo .ui
        loadUi("dashboard.ui", self)


        # Configurar la parte superior, izquierda y centro como secciones
        self.top_section = QWidget()
        self.left_section = QWidget()
        self.center_section = QWidget()

        self.top_layout = QVBoxLayout(self.top_section)
        self.left_layout = QVBoxLayout(self.left_section)

        # Obtener el nombre del usuario desde la base de datos o cualquier otro método
        self.username = username

        # Mostrar un mensaje de bienvenida con el nombre del usuario
        welcome_label = QLabel(f"Bienvenido, {self.username}!")
        self.top_layout.addWidget(welcome_label)

        # Agregar las secciones al diseño principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.top_section)
        main_layout.addWidget(self.left_section)
        main_layout.addWidget(self.center_section)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

def main():
    # Supongamos que has obtenido el nombre de usuario de la base de datos después de la autenticación.
    username = "Nombre de Usuario"  # Reemplaza esto con el nombre real del usuario.

    app = QApplication(sys.argv)
    window = DashboardApp(username)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
