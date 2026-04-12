import sys
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow

class Winfrom(QMainWindow):
    def __init__(self,parent=None):
        super(Winfrom,self).__init__(parent)

        self.setWindowTitle("主窗口放在屏幕中间例子")
        self.resize(370,250)
        #调用Winfrom类里面的自定义函数
        self.center()

    def center(self):
        #QDesktopWidget()是描述显示屏幕的类 .screenGeometry()获取屏幕的大小
        screen = QDesktopWidget().screenGeometry()
        #获取QWidget窗口的大小
        size = self.geometry()
        #将窗口移到屏幕中间
        self.move((screen.width() - size.width())//2,
                  (screen.height() - size.height())//2)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    Win = Winfrom()
    Win.show()
    sys.exit(app.exec_())
