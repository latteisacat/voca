import sys, os
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Main(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        widget_list = list()

        # 파이썬은 안되는게 없다
        for i in range(1, 12):
            locals()["widget_{}".format(i)] = QPushButton(f"Widget_{i}")
            widget_list.append(locals()["widget_{}".format(i)])

        # 레이아웃을 만들 때는 가장 작은 레이아웃 부터
        layout_high = QHBoxLayout()
        for widget in widget_list[:3]:
            layout_high.addWidget(widget)
        layout_middle = QHBoxLayout()
        for widget in widget_list[3:6]:
            layout_middle.addWidget(widget)
        layout_low = QHBoxLayout()
        for widget in widget_list[6:10]:
            layout_low.addWidget(widget)
        main_layout.addLayout(layout_high)
        main_layout.addLayout(layout_middle)
        main_layout.addLayout(layout_low)
        main_layout.addWidget(widget_list[-1])

        self.setLayout(main_layout)
        self.resize(500, 500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
