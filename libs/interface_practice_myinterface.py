import sys, os
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.open_location = None
        self.save_location = None
        self.file_open_button = None
        self.file_save_button = None
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.setWindowTitle("단어장 만들기")
        self.resize(400, 300)

        self.file_open_button = QPushButton("파일 열기")
        self.file_open_button.clicked.connect(self.file_open_button_clicked)
        self.open_location = QLabel()

        self.file_save_button = QPushButton("저장할 위치")
        self.file_save_button.clicked.connect(self.file_save_button_clicked)
        self.save_location = QLabel()

        main_layout.addWidget(self.file_open_button)
        main_layout.addWidget(self.open_location)
        main_layout.addWidget(self.file_save_button)
        main_layout.addWidget(self.save_location)

        self.setLayout(main_layout)
        self.show()

    def file_open_button_clicked(self):
        open_file_name = QFileDialog.getOpenFileName(self, '파일 열기', '/')
        self.open_location.setText(str(open_file_name[0]))

    def file_save_button_clicked(self):
        save_file_name = QFileDialog.getSaveFileName(self, '저장할 위치', '/')
        self.save_location.setText(str(save_file_name[0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
