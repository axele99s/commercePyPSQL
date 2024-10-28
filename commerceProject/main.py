import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget

from db.loginDB import loginDB
from win.wLogin import wLogin
from win.wPrincipalEmpleados import principalEmpleados
from db.DBconnection import DBconnection
from db.productoDB import productoDB
from win.wErrores import ventanaError

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Configurar la conexión a la base de datos
    DBCon = DBconnection("ep-snowy-heart-a4ie70mb.us-east-1.aws.neon.tech",
                         "commerceDB_owner",
                         "xiq1v5mAYIpC",
                         "commerceDB")
    result = DBCon.connect()

    if DBCon.connect():

        base_productos = productoDB(DBCon)
        loginn = loginDB(DBCon)

        # Crear la ventana de inicio de sesión
        login_window = wLogin(loginn)

        # Variable para mantener la referencia a la ventana de empleados
        empleados_window = principalEmpleados(base_productos)

        # Conectar la señal a la función que muestra la ventana de empleados
        login_window.login_successful.connect(empleados_window.show)

        login_window.show()
    else:
        # Cambia esto para pasar un mensaje de error
        error_window = ventanaError(DBCon.getStatus())
        error_window.show()

    sys.exit(app.exec())