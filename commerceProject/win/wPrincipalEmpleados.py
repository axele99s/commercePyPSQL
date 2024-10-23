""" Ventana principal que veran los empleados  """

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QPushButton
from win.menuPrincipalEmpleado.wGestionProductos import gestionProductos

class principalEmpleados(QWidget):
    def __init__(self, productos):
        super().__init__()
        self.setWindowTitle('Panel de Empleados')

        # Crear el widget de pestañas
        self.tabs = QTabWidget()
        self.tabs.addTab(gestionProductos(productos), 'Productos')  # Agrega la pestaña de productos

        # Crear el botón para volver al login
        self.back_button = QPushButton('Volver al Login')
        self.back_button.clicked.connect(self.volver_al_login)  # Conectar el botón a la función

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        layout.addWidget(self.back_button)  # Agregar el botón al layout

        self.setLayout(layout)

    def volver_al_login(self):
        self.close()  # Cerrar la ventana de empleados
