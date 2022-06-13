import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType('ui/myWin.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        # super().__init__()  # 부모 클래스의 초기화자. 안 호출하면 에러남 ㅋ (어. 이게 파이썬이야.)
        p = super()  # 이런 식으로 2줄로 써서 부모 클래스 초기화해도 된다.
        p.__init__()
        self.setupUi(self)


        #self.setGeometry(50, 10, 500, 600)
        self.setWindowTitle('Hello World!')
        self.setWindowIcon(QIcon("icons/NeptuneBlue.png"))  # QIcon은 QtGui 안에 있디.

        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)

        #btn1 = QPushButton('버튼1', self)
        #btn1.move(30, 50)

        #btn2 = QPushButton('버튼2', self)
        #btn2.move(200, 50)



    def btn1Click(self):
        self.label1.setText('버튼1이 클릭됨!!! ㅋ!!!!')
        print('버튼1이 클릭됨!!!!!!!!!! ㅋ!!!!!!')

    def btn2Click(self):
        self.label1.setText('버튼? 2가? 클릭됨, ㅋ???')
        print('버튼2가 클릭됨, ㅋ')

app = QApplication(sys.argv)

myWin = MyWindow()
myWin.show()

app.exec_() #어. 코드 너 꺼지지 말고 계속 돌아가, ㅋ.
