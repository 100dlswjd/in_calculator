from PySide6.QtCore import QEvent, Qt
from PySide6.QtGui import QKeyEvent
import in_tool
import sys

from main_form import Ui_in_calculator
from PySide6.QtWidgets import *

class mainwindow(QMainWindow, Ui_in_calculator):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        self.result_start = "<span style=\" font-size:14pt;\">" 
        self.result_end = "</span></p>"
        self.tem_num_1 = ""
        self.tem_num_2 = ""
        self.x = 0
        self.y = 0
        self.num_flag = False
        self.code = ""
        self.cal = False
        self.label_result_text = ""
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

        # 결과, 이전결과 초기화
        self.label_result.setText(self.result_start + "0" + self.result_end)
        self.label_prevresult.setText("")

        self.installEventFilter(self)
    def test_func(self):
        if self.num_flag == False:
            self.tem_num_1 += self.sender().text()
            self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.result_end)
            self.x = int(self.tem_num_1)
        elif self.num_flag == True:
            self.tem_num_2 += self.sender().text()
            self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + self.result_end)
            self.y = int(self.tem_num_2)
        print(self.x)
        pass
    
    def btn_plus_click(self):
        self.code = " + "
        self.num_flag = True
        #self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.result_end)
        self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + self.result_end)
        pass

    def btn_sub_click(self):
        self.code = " - "
        self.num_flag = True
        #self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.result_end)
        self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + self.result_end)
        pass

    def btn_div_click(self):
        self.code = " / "
        self.num_flag = True
        #self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.result_end)
        self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + self.result_end)
        pass

    def btn_mul_click(self):
        self.code = " * "
        self.num_flag = True
        #self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.result_end)
        self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + self.result_end)
        pass
    
    def btn_cancel_click(self):
        self.tem_num_1 = "0"
        self.tem_num_2 = "0"
        self.code = ""
        self.label_result.setText(self.result_start + "0" + self.result_end)
        pass

    def btn_delete_click(self):
        if self.num_flag == False:
            self.tem_num_1 = self.tem_num_1[0:-1]
        #self.label_result.setText(self.result_start + self.tem_num_1 + self.result_end)
            self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + self.result_end)
        if self.num_flag == True:
            self.tem_num_2 = self.tem_num_2[0:-1]
            self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + self.result_end)
            if self.tem_num_2 == "":
                self.code = ""
                self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + self.result_end)
                self.num_flag = False
        pass
    
    def btn_enter_click(self):
        if self.code == " + ":
            result1 = in_tool.add(self.x, self.y)
            self.num_flag = False
            self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + " = " + str(result1) + self.result_end)
            self.label_prevresult.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + " = " + str(result1) + self.result_end)
            self.tem_num_1 = ""
            self.tem_num_2 = ""
            self.code = ""

        elif self.code == " - ":
            result1 = in_tool.sub(self.x, self.y)
            self.num_flag = False
            self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + " = " + str(result1) + self.result_end)
            self.label_prevresult.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + " = " + str(result1) + self.result_end)
            self.tem_num_1 = ""
            self.tem_num_2 = ""
            self.code = ""

        elif self.code == " * ":
            result1 = in_tool.mul(self.x, self.y)
            self.num_flag = False
            self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + " = " + str(result1) + self.result_end)
            self.label_prevresult.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + " = " + str(result1) + self.result_end)
            self.tem_num_1 = ""
            self.tem_num_2 = ""
            self.code = ""

        elif self.code == " / ":
            result1, result2, result3 = in_tool.div(self.x, self.y)
            self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + " = " + str(result2) + "..." + str(result3) + self.result_end)
            self.label_prevresult.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + " = " + str(result2) + "..." + str(result3) + self.result_end)
            self.tem_num_1 = ""
            self.tem_num_2 = ""
            self.code = ""
            self.num_flag = False
        pass

    def eventFilter(self, watched, event) -> bool:
        if event.type() == QEvent.KeyRelease:
            key_event = QKeyEvent(event).key()
            print(key_event)
            if 9 >= key_event - 48 >= 0 :
                if self.num_flag == False:
                    self.tem_num_1 += str(key_event - 48)
                    self.label_result.setText(self.result_start + str(self.tem_num_1) + self.code + self.result_end)
                    self.x = int(self.tem_num_1)
                elif self.num_flag == True:
                    self.tem_num_2 += str(key_event - 48)
                    self.label_result.setText(self.result_start + self.tem_num_1 + self.code + self.tem_num_2 + self.result_end)
                    self.y = int(self.tem_num_2)
            # 47 = /
            elif key_event == 47:
                self.btn_div_click()
            # 42 = *
            elif key_event == 42:
                self.btn_mul_click()
            # 45 = -
            elif key_event == 45:
                self.btn_sub_click()
            # 43 = +
            elif key_event == 43:
                self.btn_plus_click()
            # 16777221 = enter
            elif key_event == 16777221:
                self.btn_enter_click()
            # 16777216 = esc
            elif key_event == 16777216:
                self.btn_cancel_click()
            # 16777219 = backspace
            elif key_event == 16777219:
                self.btn_delete_click()
        return super().eventFilter(watched, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    app.setStyle('Fusion')
    app.exec()