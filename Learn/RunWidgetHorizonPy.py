import sys
import RunWidgetHorizonLayout

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w= QWidget()
    w.resize(800, 600)
    ui = RunWidgetHorizonLayout.Ui_Form()
    ui.setupUi(w)

    w.show()

    sys.exit(app.exec())

