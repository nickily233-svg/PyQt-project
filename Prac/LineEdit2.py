import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt

class LineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit例子")

        flo = QFormLayout()

        l1 = QLineEdit(self)
        l1.setValidator(QIntValidator())
        l1.setMaxLength(4)
        l1.setAlignment(Qt.AlignRight)
        l1.setFont(QFont('Arial',20))
        flo.addRow("integer validator",l1)

        l2 = QLineEdit(self)
        l2.setValidator(QDoubleValidator(0.99,99.99,2))
        flo.addRow("double validator",l2)

        l3 = QLineEdit(self)
        l3.setInputMask("+99_9999_999999")
        flo.addRow("input mask",l3)

        l4 = QLineEdit(self)
        l4.textChanged.connect(self.textChanged)
        flo.addRow("Text Changed",l4)

        l5 = QLineEdit(self)
        l5.setEchoMode(QLineEdit.Password)
        l5.editingFinished.connect(self.enterpress)
        flo.addRow("Password",l5)

        l6 = QLineEdit("Hello PyQt5")
        l6.setReadOnly(True)
        flo.addRow("Read Only",l6)


        self.setLayout(flo)
        self.setWindowTitle("QLineEditDemo")
    def enterpress(self):
        print("输入的内容:"+ self.l5.text())
    def textChanged(self,text):
        print("已输入值")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec_())