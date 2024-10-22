import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from db.loginDB import loginDB

class wLogin(QWidget):
    def __init__(self,loginn : loginDB = None):
        super().__init__()

        self.loginn = loginn
        self.setWindowTitle('Iniciar Sesion')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        # Etiqueta y campo de texto para el nombre de usuario
        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        # Etiqueta y campo de texto para la contraseña
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Ocultar la contraseña
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Botón de inicio de sesión
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.check_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        logeo = self.loginn.validarLogin(username, password)
        if logeo:
            QMessageBox.information(self, 'Inicio de sesion', 'Sesion iniciada correctamente!')
            self.close()
        else:
            QMessageBox.warning(self, 'Error', 'Verificar usuario o contraseña.')



