import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QImage, QPixmap
import fitz  # PyMuPDF

class PDFViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("PDF Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QGraphicsView(self)
        self.setCentralWidget(self.central_widget)

        self.scene = QGraphicsScene()
        self.central_widget.setScene(self.scene)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_file_action = file_menu.addAction("Open PDF")
        open_file_action.triggered.connect(self.openPDF)

    def openPDF(self):
        options = QFileDialog.options()
        options |= QFileDialog.ReadOnly

        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf);;All Files (*)", options=options)

        if file_path:
            self.displayPDF(file_path)

    def displayPDF(self, file_path):
        pdf_document = fitz.open(file_path)

        page = pdf_document.load_page(0)  # Cargar la primera página

        # Convertir la página PDF a una imagen
        image = page.get_pixmap()

        # Crear una imagen QImage desde la imagen de PyMuPDF
        qt_image = QImage(image.samples, image.width, image.height, image.stride, QImage.Format.Format_RGBA8888)

        # Mostrar la imagen en el QGraphicsView
        pixmap = QPixmap.fromImage(qt_image)
        self.scene.clear()
        self.scene.addPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = PDFViewer()
    viewer.show()
    sys.exit(app.exec())