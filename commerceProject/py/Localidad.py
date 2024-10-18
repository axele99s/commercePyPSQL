class Localidad:
    def __init__(self, idLocalidad, codigoLocalidad, nombreLocalidad, idProvincia):
        self.idLocalidad = idLocalidad
        self.codigoLocalidad = codigoLocalidad
        self.nombreLocalidad = nombreLocalidad
        self.idProvincia = idProvincia

    def __str__(self):
        return f"Localidad: {self.nombreLocalidad} (Código: {self.codigoLocalidad})"
