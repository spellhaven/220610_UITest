import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# uic는 좀 이따 불러와 보자.


class MyWindow(QWidget):  # QMainWindow 아니고 QWidget이다.

    def __init__(self):
        super().__init__()  # 부모클래스의 초기화자 호출, ㅋ
        self.initWindow()

    # 어. 각 위젯에도 css를 설정할 수 있어.
    # 디자이너에서는 처음 보이는 모습밖에 설정 못 하잖아?
    # 이런 식으로 코드로 하면 '주식 오르면 빨강, 내리면 파랑'식의 위.꾸 (위젯 꾸미기)가 가능하다.

    def initWindow(self):
        label_red = QLabel('빨강')
        label_blue = QLabel('파랑')

        label_red.setStyleSheet(  # 근데 여기 css는 디자이너에 쓸 때처럼 ; 하나씩 붙여야 한다. 명심하셈.

            "color: red;"
            "border-style: solid;"
            "border-width: 2px;"
            "border-color: red;"
            "background-color: pink;"

        )

        label_blue.setStyleSheet(  # 근데 여기 css는 디자이너에 쓸 때처럼 ; 하나씩 붙여야 한다.

            "color: blue;"
            "border-style: solid;"
            "border-width: 2px;"
            "border-color: blue;"
            "background-color: lightBlue;"

        )

        styleBox = QVBoxLayout()
        styleBox.addWidget(label_red)
        styleBox.addWidget(label_blue)

        self.setLayout(styleBox)

        self.setGeometry(100, 100, 300, 300)
        self.show()


if __name__ == '__main__':  # 이벤트 무한루프 돌려 주는 놈.
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
