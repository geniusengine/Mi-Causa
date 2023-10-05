import sys
import os
import openpyxl
import PyPDF2
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QDockWidget, QFileDialog, QTextEdit, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt

class Dashboard(QMainWindow):
    def __init__(self, username):
        super().__init__()

        self.username = username
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 800, 600)

        # Área superior: Nombre de la persona
        top_widget = QWidget()
        top_layout = QVBoxLayout()
        top_layout.addWidget(QLabel(f"Bienvenido, {self.username}"))
        top_widget.setLayout(top_layout)
        self.setMenuWidget(top_widget)

        # Menú lateral con botones
        sidebar_widget = QDockWidget()
        sidebar_widget.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        sidebar_layout = QVBoxLayout()
        sidebar_buttons = []

        ingresar_button = QPushButton("Ingresar")
        mostrar_button = QPushButton("Mostrar")
        cerrar_sesion_button = QPushButton("Cerrar Sesión")

        sidebar_buttons.append(ingresar_button)
        sidebar_buttons.append(mostrar_button)
        sidebar_buttons.append(cerrar_sesion_button)

        for button in sidebar_buttons:
            sidebar_layout.addWidget(button)

        sidebar_widget.setWidget(QWidget(self))
        sidebar_widget.widget().setLayout(sidebar_layout)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, sidebar_widget)

        # Área central
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        # Elementos para la carga de archivos
        upload_button = QPushButton("Cargar Archivos")
        upload_button.clicked.connect(self.upload_files)
        central_layout.addWidget(upload_button)
        self.uploaded_files = []  # Lista para almacenar rutas de archivos cargados

        # Botón para elegir entre Excel y PDF
        choose_type_button = QPushButton("Elegir Tipo de Archivo")
        choose_type_button.setVisible(False)
        choose_type_button.clicked.connect(self.choose_file_type)
        central_layout.addWidget(choose_type_button)

        # TextEdit para mostrar la información
        text_edit = QTextEdit()
        central_layout.addWidget(text_edit)
        
        # Botón para volver desde la vista de archivo a la lista
        back_button = QPushButton("Volver a la Lista")
        back_button.setVisible(False)
        back_button.clicked.connect(self.show_ingresar)  # Volver al estado de ingreso
        central_layout.addWidget(back_button)

        # Lista de archivos
        file_list = QListWidget()
        file_list.itemClicked.connect(self.show_file_info)
        file_list.setVisible(False)
        central_layout.addWidget(file_list)

    def show_ingresar(self):
        self.upload_button.setVisible(True)
        self.choose_type_button.setVisible(True)
        self.text_edit.clear()
        self.show_widget(self.upload_button)
        self.show_widget(self.choose_type_button)
        self.hide_widget(self.text_edit)
        self.hide_widget(self.back_button)
        self.uploaded_files.clear()
        self.selected_file_path = None

    def show_mostrar(self):
        self.text_edit.clear()
        self.show_widget(self.text_edit)
        self.show_widget(self.back_button)
        self.hide_widget(self.upload_button)
        self.hide_widget(self.choose_type_button)
        self.show_file_list()

    def upload_files(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivos", "", "Excel Files (*.xlsx);;PDF Files (*.pdf)")
        self.uploaded_files.extend(file_paths)

    def choose_file_type(self):
        # Lógica para elegir entre Excel y PDF
        pass

    def process_pdf(self, pdf_path):
        # Lógica para procesar el archivo PDF (limpiar caracteres, etc.)
        pass

    def process_excel(self, excel_path):
        # Lógica para procesar el archivo Excel y guardar en la base de datos
        pass

    def show_file_list(self):
        self.file_list.clear()
        # Agregar archivos a la lista
        for file_path in self.uploaded_files:
            item = QListWidgetItem(os.path.basename(file_path))
            self.file_list.addItem(item)
        self.file_list.setVisible(True)
        self.back_button.setVisible(True)

    def show_file_info(self, item):
        # Mostrar información del archivo seleccionado
        self.text_edit.clear()
        file_name = item.text()
        file_path = os.path.join(self.uploaded_files, file_name)  # Obtener la ruta completa del archivo
        self.selected_file_path = file_path
        self.text_edit.setPlainText(f"Mostrando archivo: {file_name}\n")
        if file_path.endswith(".pdf"):
            # Lógica para mostrar el contenido de un archivo PDF
            pass
        elif file_path.endswith(".xlsx"):
            # Lógica para mostrar el contenido de un archivo Excel
            pass

    def return_to_login(self):
        self.hide()
        self.login_window = LoginApp()
        self.login_window.show()

    def show_widget(self, widget):
        widget.setVisible(True)

    def hide_widget(self, widget):
        widget.setVisible(False)

def main():
    app = QApplication(sys.argv)
    username = "usuario"  # Supongamos que el usuario "usuario" ha iniciado sesión
    dashboard = Dashboard(username)
    dashboard.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()