import sys
from home import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream, Qt


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.setWindowFlags(Qt.X11BypassWindowManagerHint) # formun üst kısmını değiştirmek için 
        self.ui.setupUi(self)
        self.ui.profileCont.hide() # profileCont widgeti için butonun checked özelliği açık. başlangıçta hide olmalı


        self.ui.homeBtn.clicked.connect(self.homeBtn_clicked) # butona tıklandığında change_label fonksiyonunu çalıştır
        self.ui.maintenanceBtn.clicked.connect(self.maintenanceBtn_clicked) 
        self.ui.inventoryBtn.clicked.connect(self.inventoryBtn_clicked) 
        self.ui.aircraftBtn.clicked.connect(self.aircraftBtn_clicked) 

    def homeBtn_clicked(self): # home butonuna tıklandığında çalışacak fonksiyon
        self.ui.appHeader.setText(self.ui.homeBtn.text()) 
    def maintenanceBtn_clicked(self): # maintenance butonuna tıklandığında çalışacak fonksiyon
        self.ui.appHeader.setText(self.ui.maintenanceBtn.text())
    def inventoryBtn_clicked(self): # incentory butonuna tıklandığında çalışacak fonksiyon
        self.ui.appHeader.setText(self.ui.inventoryBtn.text()) 
    def aircraftBtn_clicked(self): # incentory butonuna tıklandığında çalışacak fonksiyon
        self.ui.appHeader.setText(self.ui.aircraftBtn.text()) 
    
    
    


if __name__ == "__main__":
     app = QApplication(sys.argv)
     window=MainWindow()
     window.show()
     sys.exit(app.exec_())

