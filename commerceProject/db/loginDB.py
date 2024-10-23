from py.Login import login

class loginDB:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.log: Login = None

    def validarLogin(self, username, password):
        cursor = self.db_connection.cursor()

        query = """
                SELECT login_id, persona_id, username, password_hash, rol 
                FROM login 
                WHERE username = %s AND password_hash = crypt(%s, password_hash);
        """

        cursor.execute(query, (username, password))

        log = cursor.fetchone()

        # Si el log "existe", entonces me guardo los datos.
        if log:
            idlogin, idpersona, username, hashpassword, rol = log
            self.log = login(idlogin, idpersona, username, hashpassword, rol)
            cursor.close()
            return True

        #cursor.close()
        return False  # Retornar False si no encuentra al usuario

    def verUsuario(self):
        return self.log


    def vercON(self):
        return self.db_connection

    def verCon(self):

        return self.db_connection

