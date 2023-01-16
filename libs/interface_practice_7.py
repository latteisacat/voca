import sys, os
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# 간단한 계산기 만들어보기

class Main(QDialog):

    def __init__(self):
        super().__init__()
        self.solution = QLineEdit()
        self.equation = QLineEdit()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        layout_operation = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        layout_equation_solution.addRow("Equation: ", self.equation)
        layout_equation_solution.addRow("Solution: ", self.solution)

        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("*")
        button_division = QPushButton("/")

        button_plus.clicked.connect(lambda state, operator="+": self.button_operation_clicked(operator))
        button_minus.clicked.connect(lambda state, operator="-": self.button_operation_clicked(operator))
        button_product.clicked.connect(lambda state, operator="/": self.button_operation_clicked(operator))
        button_division.clicked.connect(lambda state, operator="*": self.button_operation_clicked(operator))

        layout_operation.addWidget(button_plus)
        layout_operation.addWidget(button_minus)
        layout_operation.addWidget(button_product)
        layout_operation.addWidget(button_division)

        button_clear = QPushButton("Clear")
        button_equal = QPushButton("=")

        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)

        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_equal)

        number_button_dict = dict()

        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            pos_row, pos_column = (3, 1) if number == 0 else divmod(number-1, 3)  # divmod는 몫과 나머지를 튜플로 반환

            number_button_dict[number].clicked.connect(lambda state, num=number: self.number_button_clicked(num))

            layout_number.addWidget(number_button_dict[number], pos_row, pos_column)

        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        # self.resize(400, 400)
        self.show()

    def button_operation_clicked(self, operator):
        equation = self.equation.text()
        equation += operator
        self.equation.setText(equation)

    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_equal_clicked(self):
        try:
            equation = self.equation.text()
            solution = eval(equation)  # 아니 이걸 직접 안만들어도 된다고? 파이썬은 진짜 신이다
            # eval함수는 들어온 문자열을 명령으로 인식할 수 있다. 그러니까 해당 부분에 코드가 들어온다면
            # 해당 코드를 실행시키는 것이다. 보안에 심각한 위협이 될 수 있으니 조심하자.
            # 계산기같이 단순한 프로그램은 화이트 리스트 방식으로 인풋을 제한하는 편이 좋아보인다.
            self.solution.setText(str(solution))
        except Exception as e:
            self.solution.setText("Error:" + str(e))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
