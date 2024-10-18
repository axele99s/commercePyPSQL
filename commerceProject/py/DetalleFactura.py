class DetalleFactura:
    def __init__(self, idFactura, idProducto, cantidad, precioUnitario):
        self.idFactura = idFactura
        self.idProducto = idProducto
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario

    def __str__(self):
        return f"Detalle Factura - Producto: {self.idProducto}, Cantidad: {self.cantidad}, Precio Unitario: {self.precioUnitario}"
