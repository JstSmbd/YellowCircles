import sys

from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.can_paint = False
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.can_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.can_paint:
            self.can_paint = False
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            for _ in range(randint(1, 5)):
                size = randint(50, 150)
                try:
                    qp.drawEllipse(randint(0, self.width() - size),
                                   randint(0, self.height() - size), size, size)
                except ValueError:
                    pass
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())