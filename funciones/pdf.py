import sys
import fitz  # PyMuPDF
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog

class PDFViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("PDF Viewer and Text Cleaner")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.load_button = QPushButton("Cargar PDF", self)
        self.load_button.clicked.connect(self.load_pdf)

        self.clean_button = QPushButton("Limpiar", self)
        self.clean_button.clicked.connect(self.clean_text)

        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.clean_button)
        layout.addWidget(self.text_edit)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def load_pdf(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir PDF", "", "Archivos PDF (*.pdf);;Todos los archivos (*)")
        if file_name:
            pdf_document = fitz.open(file_name)
            text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
            self.text_edit.setPlainText(text)

    def clean_text(self):
        text = self.text_edit.toPlainText()
        cleaned_text = self.replace_special_characters(text)
        self.text_edit.setPlainText(cleaned_text)

    def replace_special_characters(self, text):
        # Aquí puedes definir las reglas de reemplazo de caracteres especiales
        replacements = {
            'á': 'a',
            'é': 'e',
            'í': 'i',
            'ó': 'o',
            'ú': 'u',
            # Agrega más reglas aquí según tus necesidades
        }
        cleaned_text = text
        for char, replacement in replacements.items():
            cleaned_text = cleaned_text.replace(char, replacement)
        return cleaned_text

def main():
    app = QApplication(sys.argv)
    window = PDFViewerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
