from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from loginUi import Ui_LoginWindow
from home import MainWindow

class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__()
        self.loginForm = Ui_LoginWindow()
        self.mainForm=MainWindow()
        self.loginForm.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.loginForm.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.loginForm.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.loginForm.loginBtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.loginForm.loginBtn.clicked.connect(self.loginBtn_clicked)


    def loginBtn_clicked(self):
        uName=self.loginForm.userNameTxt.text()
        uPassword=self.loginForm.passwordTxt.text()
        if uName=="admin" and uPassword=="admin":
            self.close()
            self.mainForm.show()
            
      

        
    

"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=LoginWindow()
    window.show()
    sys.exit(app.exec_())
"""