import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class VocaApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("voca Application")
        self.resize(600, 400)
        self.center()
        self.show()

        ok_button = QPushButton("확인")
        cancel_button = QPushButton("취소")

        hbox = QHBoxLayout()  # horizon
        hbox.addStretch(1)
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)
        hbox.addStretch(1)

        vbox = QVBoxLayout()  # vertical
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VocaApp()
    sys.exit(app.exec_())  # python 3 이상부터는 exec_() 와 exec()는 동일. 이전에는 exec가 예약어 였기 때문에 구분이 필요했음.


