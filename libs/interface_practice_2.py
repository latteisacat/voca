import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class VocaApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('읽을 파일'), 0, 0)
        grid.addWidget(QLabel('저장할 위치'), 1, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)

        self.setWindowTitle("voca Application")
        self.resize(600, 400)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VocaApp()
    sys.exit(app.exec_())  # python 3 이상부터는 exec_() 와 exec()는 동일. 이전에는 exec가 예약어 였기 때문에 구분이 필요했음.


