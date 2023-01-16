import sys, os
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Form이란?
# 정보를 입력하거나 출력하는데 많이 이용되는 형태
# pyqt에서는 QFormLayout이라는 Label:Field 형태의 배치 제공


class Main(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QFormLayout()

        name_widget = QLineEdit()

        birthday_layout = QHBoxLayout()

        year_widget = QComboBox()
        month_widget = QComboBox()
        date_widget = QComboBox()

        birthday_layout.addWidget(year_widget)
        birthday_layout.addWidget(month_widget)
        birthday_layout.addWidget(date_widget)

        address_layout = QVBoxLayout()
        address_1 = QComboBox()
        address_1.addItems(["서울", "인천", "대전", "대구", "부산", "울산", "광주"])
        address_2 = QLineEdit()
        address_layout.addWidget(address_1)
        address_layout.addWidget(address_2)

        email_layout = QHBoxLayout()
        email_id = QLineEdit()
        email_company = QLineEdit()
        email_combobox = QComboBox()
        email_combobox.addItems(["gmail.com", "naver.com", "daum.net"])
        email_layout.addWidget(email_id)
        email_layout.addWidget(QLabel("@"))
        email_layout.addWidget(email_company)
        email_layout.addWidget(email_combobox)

        height_widget = QSpinBox()
        height_widget.setMaximum(250)
        height_widget.setMinimum(0)

        for year in range(1900, 2024):
            year_widget.addItem(str(year))
        for month in range(1, 13):
            month_widget.addItem(str(month))
        for date in range(1, 32):
            date_widget.addItem(str(date))

        main_layout.addRow("Name: ", name_widget)  # Label, Field
        main_layout.addRow("Birthday: ", birthday_layout)
        main_layout.addRow("Address: ", address_layout)
        main_layout.addRow("E-mail: ", email_layout)
        main_layout.addRow("Height(cm)", height_widget)

        self.setLayout(main_layout)
        self.resize(500, 500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
