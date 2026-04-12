import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QPushButton


class Winform(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        #初始化界面
        self.initUI()
        self.btn1 = QPushButton(self)


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        #需要鼠标停留才有提示
        self.setToolTip('这是一个<b>气泡提示</b>')
        self.setGeometry(200,300,400,400)
        self.setWindowTitle('气泡提示Demo')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = Winform()
    Win.btn1.setText("气泡提示")
    Win.btn1.setGeometry(20,20,100,100)
    Win.btn1.setToolTip('这是气泡提示按钮')
    Win.show()
    sys.exit(app.exec_())