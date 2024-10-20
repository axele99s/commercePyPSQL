class login:
    def __init__(self,idlogin,idpersona,username,password,rol):
        self.idlogin = -1
        self.idpersona = -1
        self.username = ''
        self.password = ''
        self.rol = ''
    def getID(self):
        return self.idlogin

    def getUser(self):
        return self.username
    def getPassword(self):
        return self.password