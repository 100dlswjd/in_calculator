import in_tool
import sys

from main_form import Ui_in_calculator
from PySide6.QtWidgets import *

class mainwindow(QMainWindow, Ui_in_calculator):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        self.result_start = "<span style=\" font-size:16pt;\">" 
        self.result_end = "</span></p>"
        self.tem_num_1 = ""
        self.tem_num_2 = ""
        self.x = 0
        self.y = 0
        self.num_flag = False
        self.code = ""
        self.cal = False
        # 숫자 버튼 0 ~ 9
        self.btn_zero.clicked.connect(self.test_func)
        self.btn_one.clicked.connect(self.test_func)
        self.btn_two.clicked.connect(self.test_func)
        self.btn_three.clicked.connect(self.test_func)
        self.btn_four.clicked.connect(self.test_func)
        self.btn_five.clicked.connect(self.test_func)
        self.btn_six.clicked.connect(self.test_func)
        self.btn_seven.clicked.connect(self.test_func)
        self.btn_eight.clicked.connect(self.test_func)
        self.btn_nine.clicked.connect(self.test_func)
        
        # 계산 버튼 + - * /
        self.btn_plus.clicked.connect(self.btn_plus_click)
        self.btn_sub.clicked.connect(self.btn_sub_click)
        self.btn_div.clicked.connect(self.btn_div_click)
        self.btn_mul.clicked.connect(self.btn_mul_click)

        # 기능버튼 취소, 엔터, 지우기
        self.btn_Cancel.clicked.connect(self.btn_cancel_click)
        self.btn_enter.clicked.connect(self.btn_enter_click)
        self.btn_delete.clicked.connect(self.btn_delete_click)

    def test_func(self):
        self.tem_num_1 += self.sender().text()
        self.label_result.setText(self.result_start + self.tem_num_1 + self.result_end)
        self.x = int(self.tem_num_1)
        print(self.x)
        pass
    
    def btn_plus_click(self):
        self.code = " + "
        self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.result_end)
        
        pass

    def btn_sub_click(self):
        self.code = " - "
        self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.result_end)
        pass

    def btn_div_click(self):
        self.code = " / "
        self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.result_end)
        pass

    def btn_mul_click(self):
        self.code = " * "
        self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.result_end)
        pass
    
    def btn_cancel_click(self):
        
        pass

    def btn_delete_click(self):
        pass
    
    def btn_enter_click(self):
        if self.code == " + ":
            reuslt1 = in_tool.add(self.x, self.y)
        elif self.code == " - ":
            reuslt1 = in_tool.sub(self.x, self.y)
        elif self.code == " * ":
            reuslt1 = in_tool.mul(self.x, self.y)
        elif self.code == " / ":
            reuslt1, result2, result3 = in_tool.div(self.x, self.y)
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    app.setStyle('Fusion')
    app.exec()