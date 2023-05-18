import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Orange Swallow')
        self.setFixedSize(800, 600)  # Фиксированный размер


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()  # Запускаем основной рабочий цикл
