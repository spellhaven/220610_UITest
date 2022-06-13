import sys

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initWindow()

    def initWindow(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)) # 오늘 날짜를 상태표시줄에 표시해 보자.

        # 이번엔 메뉴바 말고 아이콘이 가득한 툴바를 만들어 보자.

        menu1 = QAction(QIcon('icons/exit.png'), 'EXIT', self)
        menu1.setShortcut('CTRL+Q')
        #menu1.setStatusTip('프로그램 종료')
        menu1.triggered.connect(qApp.quit)  # 프로그램 진짜 꺼 주는 함수, qApp.quit랑 연결하기.

        menu2 = QAction(QIcon('icons/print.png'), 'PRINT', self)
        menu2.setShortcut('CTRL+P')
        #menu2.setStatusTip('프로그램 출력')

        menu3 = QAction(QIcon('icons/save.png'), 'SAVE', self)
        menu3.setShortcut('CTRL+S')
        #menu3.setStatusTip('프로그램 저장')

        menu4 = QAction(QIcon('icons/edit.png'), 'EDIT', self)
        menu4.setShortcut('CTRL+E')
        #menu4.setStatusTip('프로그램 수정')

        toolbar = self.addToolBar('toolbar')
        toolbar.addAction(menu1)
        toolbar.addAction(menu2)
        toolbar.addAction(menu3)
        toolbar.addAction(menu4)

        self.setGeometry(100, 100, 300, 300)
        self.show()


if __name__ == '__main__':  # 이벤트 무한루프 돌려 주는 놈.
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
