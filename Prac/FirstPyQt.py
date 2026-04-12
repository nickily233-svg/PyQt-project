import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget,QApplication

#1.创建一个Icon的窗口类 继承QWidget
class Icon(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()

    #2.初始化窗口
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowIcon(QIcon('程序图标'))
        self.setWindowIcon(QIcon(QIcon('D:\OneDrive\Pictures\timer.ico')))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = Icon()
    Win.show()
    sys.exit(app.exec_())