import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My Title")
window.resize(800, 600)
window.move(0,0)
window.show()

sys.exit(app.exec_())