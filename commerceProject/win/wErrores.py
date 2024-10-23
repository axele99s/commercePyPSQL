
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
class ventanaError(QWidget):
    def __init__(self, mensaje):
        super().__init__()
        self.setWindowTitle('Error')
        layout = QVBoxLayout()
        error_label = QLabel(mensaje)
        layout.addWidget(error_label)
        self.setLayout(layout)