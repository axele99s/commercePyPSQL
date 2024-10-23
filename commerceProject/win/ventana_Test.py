
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
class ventana_Test(QWidget):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle('Error')
        layout = QVBoxLayout()
        error_label = QLabel(message)
        layout.addWidget(error_label)
        self.setLayout(layout)





