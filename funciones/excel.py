"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: danie(mitchel.dmch@gmail.com) 
prueba.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  mardi 29 août 2023 à 21:01:46 
Dernière modification : mardi 29 août 2023 à 21:31:00
"""

import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, QFileDialog

class ExcelEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Excel Editor App')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        filter_layout = QHBoxLayout()
        self.filter_column_label = QLabel("Filter by Column:")
        self.filter_column_combo = QComboBox()
        self.filter_column_combo.currentTextChanged.connect(self.apply_filter)
        self.filter_value_label = QLabel("Filter Value:")
        self.filter_value_input = QLineEdit()
        self.filter_button = QPushButton("Apply Filter")
        self.filter_button.clicked.connect(self.apply_filter)

        filter_layout.addWidget(self.filter_column_label)
        filter_layout.addWidget(self.filter_column_combo)
        filter_layout.addWidget(self.filter_value_label)
        filter_layout.addWidget(self.filter_value_input)
        filter_layout.addWidget(self.filter_button)

        self.table_widget = QTableWidget()
        self.layout.addLayout(filter_layout)
        self.layout.addWidget(self.table_widget)

        self.load_button = QPushButton('Load Excel')
        self.load_button.clicked.connect(self.load_excel)
        self.layout.addWidget(self.load_button)

        self.save_button = QPushButton('Save Changes')
        self.save_button.clicked.connect(self.save_changes)
        self.layout.addWidget(self.save_button)

        self.central_widget.setLayout(self.layout)

        self.loaded_data = None

    def load_excel(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx)")

        if file_path:
            self.loaded_data = pd.read_excel(file_path)
            self.populate_table()
            self.populate_filter_columns()

    def populate_table(self):
        if self.loaded_data is not None:
            self.table_widget.setRowCount(self.loaded_data.shape[0])
            self.table_widget.setColumnCount(self.loaded_data.shape[1])

            for row in range(self.loaded_data.shape[0]):
                for col in range(self.loaded_data.shape[1]):
                    item = QTableWidgetItem(str(self.loaded_data.iat[row, col]))
                    self.table_widget.setItem(row, col, item)

    def populate_filter_columns(self):
        if self.loaded_data is not None:
            self.filter_column_combo.clear()
            self.filter_column_combo.addItems(self.loaded_data.columns)

    def apply_filter(self):
        if self.loaded_data is not None:
            column = self.filter_column_combo.currentText()
            value = self.filter_value_input.text()
            
            if column and value:
                filtered_data = self.loaded_data[self.loaded_data[column] == value]
                self.populate_table_with_filtered_data(filtered_data)
            else:
                self.populate_table()

    def populate_table_with_filtered_data(self, data):
        self.table_widget.setRowCount(data.shape[0])
        self.table_widget.setColumnCount(data.shape[1])

        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                item = QTableWidgetItem(str(data.iat[row, col]))
                self.table_widget.setItem(row, col, item)

    def save_changes(self):
        if self.loaded_data is not None:
            for row in range(self.loaded_data.shape[0]):
                for col in range(self.loaded_data.shape[1]):
                    item = self.table_widget.item(row, col)
                    if item is not None:
                        self.loaded_data.iat[row, col] = item.text()

            self.loaded_data.to_excel('edited_data.xlsx', index=False)
            print("Changes saved to edited_data.xlsx")

def main():
    app = QApplication(sys.argv)
    excel_editor = ExcelEditorApp()
    excel_editor.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()