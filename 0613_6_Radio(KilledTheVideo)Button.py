import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):  # QMainWindow 아니고 QWidget이다.

    def __init__(self):
        super().__init__()  # 부모클래스의 초기화자 호출, ㅋ
        self.initWindow()


    # 개념 몇 개만 더 하고 깃허브 연결한대 조금만 참아
    # 여튼 라디오 버튼 예제.


    def initWindow(self):

        radio1 = QRadioButton('첫번째버튼', self)
        radio1.move(50, 50)
        radio1.setChecked(True)

        radio2 = QRadioButton(self)
        radio2.move(50, 80)
        radio2.setText('두번째버튼')

        self.setGeometry(100, 100, 300, 300)
        self.show()


if __name__ == '__main__':  # 이벤트 무한루프 돌려 주는 놈.
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
