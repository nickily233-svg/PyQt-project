import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QPushButton,QWidget

class CloseWin(QMainWindow):
    def __init__(self,parent=None):
        super(CloseWin,self).__init__(parent)
        self.setWindowTitle('关闭主窗口例子')

        self.resize(800,600)
        self.button1 = QPushButton('关闭主窗口')
        #将button1的clicked信号和槽函数on_click关联
        self.button1.clicked.connect(self.on_click)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        #设置成当前主窗口的中央控件
        self.setCentralWidget(main_frame)

    def on_click(self):
        #sender 是发送信号的对象
        sender = self.sender()
        print(sender.text()+'被按下了')
        #self.close()
        #从槽函数中湖区QApplication类对象 调用它的quit来关闭窗口
        qapp = QApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CloseWin()
    win.show()

    sys.exit(app.exec_())
