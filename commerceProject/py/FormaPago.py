class FormaPago:
    def __init__(self, idFormaPago, codigo, descripcion):
        self.idFormaPago = idFormaPago
        self.codigo = codigo
        self.descripcion = descripcion

    def __str__(self):
        return f"Forma de Pago: {self.descripcion} (Código: {self.codigo})"
