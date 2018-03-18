from PyQt5 import QtWidgets
from mywindow import mywindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = mywindow()
    windows.show()
    sys.exit(app.exec_())