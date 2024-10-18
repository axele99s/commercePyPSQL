from py.Empleado import Empleado
class empleadoDB:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def cargarEmpleados(self):
        cursor = self.db_connection.cursor()
        query = ("""
                    SELECT e.idEmpleado, e.codigoEmpleado, p.idPersona, p.nombre, p.apellido, p.dni, p.tipoDNI, p.idLocalidad
                    FROM empleado e
                    JOIN persona p ON e.idPersona = p.idPersona 
                    """)
        cursor.execute(query)
        rows = cursor.fetchall()

        empleados : list[Empleado] = []

        for row in rows:
            idEmpleado, codigoEmpleado, idPersona, nombre, apellido, dni, tipoDNI, idLocalidad = row
            empleado = Empleado(idEmpleado, idPersona, nombre, apellido, dni, tipoDNI, idLocalidad, codigoEmpleado)
            empleados.append(empleado)

        cursor.close()
        return empleados