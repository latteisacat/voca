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
        layout = QVBoxLayout()

        label_widget = QLabel("Hello World!")
        button_widget = QPushButton("Click")
        combobox_widget = QComboBox()
        combobox_widget.addItem("Python")
        combobox_widget.addItem("C")
        combobox_widget.addItem("C++")
        combobox_widget.addItem("Fortran")

        check_box_widget_summer = QCheckBox("Summer")
        check_box_widget_winter = QCheckBox("Winter")

        # radio button은 여러 메뉴중 하나만 체크 가능
        radio_button_widget_male = QRadioButton("Male")
        radio_button_widget_female = QRadioButton("FeMale")

        spinbox_widget = QSpinBox()

        date_widget = QDateEdit()
        time_widget = QTimeEdit()

        list_widget = QListWidget()
        item_1 = QListWidgetItem("Cat")
        item_2 = QListWidgetItem("Dog")
        item_3 = QListWidgetItem("Bird")
        list_widget.addItem(item_1)
        list_widget.addItem(item_2)
        list_widget.addItem(item_3)

        layout.addWidget(label_widget)
        layout.addWidget(button_widget)
        layout.addWidget(combobox_widget)
        layout.addWidget(check_box_widget_summer)
        layout.addWidget(check_box_widget_winter)
        layout.addWidget(radio_button_widget_male)
        layout.addWidget(radio_button_widget_female)
        layout.addWidget(spinbox_widget)
        layout.addWidget(date_widget)
        layout.addWidget(time_widget)
        layout.addWidget(list_widget)

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
