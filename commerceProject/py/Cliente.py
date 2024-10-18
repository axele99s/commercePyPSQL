from py.Persona import Persona

class Cliente(Persona):
    def __init__(self,idCliente,idPersona,nombre,apellido,dni,tipoDNI,idLocalidad,codigoCliente):
        super().__init__(idPersona,nombre,apellido,dni,tipoDNI,idLocalidad)
        self.codigoCliente = codigoCliente
        self.idCliente = idCliente

    def getCodigoCliente(self):
        return self.codigoCliente

    def getIDCliente(self):
        return self.idCliente

