class Producto:
    def __init__(self, idProducto, idCategoria, idMarca, descripcion, codigo, precio):
        self.idProducto = idProducto
        self.idCategoria = idCategoria
        self.idMarca = idMarca
        self.descripcion = descripcion
        self.codigo = codigo
        self.precio = precio

    def __str__(self):
        return "Producto: {self.descripcion} (Código: {self.codigo}, Precio: {self.precio})"
