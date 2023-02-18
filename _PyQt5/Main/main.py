import sys
from home import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
    


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     window=MainWindow()
     window.show()
     sys.exit(app.exec_())

