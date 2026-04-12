import sys
from PyQt5.QtWidgets import *


class LineEdit(QWidget):
    def __init__(self):
        super().__init__()

        flo = QFormLayout()
        normallinedit = QLineEdit()
        noecholineedit = QLineEdit()
        passwordlineedit = QLineEdit()
        passwordechoonedit = QLineEdit()

        flo.addRow('Normal',normallinedit)
        flo.addRow('NoEcho',noecholineedit)
        flo.addRow('Password',passwordlineedit)
        flo.addRow('Password Echoone',passwordechoonedit)

        normallinedit.setPlaceholderText("Normal")
        noecholineedit.setPlaceholderText("NoEcho")
        passwordlineedit.setPlaceholderText("Password")
        passwordechoonedit.setPlaceholderText("PasswordEchoOnEdit")

        #设置显示效果
        normallinedit.setEchoMode(QLineEdit.Normal)
        noecholineedit.setEchoMode(QLineEdit.NoEcho)
        passwordlineedit.setEchoMode(QLineEdit.Password)
        passwordechoonedit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setWindowTitle("LineEdit例子")
        self.setLayout(flo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LineEdit()
    win.show()
    sys.exit(app.exec_())