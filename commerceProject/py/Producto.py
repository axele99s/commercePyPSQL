class Producto:
    def __init__(self, idProducto, idCategoria, idMarca, descripcion, codigo, precio,estado):
        self.idProducto = idProducto
        self.idCategoria = idCategoria
        self.idMarca = idMarca
        self.descripcion = descripcion
        self.codigo = codigo
        self.precio = precio
        self.estado : bool = estado

    def getID(self):
        return self.idProducto
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
    def getEstado(self):
        return self.estado

    def cambiarEstado(self):
        self.estado = not self.estado

    def __str__(self):
        return f"Producto(ID: {self.idProducto}, Descripción: {self.descripcion}, Precio: {self.precio}, Estado: {self.estado})"
