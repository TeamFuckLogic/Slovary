import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea


class InitialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):

        # Заголовок
        self.title_label = QLabel("Лекция Python | Списки")
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)  # Центрируем заголовок

        # Создаем QLabel с текстом
        self.explanation_label = QLabel(
            "<i> Список (list)</i> — это один из самых важных и часто используемых типов данных в Python. Список представляет собой упорядоченную коллекцию элементов, <br>"
            " которые могут быть любого типа: числа, строки, другие списки и т.д. Списки являются изменяемыми, что означает, что вы можете изменять их содержимое после создания.<br>"
            " my_list = [1, 2, 3, 'Python', True]<br>"
            "<br><b><i> Способы создания списков:</i></b><br>"
            " - Прямое создание списка:<br>"
            "   fruits = ['apple', 'banana', 'cherry']<br>"
            " - Создание списка с помощью функции list():<br>"
            "   numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]<br>"
            " - Создание пустого списка:<br>"
            "   empty_list = []<br>"
            " - Инициализация списков с помощью генераторов:<br>"
            "<br><b><i> Основные операции со списками:</i></b><br>"
            "   squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]<br>"
            " - Доступ к элементам списка: Элементы списка индексируются, начиная с 0. Можно использовать отрицательные индексы для доступа к элементам с конца списка.<br>"
            "   fruits = ['apple', 'banana', 'cherry'] <br>print(fruits[0])  # apple <br>print(fruits[-1])  # cherry <br>"
            " - Изменение элементов списка:<br>"
            "   fruits[1] = 'orange' <br>print(fruits)  # ['apple', 'orange', 'cherry'] <br>"
            " - Срезы (slicing): Срезы позволяют получить подсписок из списка.<br>"
            "   numbers = [1, 2, 3, 4, 5] <br>print(numbers[1:3])  # [2, 3] <br>print(numbers[:3])   # [1, 2, 3] <br>print(numbers[2:])   # [3, 4, 5] <br>"
            " - Длина списка:<br>"
            "   print(len(numbers))  # 5<br>"
            " - Проверка наличия элемента в списке:<br>"
            "   print('apple' in fruits)  # True<br>"
            "<br><b><i> Методы списков:</i></b><br>"
            "<br><b><i> 1. Добавление элементов:</i></b><br>"
            " - append(): добавляет элемент в конец списка.<br>   fruits.append('grape')<br>"
            " - insert(): вставляет элемент на определенную позицию.<br>   fruits.insert(1, 'kiwi')<br>"
            " - extend(): добавляет несколько элементов в конец списка.<br>   fruits.extend(['mango', 'pineapple'])<br>"
            "<br><b><i> 2. Удаление элементов:</i></b><br>"
            " - remove(): удаляет первый найденный элемент.<br>   fruits.remove('banana')<br>"
            " - pop(): удаляет элемент по индексу (по умолчанию последний).<br>   fruits.pop(1)<br>"
            " - del(): удаляет один или несколько элементов из списка.<br>   del fruits[1]<br>"
            " - clear(): очищает весь список.<br>   fruits.clear()"
        )
        
        self.explanation_label.setStyleSheet("font-size: 14px;")

        # Создаем QScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Позволяет QLabel изменять размер
        self.scroll_area.setFixedHeight(850)  # Устанавливаем фиксированную высоту для области прокрутки
        self.scroll_area.setFixedWidth(1200)  # Устанавливаем фиксированную ширину для области прокрутки


        # Устанавливаем QLabel как виджет для QScrollArea
        self.scroll_area.setWidget(self.explanation_label)

        self.start_button = QPushButton("Проверить знания")
        self.start_button.setStyleSheet("font-size: 16px;")

        layout = QVBoxLayout()
        layout.addWidget(self.title_label, alignment=Qt.AlignCenter)  # Добавляем заголовок в layout
        layout.addWidget(self.scroll_area, alignment=Qt.AlignLeft)  # Добавляем QScrollArea в layout
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def connects(self):
        self.start_button.clicked.connect(self.start_test)

    def set_appear(self):
        self.setWindowTitle("Python | Списки")
        self.resize(700, 600)
        self.move(100, 100)

    def start_test(self):
        from info import InfoWindow
        self.hide()
        self.info_window = InfoWindow()
        self.info_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InitialWindow()
    sys.exit(app.exec_())