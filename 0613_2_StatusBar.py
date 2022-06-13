import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow): #QWidget 아니고 QMainWindow다.

    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.statusBar().showMessage('어. 이놈은 상태표시줄이야. ver 1.0.0')  # 상태표시줄 메인윈도우에 붙이기.

        # 심심하니까 애플리케이션 꺼 주는 기능 예쁘게 만들고 메뉴 바에도 추가해 보자.
        exitWindow = QAction(QIcon('icons/NeptuneBlack.png'), 'EXIT', self)
        exitWindow.setShortcut('CTRL+Q')
        exitWindow.setStatusTip('프로그램 종료')
        exitWindow.triggered.connect(qApp.quit)  # 프로그램 진짜 꺼 주는 함수, qApp.quit랑 연결하기.

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&파일')  # 앞에 &를 써 줘야 하는 이유는...
        filemenu.addAction(exitWindow)

        self.setGeometry(100, 100, 300, 300)
        self.show()


if __name__ == '__main__':  # 이벤트 무한루프 돌려 주는 놈.
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
