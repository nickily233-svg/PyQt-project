import sys

from PyQt5.QtCore import QDir,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class treeList(QWidget):
    def __init__(self, parent=None):
        super(treeList, self).__init__(parent)

        layout = QVBoxLayout()
        model = QFileSystemModel(self)
        path = "C:/"
        model.setRootPath(path)
        tree = QTreeView(self)
        tree.setModel(model)
        tree.setRootIndex(model.index(path))
        tree.setFixedSize(240,160)

        layout.addWidget(tree,alignment = Qt.AlignTop | Qt.AlignLeft)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = treeList()
    tree.setWindowTitle("QTreeView例子")
    tree.resize(640, 480)
    tree.show()
    sys.exit(app.exec_())

