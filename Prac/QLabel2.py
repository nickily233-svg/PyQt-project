import sys
from PyQt5.QtWidgets import *


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel例子")
        namelb1 = QLabel('&Name',self)
        nameed1 = QLineEdit(self)
        namelb1.setBuddy(nameed1)

        namelb2 = QLabel('&Password',self)
        nameed2 = QLineEdit(self)
        namelb2.setBuddy(nameed2)

        btnok = QPushButton('&ok',self)
        btnCancel = QPushButton('Cancel',self)

        mainlayout = QGridLayout(self)
        mainlayout.addWidget(namelb1,0,0)
        mainlayout.addWidget(namelb2,1,0)

        mainlayout.addWidget(nameed1,0,1,1,2)
        mainlayout.addWidget(nameed2,1,1,1,2)

        mainlayout.addWidget(btnok,2,1)
        mainlayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QLabelDemo()
    win.show()
    sys.exit(app.exec_())