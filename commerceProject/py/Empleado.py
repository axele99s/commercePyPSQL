from py.Persona import Persona

class Empleado(Persona):
    def __init__(self,idEmpleado,idPersona,nombre,apellido,dni,tipoDNI,idLocalidad,codigoEmpleado):
        super().__init__(idPersona,nombre,apellido,dni,tipoDNI,idLocalidad)
        self.codigoEmpleado = codigoEmpleado
        self.idEmpleado = idEmpleado

    def getCodigoEmpleado(self):
        return self.codigoEmpleado

    def getIDEmpleado(self):
        return self.idEmpleado