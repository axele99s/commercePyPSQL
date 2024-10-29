from PyQt6.QtWidgets import QVBoxLayout,QHBoxLayout, QLineEdit, QPushButton, QDialog, QLabel, QComboBox,QMessageBox

from py.Producto import Producto
from db.productoDB import productoDB

class wAgregarProducto(QDialog):
    def __init__(self, parent=None,db_prods : productoDB = None): # Falta pasarle la base de marca y la base de categoria.. SI O SI
        super().__init__(parent)

        self.db_prods = db_prods
        self.setWindowTitle('Agregar Producto')
        self.setGeometry(500, 500, 500, 500)

        # Crear el layout principal
        layout_principal = QVBoxLayout()

        # Agregar el layout de labels e inputs
        layout_principal.addLayout(self.cargarLabelsInputs())

        # Agregar el layout de botones
        layout_principal.addLayout(self.cargarBotones())

        # Establecer el layout principal
        self.setLayout(layout_principal)





    def cargarLabelsInputs(self):
        # Crear el layout para la ventana
        layout = QVBoxLayout()

        # Labels e Inputs
        self.nombre_label = QLabel("Nombre del Producto")
        self.nombre_input = QLineEdit()

        self.categ_label = QLabel("Categoria:")

        self.categ_input = QComboBox()
        self.categ_input.addItems(["Producto", "Servicio"])

        self.marca_label = QLabel("Marca:")
        self.marca_input = QComboBox()
        self.marca_input.addItems(["Samsung", "LGo"])


        self.desc_label = QLabel("Descripcion:")
        self.desc_input = QLineEdit()

        self.cod_label = QLabel("Codigo:")
        self.cod_input = QLineEdit()


        self.precio_label = QLabel("Precio:")
        self.precio_input = QLineEdit()




        # Añadir widgets al layout
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.categ_label)
        layout.addWidget(self.categ_input)
        layout.addWidget(self.marca_label)
        layout.addWidget(self.marca_input)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.desc_input)
        layout.addWidget(self.cod_label)
        layout.addWidget(self.cod_input)
        layout.addWidget(self.precio_label)
        layout.addWidget(self.precio_input)

        # Configurar el layout principal
        return layout


    def cargarBotones(self):
        botones = QHBoxLayout()

        boton_confirmar = QPushButton('Confirmar')
        boton_confirmar.clicked.connect(self.agregarABase)

        boton_cancelar = QPushButton('Cancelar')
        boton_cancelar.clicked.connect(self.reject)

        botones.addWidget(boton_confirmar)
        botones.addWidget(boton_cancelar)

        return botones



    def agregarABase(self):
        # Crear una instancia del producto con los datos del formulario

        producto = Producto(
            None,  # es auto-incremental
            self.categ_input.currentIndex() + 1,
            self.marca_input.currentIndex() + 1,
            self.desc_input.text(),
            int(self.cod_input.text()),  # Convertir a entero
            float(self.precio_input.text())  # Convertir precio a float
        )

        # Intentar agregar el producto a la base de datos
        error = self.db_prods.agregarProducto(producto)

        if error:  # Si hubo un error al agregar el producto
            # Mostrar un mensaje de error en una ventana emergente
            QMessageBox.critical(self, "Error", f"No se pudo agregar el producto: {error}")
        else:
            # Mostrar un mensaje de éxito antes de cerrar el diálogo
            QMessageBox.information(self, "Éxito", "Producto agregado exitosamente.")
            self.accept()  # Cerrar el diálogo con éxito




