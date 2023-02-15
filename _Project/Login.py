# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, LoginRes


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 554)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setStyleSheet("QPushButton#BtnLogin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#BtnLogin:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219),stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#BtnLogin:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(150,123,111,255)\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#BtnTwitter{\n"
"    background-color:  rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"QPushButton#BtnTwitter:hover{\n"
"color: rgba(131,96,53,255);\n"
"}\n"
"QPushButton#BtnTwitter:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(91,88,53,255)\n"
"}\n"
"\n"
"QPushButton#BtnInstagram{\n"
"    background-color:  rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"QPushButton#BtnInstagram:hover{\n"
"color: rgba(131,96,53,255);\n"
"}\n"
"QPushButton#BtnInstagram:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(91,88,53,255)\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/Screenshot_2.png);\n"
"border-top-left-radius:50px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius:50px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(340, 80, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_4.setObjectName("label_4")
        self.txtUserName = QtWidgets.QLineEdit(self.widget)
        self.txtUserName.setGeometry(QtCore.QRect(295, 150, 190, 37))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txtUserName.setFont(font)
        self.txtUserName.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtUserName.setObjectName("txtUserName")
        self.txtPassword = QtWidgets.QLineEdit(self.widget)
        self.txtPassword.setGeometry(QtCore.QRect(295, 215, 190, 37))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txtPassword.setFont(font)
        self.txtPassword.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.BtnLogin = QtWidgets.QPushButton(self.widget)
        self.BtnLogin.setGeometry(QtCore.QRect(295, 295, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnLogin.setFont(font)
        self.BtnLogin.setObjectName("BtnLogin")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(300, 350, 181, 16))
        self.label_5.setStyleSheet("color:rgba(0,0,0,210);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 380, 131, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BtnTwitter = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BtnTwitter.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.BtnTwitter.setFont(font)
        self.BtnTwitter.setObjectName("BtnTwitter")
        self.horizontalLayout.addWidget(self.BtnTwitter)
        self.BtnInstagram = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BtnInstagram.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.BtnInstagram.setFont(font)
        self.BtnInstagram.setObjectName("BtnInstagram")
        self.horizontalLayout.addWidget(self.BtnInstagram)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 230, 141))
        self.label_6.setStyleSheet("background-color:rgba(0,0,0,75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 231, 51))
        self.label_7.setStyleSheet("border-image: url(:/images/skyolympos_logo_son.png);\n"
"border-top-left-radius:50px")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(50, 145, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255,255,255,200);")
        self.label_8.setObjectName("label_8")

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.BtnLogin.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.txtUserName.setPlaceholderText(_translate("Form", " User Name"))
        self.txtPassword.setPlaceholderText(_translate("Form", " Password"))
        self.BtnLogin.setText(_translate("Form", "Log In"))
        self.label_5.setText(_translate("Form", "Forgot your User Name or password?"))
        self.BtnTwitter.setText(_translate("Form", "D"))
        self.BtnInstagram.setText(_translate("Form", "Q"))
        self.label_8.setText(_translate("Form", "Welcome to the Aircraft\n"
"Maintenance Control System"))


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())