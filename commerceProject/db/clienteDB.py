from py.Cliente import Cliente


class clienteDB:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def cargarClientes(self):
        cursor = self.db_connection.cursor()
        query = ("""SELECT c.idCliente, c.codigoCliente, p.idPersona, p.nombre, p.apellido, p.dni, p.tipoDNI, p.idLocalidad
                    FROM cliente c
                    JOIN persona p ON c.idPersona = p.idPersona""")
        cursor.execute(query)
        rows = cursor.fetchall()

        clientes : list[Cliente] = []
        for row in rows:
            idCliente, codigoCliente, idPersona, nombre, apellido, dni, tipoDNI, idLocalidad = row
            cliente = Cliente(idCliente, idPersona, nombre, apellido, dni, tipoDNI, idLocalidad, codigoCliente)
            clientes.append(cliente)

        cursor.close()
        return clientes
