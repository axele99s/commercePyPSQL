import psycopg2

class DBconnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa.")
            return True
        except Exception as ex:
            print(f"Error al conectar a la base de datos: {ex}")
            return False

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    def cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            raise Exception("No hay conexión a la base de datos.")

    def commit(self):
        if self.connection:
            self.connection.commit()
        else:
            raise Exception("No hay conexión a la base de datos para hacer commit.")

    def rollback(self):
        if self.connection:
            self.connection.rollback()
        else:
            raise Exception("No hay conexión a la base de datos para hacer rollback.")