import sys

from PyQt5.QtGui import QStandardItemModel,QStandardItem
from  PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QListView,QMessageBox,QGridLayout
from PyQt5.QtCore import QStringListModel, QSize,Qt


class ListViewDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 270)
        self.setWindowTitle("ListViewDemo")

        listView = QListView(self)
        listView.setViewMode(QListView.IconMode)
        listView.setResizeMode(QListView.Adjust)
        listView.setGridSize(QSize(100, 100))

        slm = QStandardItemModel(self)
        self.qlist = []
        self.qlist.insert(0,"item1")
        self.qlist.insert(1,"item2")
        self.qlist.insert(2,"item3")
        self.qlist.insert(3,"item4")

        for text in self.qlist:
            item = QStandardItem(text)
            item.setTextAlignment(Qt.AlignCenter)
            slm.appendRow(item)

        listView.setModel(slm)
        listView.clicked.connect(self.onClick)

        self.setCentralWidget(listView)

    def onClick(self,qModelIndex):
        QMessageBox.information(self, "ListWidget", "你选择了:"+self.qlist[qModelIndex.row()])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ListViewDemo()
    demo.show()
    sys.exit(app.exec_())