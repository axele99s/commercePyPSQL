class Persona:
    def __init__(self, idPersona, nombre, apellido, dni, tipoDNI, idLocalidad):
        self.idPersona = idPersona
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipoDNI = tipoDNI
        self.idLocalidad = idLocalidad

    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def verID(self):
        return self.idPersona