import sys
import sheet

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt

if __name__ == '__main__':

    app =QApplication(sys.argv)

    w =QWidget()

    ui = sheet.Ui_Form()

    ui.setupUi(w)
    w.setWindowTitle("Sheet")
    w.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
    w.setWindowFlag(Qt.WindowMinimizeButtonHint,False)
    w.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
    w.setWindowFlag(Qt.WindowCloseButtonHint,True)

    w.show()

    sys.exit(app.exec())