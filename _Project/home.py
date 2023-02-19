import sys
from homeUi import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream, Qt


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        self.mainForm = Ui_MainWindow()

        self.mainForm.setupUi(self)
        self.mainForm.profileCont.hide() # profileCont widgeti için butonun checked özelliği açık. başlangıçta hide olmalı
        self.setWindowFlags(Qt.X11BypassWindowManagerHint) # formun üst kısmını değiştirmek için 

        self.mainForm.overviewBtn.clicked.connect(self.overviewBtn_clicked) # butona tıklandığında change_label fonksiyonunu çalıştır
        self.mainForm.maintenanceBtn.clicked.connect(self.maintenanceBtn_clicked) 
        self.mainForm.inventoryBtn.clicked.connect(self.inventoryBtn_clicked) 
        self.mainForm.aircraftBtn.clicked.connect(self.aircraftBtn_clicked) 

        self.mainForm.overviewBtn.click() # Sayfa açıldığında overview butonuna tıklanmış gibi çalıştır

    def overviewBtn_clicked(self): # home butonuna tıklandığında çalışacak fonksiyon
        self.mainForm.appHeader.setText(self.mainForm.overviewBtn.text()) 
    def maintenanceBtn_clicked(self): # maintenance butonuna tıklandığında çalışacak fonksiyon
        self.mainForm.appHeader.setText(self.mainForm.maintenanceBtn.text())
    def inventoryBtn_clicked(self): # incentory butonuna tıklandığında çalışacak fonksiyon
        self.mainForm.appHeader.setText(self.mainForm.inventoryBtn.text()) 
    def aircraftBtn_clicked(self): # incentory butonuna tıklandığında çalışacak fonksiyon
        self.mainForm.appHeader.setText(self.mainForm.aircraftBtn.text()) 
    

    
"""
if __name__ == "__main__":
     app = QApplication(sys.argv)
     window=MainWindow()
     window.show()
     sys.exit(app.exec_())
"""

