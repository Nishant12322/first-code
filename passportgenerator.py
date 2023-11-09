import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import string
import secrets


class PasswordGeneratorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 400, 200)

        self.label = QtWidgets.QLabel('Generated Password:', self)
        self.label.setGeometry(20, 20, 200, 30)

        self.password_display = QtWidgets.QLineEdit(self)
        self.password_display.setGeometry(20, 50, 360, 30)
        self.password_display.setReadOnly(True)

        self.generate_button = QtWidgets.QPushButton('Generate New', self)
        self.generate_button.setGeometry(20, 90, 150, 30)
        self.generate_button.clicked.connect(self.generate_password)

        self.copy_button = QtWidgets.QPushButton('Copy', self)
        self.copy_button.setGeometry(230, 90, 150, 30)
        self.copy_button.clicked.connect(self.copy_password)

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for i in range(12))
        self.password_display.setText(password)

    def copy_password(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.password_display.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = PasswordGeneratorApp()
    ex.show()
    sys.exit(app.exec_())
