import sys, os
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# widget에 event 연결하기

class Main(QDialog):

    def __init__(self):
        super().__init__()
        self.line_edit_combo_box = QLineEdit()
        self.line_edit_check_box = QLineEdit()
        self.line_edit = QLineEdit()
        self.line_edit_radio_1 = QLineEdit()
        self.line_edit_radio_2 = QLineEdit()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        push_button = QPushButton("Button 1")
        push_button.clicked.connect(self.button_clicked)

        combo_box = QComboBox()
        combo_box.addItems(["dog", "cat", "rabbit", "lion"])
        combo_box.currentTextChanged.connect(self.combo_box_changed)

        check_box = QCheckBox("item")
        check_box.stateChanged.connect(self.check_box_changed)

        radio_button_1 = QRadioButton("A")
        radio_button_2 = QRadioButton("B")

        radio_button_1.toggled.connect(self.radio_1_toggled)
        radio_button_2.toggled.connect(self.radio_2_toggled)

        main_layout.addWidget(combo_box)
        main_layout.addWidget(push_button)
        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(self.line_edit_combo_box)

        main_layout.addWidget(check_box)
        main_layout.addWidget(self.line_edit_check_box)

        main_layout.addWidget(radio_button_1)
        main_layout.addWidget(radio_button_2)
        main_layout.addWidget(self.line_edit_radio_1)
        main_layout.addWidget(self.line_edit_radio_2)

        self.setLayout(main_layout)
        self.resize(400, 400)
        self.show()

    def button_clicked(self):
        self.line_edit.setText("button clicked")

    def combo_box_changed(self, item):
        self.line_edit_combo_box.setText(item)  # 함수의 인자 개수 주의

    def check_box_changed(self, state):
        self.line_edit_check_box.setText(str(state))  # 함수 인자 개수 주의 체크가 되어있으면 2 아니면 0을 반환

    def radio_1_toggled(self, state):
        self.line_edit_radio_1.setText(str(state))  # radio button은 true false를 반환

    def radio_2_toggled(self, state):
        self.line_edit_radio_2.setText(str(state))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
