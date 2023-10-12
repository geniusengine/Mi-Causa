"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: danie(danie.pro@gmail.com) 
estoycansadojefe.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  jeudi 12 octobre 2023 à 2:18:36 
Dernière modification : jeudi 12 octobre 2023 à 2:19:14
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QWidget, QVBoxLayout
import mysql.connector
from docx import Document

class DocumentListApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lista de Documentos de Word")
        self.setGeometry(100, 100, 400, 300)

        self.document_list = QListWidget(self)
        self.document_list.itemDoubleClicked.connect(self.open_document)

        layout = QVBoxLayout()
        layout.addWidget(self.document_list)

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

        # Cargar la lista de documentos desde la base de datos
        self.load_documents()

    def load_documents(self):
        cursor = self.db.cursor()
        select_query = "SELECT id, nombre_documento FROM documentos_word"
        cursor.execute(select_query)
        documents = cursor.fetchall()
        for document in documents:
            id, nombre = document
            self.document_list.addItem(f"{id}: {nombre}")
        cursor.close()

    def open_document(self, item):
        selected_item = item.text()
        document_id = int(selected_item.split(':')[0])
        cursor = self.db.cursor()
        select_query = "SELECT nombre_documento, contenido FROM documentos_word WHERE id = %s"
        cursor.execute(select_query, (document_id,))
        document = cursor.fetchone()
        if document:
            nombre_documento, contenido = document
            doc = Document()
            doc.add_paragraph(contenido)
            # Puedes abrir una nueva ventana o utilizar una librería para editar el documento, como python-docx

def main():
    app = QApplication(sys.argv)
    window = DocumentListApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

