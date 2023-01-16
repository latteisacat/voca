from wordlist import reader
from wordlist import searcher
from libs import list_to_csv
import sys, os
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class SaveFileThread(QThread):
    def __init__(self, parent, dic_word, save_file_location):
        super().__init__(parent)
        self.dic_word = dic_word
        self.save_file_location = save_file_location

    def run(self):
        self.dic_word.word_search()
        self.dic_word.convert_to_2d_list()
        list_to_csv.list_to_csv(self.dic_word.voca_list, self.save_file_location)


class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.web_driver_location = None
        self.web_driver_button = None
        self.web_driver_path = None
        self.search_data = None
        self.dic_word = None
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

        self.web_driver_button = QPushButton("웹 드라이버 지정")
        self.web_driver_button.clicked.connect(self.web_driver_button_clicked)
        self.web_driver_location = QLabel()

        self.file_save_button = QPushButton("저장할 위치")
        self.file_save_button.clicked.connect(self.file_save_button_clicked)
        self.save_location = QLabel()

        main_layout.addWidget(self.file_open_button)
        main_layout.addWidget(self.open_location)
        main_layout.addWidget(self.web_driver_button)
        main_layout.addWidget(self.web_driver_location)
        main_layout.addWidget(self.file_save_button)
        main_layout.addWidget(self.save_location)

        self.setLayout(main_layout)
        self.show()

    def file_open_button_clicked(self):
        open_file_name = QFileDialog.getOpenFileName(self, '파일 열기', './')
        file_location = str(open_file_name[0])
        if file_location.find(".txt") == -1:
            self.open_location.setText("Please select a .txt file")
        else:
            self.open_location.setText(file_location)
            self.search_data = reader.Reader(self.open_location.text())
            self.search_data.read_data()
            self.search_data.remove_stopwords()
            print(self.search_data.data)

    def file_save_button_clicked(self):
        save_file_location = QFileDialog.getSaveFileName(self, '저장할 위치', './')[0]
        self.save_location.setText(save_file_location)
        thread = SaveFileThread(self, self.dic_word, save_file_location)
        thread.start()

    def web_driver_button_clicked(self):
        web_driver_location = QFileDialog.getOpenFileName(self, '웹 드라이버 선택', './')[0]
        self.web_driver_location.setText(web_driver_location)
        self.web_driver_path = web_driver_location
        self.dic_word = searcher.Searcher(self.search_data.data, self.web_driver_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())


# search_data = reader.Reader("C:\\developer\\voca\\eng.txt")
#
# search_data.read_data()
# search_data.remove_stopwords()
# print(search_data.data)
#
# dic_word = searcher.Searcher(search_data.data, "C:/developer/voca/webdriver/chromedriver.exe")
# dic_word.word_search()
# print(dic_word.voca_list)
# dic_word.convert_to_2d_list()
# print(dic_word.voca_list)
# list_to_csv.list_to_csv(dic_word.voca_list, 'C:/developer/voca/voca_list.csv')
#

