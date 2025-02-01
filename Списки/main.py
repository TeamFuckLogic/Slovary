import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class InitialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.label = QLabel("Python | Списки")
        self.label.setStyleSheet("font-size: 18px; font: bold")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
# Теория по спискам
        self.explanation_label = QLabel("Список (list) — это один из самых важных и часто используемых типов данных в Python. Список представляет собой упорядоченную коллекцию элементов, которые могут быть любого типа: числа, строки, другие списки и т.д. Списки являются изменяемыми, что означает, что вы можете изменять их содержимое после создания.\n"
                                        "Verify \nRun \nCopy code \nmy_list = [1, 2, 3, 'Python', True]"
                                        "Способы создания списков: "
                                        "- Прямое создание списка:"
                                        "fruits = ['apple', 'banana', 'cherry']"
                                        "- Создание списка с помощью функции list():"
                                        "numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]"
                                        "- Создание пустого списка: "
                                        "empty_list = []"
                                        "- Инициализация списков с помощью генераторов: "
                                        "Основные операции со списками "
                                        "squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] "
                                        "- Доступ к элементам списка: Элементы списка индексируются, начиная с 0. Можно использовать отрицательные индексы для доступа к элементам с конца списка."
                                        "fruits = ['apple', 'banana', 'cherry'] \nprint(fruits[0])  # apple \nprint(fruits[-1])  # cherry "
                                        "- Изменение элементов списка: "
                                        "fruits[1] = 'orange' \nprint(fruits)  # ['apple', 'orange', 'cherry'] "
                                        "- Срезы (slicing): Срезы позволяют получить подсписок из списка. "
                                        "numbers = [1, 2, 3, 4, 5] \nprint(numbers[1:3])  # [2, 3] \nprint(numbers[:3])   # [1, 2, 3] \nprint(numbers[2:])   # [3, 4, 5] "
                                        "- Длина списка: "
                                        "print(len(numbers))  # 5"
                                        "- Проверка наличия элемента в списке: "
                                        "print('apple' in fruits)  # True "
                                        "Методы списков"
                                        "Добавление элементов:"
                                        "- append(): добавляет элемент в конец списка. \nfruits.append('grape')"
                                        "- insert(): вставляет элемент на определенную позицию. \nfruits.insert(1, 'kiwi')"
                                        "- extend(): добавляет несколько элементов в конец списка. \nfruits.extend(['mango', 'pineapple'])"
                                        "Удаление элементов:"
                                        "- remove(): удаляет первый найденный элемент. \nfruits.remove('banana')"
                                        "- pop(): удаляет элемент по индексу (по умолчанию последний). \nfruits.pop(1)"
                                        "- clear(): очищает весь список. \nfruits.clear()")
        self.explanation_label.setStyleSheet("font-size: 14px;")

        self.start_button = QPushButton("Проверить знания по теме")

        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignLeft)
        layout.addWidget(self.explanation_label, alignment=Qt.AlignLeft)
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def connects(self):
        self.start_button.clicked.connect(self.start_test)

    def set_appear(self):
        self.setWindowTitle("Python | Списки")
        self.resize(700, 600)
        self.move(100, 100)

    def start_test(self):
        from questions import QuestionsWindow
        self.hide()
        self.questions_window = QuestionsWindow()
        self.questions_window.show()