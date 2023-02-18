import sys
from home import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.profileCont.hide() # profileCont widgeti için butonun checked özelliği açık. başlangıçta hide olmalı
        
        
  
    


if __name__ == "__main__":
     app = QApplication(sys.argv)
     window=MainWindow()
     window.show()
     sys.exit(app.exec_())

