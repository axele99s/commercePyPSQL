from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QPushButton, QLineEdit, QHBoxLayout, QLabel, QHeaderView, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from py.Producto import Producto
from win.menuPrincipalEmpleado.wAgregarProducto import wAgregarProducto
from db.productoDB import productoDB

class gestionProductos(QWidget):

    def __init__(self, db_prods : productoDB = None):
        super().__init__()
        self.db_prods = db_prods
        self.lista_productos = self.db_prods.getProductos()  # Guardar la lista de productos
        self.setLayout(QVBoxLayout())  # Establecer layout principal

        # Llamar a ventanaProducto para crear la interfaz antes de cargar productos
        self.ventanaBuscar()  # Contiene la ventana que incluye agregarProd , editar, eliminar, el buscador
        self.ventanaProductos() # Solo contiene las filas y columnas de los productos
        self.ventanasExtras()

        # Cargar los productos después de que la tabla ha sido creada
        self.cargarProductos()


    # Ventana general, aca se carga la grilla y demas...
    def ventanaProductos(self):
        # Inicializa el modelo y la vista de productos
        self.product_table = QTableView()  # Cambiar a QTableView
        self.model = QStandardItemModel(0, 3)  # 0 filas, 3 columnas
        self.model.setHorizontalHeaderLabels(['ID','Codigo', 'Nombre', 'Precio', 'Estado'])  # Encabezados de la tabla

        # Configurar el QTableView
        self.product_table.setModel(self.model)
        self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # Ajustar columnas al tamaño

        self.product_table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows) # Se selecciona la fila completa
        self.product_table.setSelectionMode(QTableView.SelectionMode.SingleSelection) # solo se selecciona una fila a la vez

        # Añadir los layouts y la tabla al layout principal

        self.layout().addWidget(self.product_table)  # Añadir la tabla



        # Establecer que las celdas no sean editables
        self.product_table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)



    def cargarProductos(self):
        self.model.setRowCount(0)  # Limpiar la tabla antes de cargar nuevos productos

        # Cargar productos en la tabla
        for producto in self.lista_productos:
            row_position = self.model.rowCount()

            # Crear los items y establecer los flags
            item_id = QStandardItem(str(producto.getID()))
            item_id.setFlags(
                Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Solo seleccionable, no editable

            item_cod = QStandardItem(str(producto.getCodigo()))
            item_cod.setFlags(
                Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Solo seleccionable, no editable

            item_nombre = QStandardItem(producto.getDescripcion())
            item_nombre.setFlags(
                Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Solo seleccionable, no editable

            item_precio = QStandardItem(str(producto.getPrecio()))
            item_precio.setFlags(
                Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Solo seleccionable, no editable

            item_estado = QStandardItem(str(producto.getEstado()))
            item_estado.setFlags(
                Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Solo seleccionable, no editable
            # Añadir los items al modelo
            self.model.appendRow([item_id,item_cod, item_nombre, item_precio,item_estado])

    def ventanaBuscar(self):
        # Crear el layout para la búsqueda
        search_layout = QHBoxLayout()
        self.product_search = QLineEdit()  # Campo de búsqueda

        search_button = QPushButton('Buscar')  # Botón de búsqueda
        search_layout.addWidget(QLabel('Buscar Producto:'))  # Etiqueta de búsqueda
        search_layout.addWidget(self.product_search)  # Añadir el campo de búsqueda
        search_layout.addWidget(search_button)  # Añadir el botón de búsqueda
        self.layout().addLayout(search_layout)  # Añadir el layout de búsqueda
        """Falta la logica !!!!!! """


    def ventanasExtras(self):
        # Crear el layout para gestionar productos
        manage_layout = QHBoxLayout()
        agregar_producto = QPushButton('Agregar Producto')  # Botón para agregar
        agregar_producto.clicked.connect(self.agregarProducto)
        boton_editar = QPushButton('Editar ')  # Botón para editar
        boton_eliminar = QPushButton('Deslistar Producto')  # Botón para eliminar
        manage_layout.addWidget(agregar_producto)  # Añadir botón de agregar
        manage_layout.addWidget(boton_editar)  # Añadir botón de editar
        manage_layout.addWidget(boton_eliminar)  # Añadir botón de
        boton_eliminar.clicked.connect(self.cambiarEstado)
        self.layout().addLayout(manage_layout)  # Añadir el layout de gestión

    def agregarProducto(self):
        ventana_agregar = wAgregarProducto(self, self.db_prods)
        ventana_agregar.exec()


    def cambiarEstado(self):
        index = self.product_table.selectionModel().currentIndex()  # obtengo la fila en la que estoy
        row = index.row() #numero de la fila
        id_producto = int(self.model.item(row, 0).text())





        producto = self.db_prods.verProducto(id_producto)
        print(producto)
        producto.cambiarEstado()



        err = self.db_prods.cambiarEstado(id_producto, producto.getEstado())

        nuevo_estado = ""
        if producto.getEstado() is True:
            nuevo_estado = "Activado"
        else:
            nuevo_estado = "Desactivado"

        if err is None:
            QMessageBox.information(self, "Éxito", f"Producto {nuevo_estado} exitosamente.")
            self.cargarProductos()
        else:
            QMessageBox.critical(self, "Error", f"No se pudo {nuevo_estado} el producto: {err}")



