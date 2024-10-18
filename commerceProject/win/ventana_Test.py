# win/ventana_Test.py

from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QTableWidget, QTableWidgetItem

class VentanaPrueba(QWidget):
    def __init__(self, personas):
        super().__init__()  # Llama al constructor de la clase base
        self.personas = personas  # Guarda la lista de instancias de Persona
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 400, 300)  # Ajusta el tamaño si es necesario
        self.setWindowTitle('Test')

        # Crea un QGridLayout
        layout = QGridLayout()

        # Crea una etiqueta y la añade al layout
        etiqueta_personas = QLabel("Personas:")
        layout.addWidget(etiqueta_personas, 0, 0)  # Fila 0, Columna 0

        # Crea un QTableWidget para mostrar los nombres y apellidos
        self.tabla_personas = QTableWidget()
        self.tabla_personas.setColumnCount(2)  # Dos columnas: Nombres y Apellidos
        #self.tabla_personas.setHorizontalHeaderLabels(["Nombres", "Apellidos"])  # Encabezados

        # Cargar los nombres y apellidos en la tabla
        self.cargar_personas()

        layout.addWidget(self.tabla_personas, 1, 0)  # Fila 1, Columna 0

        # Establece el layout en la ventana
        self.setLayout(layout)

        self.show()

    def cargar_personas(self):
        # Limpia la tabla antes de cargar nuevos datos
        self.tabla_personas.setRowCount(0)  # Resetea las filas

        # Agrega los nombres y apellidos de cada Persona a la tabla
        for persona in self.personas:
            fila = self.tabla_personas.rowCount()  # Obtiene la fila actual
            self.tabla_personas.insertRow(fila)  # Inserta una nueva fila

            # Agrega el nombre y apellido a la fila
            self.tabla_personas.setItem(fila, 0, QTableWidgetItem(persona.getNombre()))  # Columna de nombres
            self.tabla_personas.setItem(fila, 1, QTableWidgetItem(persona.getApellido()))  # Columna de apellidos
