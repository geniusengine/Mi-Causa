"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: danie(mitchel.dmch@gmail.com) 
menucrud.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  samedi 26 août 2023 à 18:42:51 
Dernière modification : samedi 26 août 2023 à 18:42:55
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar

class MenuExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menú de Funciones")

        menubar = self.menuBar()
        file_menu = menubar.addMenu("Funciones")

        show_action = QAction("Mostrar Información", self)
        show_action.triggered.connect(self.show_info)
        file_menu.addAction(show_action)

    def show_info(self):
        info_window = InfoDisplayApp()
        info_window.show()

class InfoDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mostrar Información")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Aquí se mostraría la información")
        self.layout.addWidget(self.label)

        self.central_widget.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuExample()
    window.show()
    sys.exit(app.exec())
