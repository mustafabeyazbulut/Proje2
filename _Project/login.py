from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,webbrowser

from loginUi import Ui_LoginWindow


class LoginWindow(QWidget):
    def mainLoad (self):
        from home import MainWindow
        self.mainForm=MainWindow()
        self.mainForm.show()

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__()
        self.loginForm = Ui_LoginWindow()
        self.loginForm.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.loginForm.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.loginForm.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.loginForm.loginBtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.loginForm.loginBtn.clicked.connect(self.loginBtn_clicked)
        self.loginForm.twitterBtn.clicked.connect(self.twitterBtn_clicked)
        self.loginForm.instagramBtn.clicked.connect(self.instagramBtn_clicked)

        self.loginForm.echoModeBtn.pressed.connect(self.echoModeBtn_clicked) # butona basılı tutulduğunda çalışacak fonksiyon
        self.loginForm.echoModeBtn.released.connect(self.echoModeBtn_clicked) # buton bırakıldığında çalışacak fonksiyon

   

    def loginBtn_clicked(self):
        uName=self.loginForm.userNameTxt.text()
        uPassword=self.loginForm.passwordTxt.text()
        if uName=="admin" and uPassword=="admin":
            self.close()
            self.mainLoad()
        else:
            self.loginForm.errorLbl.setText("Kullanıcı adı veya şifre hatalı")
    
    def twitterBtn_clicked(self):
        webbrowser.open("https://twitter.com/skyolympos")
    def instagramBtn_clicked(self):
        webbrowser.open("https://www.instagram.com/skyolympos/")
    def echoModeBtn_clicked(self): #butona basılınca da bırakınca da çalışacak fonksiyon
        if self.loginForm.passwordTxt.echoMode()==2:
            self.loginForm.passwordTxt.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.loginForm.passwordTxt.setEchoMode(QtWidgets.QLineEdit.Password)
