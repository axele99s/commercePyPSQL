class Marca:
    def __init__(self, idMarca, descripcion, codigo):
        self.idMarca = idMarca
        self.descripcion = descripcion
        self.codigo = codigo

    def __str__(self):
        return f"Marca: {self.descripcion} (Código: {self.codigo})"
