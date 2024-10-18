class Provincia:
    def __init__(self, idProvincia, codigoProvincia, nombreProvincia):
        self.idProvincia = idProvincia
        self.codigoProvincia = codigoProvincia
        self.nombreProvincia = nombreProvincia

    def __str__(self):
        return f"Provincia: {self.nombreProvincia} (Código: {self.codigoProvincia})"
