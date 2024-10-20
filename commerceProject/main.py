import sys
from PyQt6.QtWidgets import QApplication
from db.clienteDB import clienteDB
from db.empleadoDB import empleadoDB
from db.personaDB import PersonaDB
from py.Cliente import Cliente
from py.Empleado import Empleado
from py.Persona import Persona
from win.ventana_Test import VentanaPrueba
from db.loginDB import loginDB
from db.DBconnection import DBconnection
from win.wLogin import wLogin



if __name__ == '__main__':
    dbCon = DBconnection("localhost", "postgres", "1234", "commerce")
    dbCon.connect()
    loginn = loginDB(dbCon)



    app = QApplication(sys.argv)
    window = wLogin(loginn)  # Crear una instancia de la clase wLogin
    window.show()
    sys.exit(app.exec())

"""
if __name__ == '__main__':
    # Crear una instancia de DBconnection
    DBCon = DBconnection("localhost", "postgres", "1234", "commerce")

    # Conectar a la base de datos
    DBCon.connect() # Estoy ASUMIENDO que si me conecto (deberia ser un if <--- cambiar)

    # me conecto a la logica de personas de la base de datos
    per_LogicaDB = PersonaDB(DBCon)

    # Cargo las personas
    personas : list[Persona] = per_LogicaDB.cargar_personas()

    # Imprimir los nombres de las personas cargadas
    for persona in personas:
        print(persona.verID())

    #nueva_persona = Persona(idPersona=None,idLocalidad=1, nombre="Steve", apellido="Jobs", dni="123456", tipoDNI=1)
    #per_LogicaDB.agregarPersona(nueva_persona)

    # Cerrar la conexión al final

    clientesDb = clienteDB(DBCon)
    clientes: list[Cliente] = clientesDb.cargarClientes()
    for cliente in clientes:
        print(cliente.getNombre())


    empleadoDb = empleadoDB(DBCon)
    empleados : list[Empleado] = empleadoDb.cargarEmpleados()
    for empleado in empleados:
        print(empleado.getNombre())

    app = QApplication(sys.argv)
    DBCon.close()
    ventana = VentanaPrueba(personas)  # Instancia la clase VentanaPrueba
    sys.exit(app.exec())"""