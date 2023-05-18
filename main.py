import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QWidget,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Turbo_Waffle')
        self.setMinimumSize(QSize(800, 600))  # Минимальный размер

        main_layout = QHBoxLayout()  # Главный main_layout, остальное на нем будет

        main_layout.addWidget(QLabel('Фильтры и поиск'), stretch=1)
        main_layout.addWidget(QLabel('Таблица с фильмами'), stretch=2)

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()  # Запускаем основной рабочий цикл
