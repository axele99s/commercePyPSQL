class Producto:
    def __init__(self, idProducto, idCategoria, idMarca, descripcion, codigo, precio):
        self.idProducto = idProducto
        self.idCategoria = idCategoria
        self.idMarca = idMarca
        self.descripcion = descripcion
        self.codigo = codigo
        self.precio = precio

    def getPrecio(self):
        return self.precio

    def getCodigo(self):
        return self.codigo

    def getDescripcion(self):
        return self.descripcion

    def getCategoria(self):
        return self.idCategoria

    def getMarca(self):
        return self.idMarca