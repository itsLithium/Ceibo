import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class Squares(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Squares")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor("#dddddd"))
        painter.setBrush(brush)
        for i in range(50):
            for j in range(50):
                x = 20 * i
                y = 20 * j
                painter.drawRect(x, y, 10, 10)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Squares()
    window.show()
    sys.exit(app.exec_())