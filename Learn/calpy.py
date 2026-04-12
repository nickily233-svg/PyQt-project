import sys
import cal

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import Qt

if __name__ == '__main__':

    app =QApplication(sys.argv)

    w =QWidget()

    ui = cal.Ui_Form()

    ui.setupUi(w)

    w.setWindowState(Qt.WindowMaximized)
    w.show()

    sys.exit(app.exec())