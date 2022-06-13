import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):  # QMainWindow 아니고 QWidget이다.

    def __init__(self):
        super().__init__()  # 부모클래스의 초기화자 호출, ㅋ
        self.initWindow()

    # 콤보 박스와 레이블 예제.

    def initWindow(self):

        combo = QComboBox(self)
        combo.addItem('사과')
        combo.addItem('수박')
        combo.addItem('멜론')
        combo.addItem('딸기')

        self.label1 = QLabel('선택', self)
        self.label1.move(50, 100)

        combo.activated[str].connect(self.onCombo) #콤보 상자에서 선택한 텍스트를 라벨에 연결띠 하는 시그널.

        self.setGeometry(100, 100, 300, 300)
        self.show()

    def onCombo(self, text):
        self.label1.setText(text)


if __name__ == '__main__':  # 이벤트 무한루프 돌려 주는 놈.
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
