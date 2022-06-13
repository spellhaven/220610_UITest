import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):  # QMainWindow 아니고 QWidget이다.

    def __init__(self):
        super().__init__()  # 부모클래스의 초기화자 호출, ㅋ
        self.initWindow()


    # 어. 언제까지 개. 개념 하. 하나하나씩...
    # h. html. 생. 생각나요. 생각나요. 빨. 빨리 프. 프로젝트 시. 시작해 주. 주세요... 🥺
    # 여튼 체크박스 예제.


    def initWindow(self):
        checkBox = QCheckBox('체크박스', self)
        #checkBox.toggle() # 체크박스 체크된 상태로 출력
        checkBox.stateChanged.connect(self.changeText)  # 시그널이니까 꼭 .connect로 끝내야 하고, 안에 들어오는 함수는 () 없이 이름만 써야 한다. 함수를 호출하는 게 아니라 연결만 해야 하니까.
        # 여튼 체크박스의 상태가 변하면 self.changeText()를 호출하라는 의미의 시그널임.

        self.setGeometry(100, 100, 300, 300)
        self.show()

    def changeText(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('체크박스 체크 성공!')
        else:
            self.setWindowTitle('체크박스 체크 않됨!')


if __name__ == '__main__':  # 이벤트 무한루프 돌려 주는 놈.
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
