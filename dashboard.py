import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QStackedWidget
from PyQt6.QtCore import Qt
from funciones.excel import ExcelEditorApp


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Configura la ventana principal
        self.setWindowTitle("Dashboard en PyQt6")
        self.setGeometry(100, 100, 800, 600)

        # Crea un widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Crea un diseño vertical para organizar los widgets
        layout = QVBoxLayout()

        # Crea un QStackedWidget para gestionar las diferentes ventanas
        self.stacked_widget = QStackedWidget()

        # Agrega la ventana actual (puedes personalizar esta ventana)
        current_window = QWidget()
        label = QLabel("Contenido del dashboard va aquí")
        current_window.layout = QVBoxLayout()
        current_window.layout.addWidget(label)
        current_window.setLayout(current_window.layout)
        self.stacked_widget.addWidget(current_window)

        # Agrega botones en la parte superior
        button_ingresar = QPushButton("Ingresar")
        button_mostrar = QPushButton("Mostrar")
        button_cerrar_sesion = QPushButton("Cerrar Sesión")

        layout.addWidget(button_ingresar)
        layout.addWidget(button_mostrar)
        layout.addWidget(button_cerrar_sesion)
        layout.addWidget(self.stacked_widget)

        # Conecta el botón "Ingresar" para cambiar a la ventana de Excel
        button_ingresar.clicked.connect(self.show_excel_window)

        # Establece el diseño en el widget central
        central_widget.setLayout(layout)

    def show_excel_window(self):
        # Cambia a la ventana de Excel
        excel_window = ExcelEditorApp()
        self.stacked_widget.addWidget(excel_window)
        self.stacked_widget.setCurrentWidget(excel_window)

def main():
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

