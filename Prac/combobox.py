import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class NewWindow(QWidget):
    def __init__(self):
        super(NewWindow, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle("我是新窗口")
        self.label1 = QLabel(self)
        self.label1.setText("惊喜！新窗口出现了！")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout = QHBoxLayout()
        layout.addWidget(self.label1)
        self.setLayout(layout)


class combobox(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Combox例子")
        self.resize(800, 600)
        layout = QVBoxLayout()
        self.fontselect = QPushButton("choose font")
        self.fontselect.clicked.connect(self.getFont)
        self.NewWinBtn = QPushButton("New Window")
        self.NewWinBtn.clicked.connect(self.newWindow)
        layout.addWidget(self.NewWinBtn)
        layout.addWidget(self.fontselect)

        self.l1 = QLabel(self)
        self.l2 = QLabel(self)
        self.l2.setText("Hello,测试字体例子")

        self.slider = QSlider(self)
        self.slider.setMinimum(10)
        self.slider.setMaximum(100)
        self.slider.setSingleStep(5)
        self.slider.setValue(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(3)
        self.slider.valueChanged.connect(self.change)
        self.slider.move(20,20)
        layout.addWidget(self.slider)

        layout.addWidget(self.l1)
        self.combobox = QComboBox(self)
        self.combobox.addItem("c")
        self.combobox.addItem("c++")
        self.combobox.addItems(["jave","python","c#"])
        self.combobox.currentIndexChanged.connect(self.selectionchange)
        layout.addWidget(self.combobox)
        layout.addWidget(self.l1)

        self.setLayout(layout)

    def selectionchange(self,i):
        self.l1.setText(self.combobox.currentText())
        print("Items in the list are :")
        for count in range(self.combobox.count()):
            print("item" + str(count) + "=" + self.combobox.itemText(count))
        print("current index",i,"selection changed",self.combobox.currentText() )

    def change(self):
        size = self.slider.value()
        self.l1.setFont(QFont("Arial",size))

    def getFont(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.l2.setFont(font)

    def newWindow(self):
        self.newWin = NewWindow()
        self.newWin.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = combobox()
    window.show()
    sys.exit(app.exec_())

