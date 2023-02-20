import sys
from homeUi import Ui_MainWindow
import Class.userClass as userClass

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream, Qt


class MainWindow(QMainWindow):
    def loginLoad (self):
        from login import LoginWindow
        self.loginForm=LoginWindow()
        self.loginForm.show()

    def __init__(self, parent=None): # __init__ fonksiyonu, sınıf çağırıldığında çalışan fonksiyondur
        super(MainWindow, self).__init__() # QMainWindow sınıfını çağır

        self.mainForm = Ui_MainWindow() # homeUi.py dosyasındaki Ui_MainWindow sınıfını çağır
        self.mainForm.setupUi(self) # homeUi.py dosyasındaki setupUi fonksiyonunu çalıştır	
        self.mainForm.profileCont.hide() # profileCont widgeti için butonun checked özelliği açık. başlangıçta hide olmalı
        self.setWindowFlags(Qt.X11BypassWindowManagerHint) # formun üst kısmını değiştirmek için 

        self.mainForm.overviewBtn.clicked.connect(self.overviewBtn_clicked) # butona tıklandığında overviewBtn_clicked fonksiyonunu çalıştır
        self.mainForm.maintenanceBtn.clicked.connect(self.maintenanceBtn_clicked) # butona tıklandığında maintenanceBtn_clicked fonksiyonunu çalıştır
        self.mainForm.inventoryBtn.clicked.connect(self.inventoryBtn_clicked) # butona tıklandığında inventoryBtn_clicked fonksiyonunu çalıştır
        self.mainForm.aircraftBtn.clicked.connect(self.aircraftBtn_clicked) # butona tıklandığında aircraftBtn_clicked fonksiyonunu çalıştır
        self.mainForm.logoutBtn.clicked.connect(self.logoutBtn_clicked) # butona tıklandığında logoutBtn_clicked fonksiyonunu çalıştır


        self.mainForm.userNameLbl.setText(userClass.store.userName) # login formundan gelen kullanıcı adını yazdır
        self.mainForm.overviewBtn.click() # Sayfa açıldığında overview butonuna tıklanmış gibi çalıştır

    def overviewBtn_clicked(self): # home butonuna tıklandığında çalışacak fonksiyon
        self.mainForm.appHeader.setText(self.mainForm.overviewBtn.text()) 
    def maintenanceBtn_clicked(self): # maintenance butonuna tıklandığında çalışacak fonksiyon
        self.mainForm.appHeader.setText(self.mainForm.maintenanceBtn.text())
    def inventoryBtn_clicked(self): # incentory butonuna tıklandığında çalışacak fonksiyon
        self.mainForm.appHeader.setText(self.mainForm.inventoryBtn.text()) 
    def aircraftBtn_clicked(self): # incentory butonuna tıklandığında çalışacak fonksiyon
        self.mainForm.appHeader.setText(self.mainForm.aircraftBtn.text()) 
    def logoutBtn_clicked(self): # logout butonuna tıklandığında çalışacak fonksiyon
        self.close() # formu kapat
        self.loginLoad() # login formunu aç
        

    


