#引入系统
import sys
#导入.ui转换生成的模块CouldMusic
from Learn import CouldMusic
#从PyQt5.QtWidgets中引入QApplication和QWidget
from PyQt5.QtWidgets import QApplication,QWidget
#
if __name__ == '__main__':
    #创建应用对象
    app = QApplication(sys.argv)
    #创建主窗口对象
    w= QWidget()
    w.resize(800, 600)
    #创建UI界面对象
    ui = CouldMusic.Ui_Form()
    #将UI布局和控件安装到窗口w上
    ui.setupUi(w)
    #显示
    w.show()
    #进入事件循环
    sys.exit(app.exec())
