import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
from PyQt5.QtWidgets import QLabel,QApplication,QWidget,QVBoxLayout

class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        #1.初始化标签控件
        label1.setText("这是一个文本标签")
        label1.setAutoFillBackground(True)
        #创建一个调色板
        palette = QPalette()
        palette.setColor(QPalette.Background,Qt.blue)

        label1.setPalette(palette)
        #设置水平方向居中对齐
        label1.setAlignment(Qt.AlignCenter)
        label2.setText("<a href='https://www.python.org'>欢迎使用Python应用</a>")
        label2.setAlignment(Qt.AlignLeading|Qt.AlignLeft)

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("python.png"))
        label3.setScaledContents(True)

        label4.setText("<A href='http://www.cnblogs.com/wangshuo1/'>欢迎访问信平的小屋</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')

        #2.在窗口布局中添加控件
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        #3.允许label1控件访问超链接
        #打开允许超链接，默认是不允许打开的需要使用setOpenExternalLinks(True)
        label1.setOpenExternalLinks(True)
        label4.setOpenExternalLinks(True)
        #点击文本框绑定槽事件
        label4.linkActivated.connect(self.link_clicked)

        #划过文本框绑定槽事件
        label2.linkHovered.connect(self.link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel例子")

    def link_clicked(self,link):
        print("link_clicked")
    def link_hovered(self,link):
        print("link_hovered")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec_())