class Factura:
    def __init__(self, idFactura, idEmpleado, idCliente, fecha, idFormaPago):
        self.idFactura = idFactura
        self.idEmpleado = idEmpleado
        self.idCliente = idCliente
        self.fecha = fecha
        self.idFormaPago = idFormaPago

    def __str__(self):
        return f"Factura ID: {self.idFactura} (Fecha: {self.fecha}, Empleado: {self.idEmpleado}, Cliente: {self.idCliente})"
