import psycopg2

class DBconnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.status = "Not Started"

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.status = "Connected"
            return True
        except Exception as ex:
            self.status = f"Error: {ex}"
            return False

    def close(self):
        if self.connection:
            self.connection.close()
          

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

    def getStatus(self):
        return self.status