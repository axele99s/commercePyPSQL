from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QPushButton, QLineEdit, QHBoxLayout, QLabel, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from py.Producto import Producto

class gestionProductos(QWidget):
    def __init__(self, productos):
        super().__init__()
        self.lista_productos = productos  # Guardar la lista de productos
        self.setLayout(QVBoxLayout())  # Establecer layout principal

        # Llamar a ventanaProducto para crear la interfaz antes de cargar productos
        self.ventanaProducto()

        # Cargar los productos después de que la tabla ha sido creada
        self.cargarProductos()

    def ventanaProducto(self):
        # Crear el layout para la búsqueda
        search_layout = QHBoxLayout()
        self.product_search = QLineEdit()  # Campo de búsqueda

        search_button = QPushButton('Buscar')  # Botón de búsqueda
        search_layout.addWidget(QLabel('Buscar Producto:'))  # Etiqueta de búsqueda
        search_layout.addWidget(self.product_search)  # Añadir el campo de búsqueda
        search_layout.addWidget(search_button)  # Añadir el botón de búsqueda

        # Inicializa el modelo y la vista de productos
        self.product_table = QTableView()  # Cambiar a QTableView
        self.model = QStandardItemModel(0, 3)  # 0 filas, 3 columnas
        self.model.setHorizontalHeaderLabels(['Codigo', 'Nombre', 'Precio'])  # Encabezados de la tabla

        # Configurar el QTableView
        self.product_table.setModel(self.model)
        self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # Ajustar columnas al tamaño

        # Crear el layout para gestionar productos
        manage_layout = QHBoxLayout()
        add_button = QPushButton('Agregar Producto')  # Botón para agregar
        edit_button = QPushButton('Editar Producto')  # Botón para editar
        delete_button = QPushButton('Eliminar Producto')  # Botón para eliminar
        manage_layout.addWidget(add_button)  # Añadir botón de agregar
        manage_layout.addWidget(edit_button)  # Añadir botón de editar
        manage_layout.addWidget(delete_button)  # Añadir botón de eliminar

        # Añadir los layouts y la tabla al layout principal
        self.layout().addLayout(search_layout)  # Añadir el layout de búsqueda
        self.layout().addWidget(self.product_table)  # Añadir la tabla
        self.layout().addLayout(manage_layout)  # Añadir el layout de gestión

        # Establecer que las celdas no sean editables
        self.product_table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)

    def cargarProductos(self):
        self.model.setRowCount(0)  # Limpiar la tabla antes de cargar nuevos productos

        # Cargar productos en la tabla
        for producto in self.lista_productos:
            row_position = self.model.rowCount()

            # Crear los items y establecer los flags
            item_id = QStandardItem(str(producto.getCodigo()))
            item_id.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Solo seleccionable, no editable

            item_nombre = QStandardItem(producto.getDescripcion())
            item_nombre.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Solo seleccionable, no editable

            item_precio = QStandardItem(str(producto.getPrecio()))
            item_precio.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Solo seleccionable, no editable

            # Añadir los items al modelo
            self.model.appendRow([item_id, item_nombre, item_precio])
