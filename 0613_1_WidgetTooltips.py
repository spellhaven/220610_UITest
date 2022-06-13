import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#uic는 좀 이따 불러와 보자.


class MyWindow(QWidget):
    
    def __init__(self):
        super().__init__() # 부모클래스의 초기화자 호출, ㅋ
        self.initWindow() # 꼭 초기화자에서 함수를 이렇게 호출해야 실행된다. (당연하지-)

    def initWindow(self): # 풍선 도움말을 구현해 보자!
        QToolTip.setFont(QFont("Gulim", 12))
        self.setToolTip("<b>자바는 너무 빠르고</b>... <u>지금은 너무 느려</u>") #위젯 판에 툹팁 적용. 느릴 때가 좋을 때다. 즐겨봐.
        #아, 참고로 이 안은 xml 형식으로 된 html 코드니까(맞게 들었나?) 여튼 뭔 말이냐면, html 태그가 먹는다는 말이여.

        btn1 = QPushButton('버튼1', self)
        btn1.setToolTip('<i>버튼</i>에 대한 <i>풍선 도움말</i>')

        self.setGeometry(100, 100, 300, 300)
        self.show()

if __name__ == '__main__':  # 이벤트 무한루프 돌려 주는 놈.
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
























