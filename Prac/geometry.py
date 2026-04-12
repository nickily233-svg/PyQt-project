import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication(sys.argv)
Widget = QWidget()

btn = QPushButton(Widget)
btn.setText("Button")

#设置位置为(0,0)
Widget.setWindowTitle("坐标系统例子 ")
Widget.setGeometry(0, 0, 800, 600)
#设置按钮的位置
btn.move(20, 20)
Widget.show()

print("Widget.x()=%d",Widget.x())
print("Widget.y()=%d",Widget.y())
print("Widget.width()=%d",Widget.width())
print("Widget.height()=%d",Widget.height())
print("Widget.geometry()=%d",Widget.geometry())
print("Widget.size())=%d",Widget.size())

if __name__ == '__main__':
    sys.exit(app.exec_())

