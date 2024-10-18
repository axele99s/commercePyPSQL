class Categoria:
    def __init__(self, idCategoria, descripcion, codigo):
        self.idCategoria = idCategoria
        self.descripcion = descripcion
        self.codigo = codigo

    def __str__(self):
        return f"Categoría: {self.descripcion} (Código: {self.codigo})"
