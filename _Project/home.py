# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(976, 740)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowTitle("Aircraft Maintenance Control System")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/skyolympos_logo_son.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"#mainFrame{\n"
"    background-color: #fefeff;\n"
"}\n"
"#logoLbl{\n"
"    background-color: #fefeff;\n"
"}\n"
"#leftMenu{\n"
"    background-color:#afc1d7;\n"
"}\n"
"\n"
"\n"
"#centralwidget{\n"
"    background-color:#eff9fe;\n"
"}\n"
"QLineEdit{\n"
"    background: transparent;\n"
"    color: #2596be;\n"
"}\n"
"#searchFrame{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #afc1d7;\n"
"}\n"
"#appHeader{\n"
"    color: #afc1d7;\n"
"}\n"
"#headerFrame{\n"
"    background-color: #fefeff;\n"
"}\n"
"\n"
"\n"
"#profileContFrame,#profileCont{\n"
"    background-color: #afc1d7;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 10px 5px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgba(131,96,53,255);\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(91,88,53,255)\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #fefeff;\n"
"    padding: 10px 5px;\n"
"    text-align: left;\n"
"    border-top-left-radius: 20px ;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        self.leftMenu.setMaximumSize(QtCore.QSize(250, 16777215))
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leftMenuframe = QtWidgets.QFrame(self.leftMenu)
        self.leftMenuframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftMenuframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuframe.setObjectName("leftMenuframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftMenuframe)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menuTopFrame = QtWidgets.QFrame(self.leftMenuframe)
        self.menuTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuTopFrame.setObjectName("menuTopFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.menuTopFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.logoLbl = QtWidgets.QLabel(self.menuTopFrame)
        self.logoLbl.setMinimumSize(QtCore.QSize(30, 30))
        self.logoLbl.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.logoLbl.setFont(font)
        self.logoLbl.setText("")
        self.logoLbl.setPixmap(QtGui.QPixmap(":/logo/skyolympos_logo_son.png"))
        self.logoLbl.setScaledContents(True)
        self.logoLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLbl.setObjectName("logoLbl")
        self.horizontalLayout_7.addWidget(self.logoLbl, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.menuTopFrame, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.leftMenuframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.menuFrame = QtWidgets.QFrame(self.frame)
        self.menuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuFrame.setObjectName("menuFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menuFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.homeBtn = QtWidgets.QPushButton(self.menuFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.homeBtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/whiteIcons/white/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/blueIcons/blue/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(24, 24))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setChecked(True)
        self.homeBtn.setAutoRepeat(False)
        self.homeBtn.setAutoExclusive(True)
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_4.addWidget(self.homeBtn)
        self.maintenanceBtn = QtWidgets.QPushButton(self.menuFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.maintenanceBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/whiteIcons/white/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/blueIcons/blue/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.maintenanceBtn.setIcon(icon2)
        self.maintenanceBtn.setIconSize(QtCore.QSize(24, 24))
        self.maintenanceBtn.setCheckable(True)
        self.maintenanceBtn.setAutoExclusive(True)
        self.maintenanceBtn.setObjectName("maintenanceBtn")
        self.verticalLayout_4.addWidget(self.maintenanceBtn)
        self.inventoryBtn = QtWidgets.QPushButton(self.menuFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inventoryBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/whiteIcons/white/book-open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/blueIcons/blue/book-open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.inventoryBtn.setIcon(icon3)
        self.inventoryBtn.setIconSize(QtCore.QSize(24, 24))
        self.inventoryBtn.setCheckable(True)
        self.inventoryBtn.setAutoExclusive(True)
        self.inventoryBtn.setObjectName("inventoryBtn")
        self.verticalLayout_4.addWidget(self.inventoryBtn)
        self.aircraftBtn = QtWidgets.QPushButton(self.menuFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aircraftBtn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/whiteIcons/white/twitter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/blueIcons/blue/twitter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.aircraftBtn.setIcon(icon4)
        self.aircraftBtn.setIconSize(QtCore.QSize(24, 24))
        self.aircraftBtn.setCheckable(True)
        self.aircraftBtn.setAutoExclusive(True)
        self.aircraftBtn.setObjectName("aircraftBtn")
        self.verticalLayout_4.addWidget(self.aircraftBtn)
        self.verticalLayout_5.addWidget(self.menuFrame, 0, QtCore.Qt.AlignTop)
        self.exitBtn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exitBtn.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/whiteIcons/white/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitBtn.setIcon(icon5)
        self.exitBtn.setIconSize(QtCore.QSize(24, 24))
        self.exitBtn.setCheckable(False)
        self.exitBtn.setAutoExclusive(True)
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout_5.addWidget(self.exitBtn)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.leftMenuframe)
        self.horizontalLayout.addWidget(self.leftMenu)
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainBody)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.headerFrame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuBtn = QtWidgets.QPushButton(self.widget)
        self.menuBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/blueIcons/blue/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon6)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setCheckable(True)
        self.menuBtn.setChecked(False)
        self.menuBtn.setAutoRepeat(False)
        self.menuBtn.setAutoDefault(False)
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_3.addWidget(self.menuBtn)
        self.appHeader = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.appHeader.setFont(font)
        self.appHeader.setTextFormat(QtCore.Qt.AutoText)
        self.appHeader.setScaledContents(False)
        self.appHeader.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.appHeader.setObjectName("appHeader")
        self.horizontalLayout_3.addWidget(self.appHeader)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.widget_2 = QtWidgets.QWidget(self.headerFrame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.searchFrame = QtWidgets.QFrame(self.widget_2)
        self.searchFrame.setMinimumSize(QtCore.QSize(160, 0))
        self.searchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.searchFrame)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setMaximumSize(QtCore.QSize(30, 30))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/blueIcons/blue/search.svg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.horizontalLayout_4.addWidget(self.searchFrame, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)
        self.widget_3 = QtWidgets.QWidget(self.headerFrame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.accountBtn = QtWidgets.QPushButton(self.widget_3)
        self.accountBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/blueIcons/blue/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountBtn.setIcon(icon7)
        self.accountBtn.setIconSize(QtCore.QSize(32, 32))
        self.accountBtn.setCheckable(True)
        self.accountBtn.setChecked(True)
        self.accountBtn.setAutoExclusive(True)
        self.accountBtn.setObjectName("accountBtn")
        self.horizontalLayout_6.addWidget(self.accountBtn, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addWidget(self.widget_3, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignTop)
        self.mainFrame = QtWidgets.QWidget(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout.addWidget(self.mainFrame)
        self.horizontalLayout.addWidget(self.mainBody)
        self.profileCont = QtWidgets.QWidget(self.centralwidget)
        self.profileCont.setEnabled(True)
        self.profileCont.setMinimumSize(QtCore.QSize(100, 0))
        self.profileCont.setMaximumSize(QtCore.QSize(200, 200))
        self.profileCont.setStyleSheet("")
        self.profileCont.setObjectName("profileCont")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.profileCont)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.profileContFrame = QtWidgets.QFrame(self.profileCont)
        self.profileContFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profileContFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profileContFrame.setObjectName("profileContFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.profileContFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.profileContFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3, 0, QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.profileContFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4, 0, QtCore.Qt.AlignTop)
        self.label_5 = QtWidgets.QLabel(self.profileContFrame)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setMaximumSize(QtCore.QSize(50, 50))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/whiteIcons/white/user.svg"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.myProfileBtn = QtWidgets.QPushButton(self.profileContFrame)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/whiteIcons/white/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.myProfileBtn.setIcon(icon8)
        self.myProfileBtn.setObjectName("myProfileBtn")
        self.verticalLayout_7.addWidget(self.myProfileBtn)
        self.logoutBtn = QtWidgets.QPushButton(self.profileContFrame)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/whiteIcons/white/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutBtn.setIcon(icon9)
        self.logoutBtn.setObjectName("logoutBtn")
        self.verticalLayout_7.addWidget(self.logoutBtn)
        self.verticalLayout_6.addWidget(self.profileContFrame, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.profileCont, 0, QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuBtn.toggled['bool'].connect(self.leftMenu.setHidden)
        self.accountBtn.toggled['bool'].connect(self.profileCont.setHidden)
        self.exitBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.homeBtn.setText(_translate("MainWindow", "Home"))
        self.maintenanceBtn.setText(_translate("MainWindow", "Maintenance"))
        self.inventoryBtn.setText(_translate("MainWindow", "Inventory"))
        self.aircraftBtn.setText(_translate("MainWindow", "Aircraft"))
        self.exitBtn.setText(_translate("MainWindow", "Close"))
        self.appHeader.setText(_translate("MainWindow", "Home"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search Something"))
        self.profileCont.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Settings"))
        self.label_4.setText(_translate("MainWindow", "Admin"))
        self.myProfileBtn.setText(_translate("MainWindow", "My Profile"))
        self.logoutBtn.setText(_translate("MainWindow", "Logout"))
import home_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())