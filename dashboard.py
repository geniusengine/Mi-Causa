import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QComboBox, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QColor, QBrush
from xlsxwriter import Workbook


class ExcelEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Excel Data Editor")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

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

        layout.addLayout(filter_layout)

        self.table_widget = QTableWidget()
        self.load_data()

        layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    #def load_data(self):
       # workbook = Workbook("data.xlsx")
        #sheet = workbook.active

       # self.table_widget.setRowCount(sheet.max_row)
        #self.table_widget.setColumnCount(sheet.max_column)

        #for col_index, col_letter in enumerate(sheet.iter_cols(min_row=1, max_row=1)):
         #   self.filter_column_combo.addItem(col_letter[0])

        #for row in sheet.iter_rows(values_only=True):
         #   row_index = sheet.iter_rows(values_only=True).index(row)
          #  for col_index, cell_value in enumerate(row):
           #     item = QTableWidgetItem(str(cell_value))
            #    self.table_widget.setItem(row_index, col_index, item)

    #def apply_filter(self):
    #    column_index = self.filter_column_combo.currentIndex()
    #    filter_value = self.filter_value_input.text().lower()
#
    #    for row_index in range(self.table_widget.rowCount()):
    #        item = self.table_widget.item(row_index, column_index)
    #        cell_value = item.text().lower()
#
    #        if filter_value in cell_value:
    #            item.setBackground(QBrush(QColor(255, 255, 255)))
    #        else:
    #            item.setBackground(QBrush(QColor(200, 200, 200)))
#
#
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    mainWindow = ExcelEditor()
#    mainWindow.show()
#    sys.exit(app.exec_())
#