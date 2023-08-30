"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: danie(mitchel.dmch@gmail.com) 
ingresar.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  samedi 26 août 2023 à 18:21:39 
Dernière modification : mardi 29 août 2023 à 20:16:58
"""
import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget

class ExcelLoaderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excel File Loader")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("No se ha cargado ningún archivo.")
        self.layout.addWidget(self.label)

        self.load_button = QPushButton("Cargar Archivo Excel")
        self.load_button.clicked.connect(self.load_excel_file)
        self.layout.addWidget(self.load_button)

        self.central_widget.setLayout(self.layout)

    def load_excel_file(self):
        file_dialog = QFileDialog()
        file_dialog.setOptions(QFileDialog.ReadOnly)
        file_path, _ = file_dialog.getOpenFileName(self, "Cargar Archivo Excel", "", "Archivos Excel (*.xls *.xlsx);;Todos los archivos (*)")

        if file_path:
            try:
                df = pd.read_excel(file_path) 
                self.label.setText(f"Archivo cargado: {os.path.basename(file_path)}")
            except Exception as e:
                self.label.setText(f"Error al cargar el archivo: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExcelLoaderApp()
    window.show()
    sys.exit(app.exec())
