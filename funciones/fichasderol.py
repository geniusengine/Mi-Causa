import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
import mysql.connector
from docx import Document

class WordDocumentApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.file_name = None  # Define la variable file_name en el alcance de la clase

    def initUI(self):
        self.setWindowTitle("Word Document Viewer and Saver")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        self.load_button = QPushButton("Cargar Documento de Word", self)
        self.load_button.clicked.connect(self.load_word_doc)

        self.save_button = QPushButton("Guardar en Base de Datos", self)
        self.save_button.clicked.connect(self.save_to_database)

        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.text_edit)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Conexión a la base de datos
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mi_causa"
        )

    def load_word_doc(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Documento de Word", "", "Archivos de Word (*.docx);;Todos los archivos (*)")
        if self.file_name:
            doc = Document(self.file_name)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text
            self.text_edit.setPlainText(text)

    def save_to_database(self):
        if self.file_name is not None:  # Asegúrate de que file_name esté definido
            text = self.text_edit.toPlainText()

            # Insertar el texto en la base de datos
            cursor = self.db.cursor()
            insert_query = "INSERT INTO documentos_word (nombre_documento, contenido) VALUES (%s, %s)"
            archivo_doc = (os.path.basename(self.file_name), text.encode('utf-8'))
            cursor.execute(insert_query, archivo_doc)
            self.db.commit()
            cursor.close()

def main():
    app = QApplication(sys.argv)
    window = WordDocumentApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
