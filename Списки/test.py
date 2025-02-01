import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox

class QuestionsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_question = 0
        self.score = 0
        self.questions = [
            {
                "question": "1. Что такое список в Python?",
                "options": [
                    "Упорядоченная коллекция элементов",
                    "Неупорядоченная коллекция элементов",
                    "Тип данных для хранения только чисел",
                    "Тип данных для хранения только строк"
                ],
                "answer": 0 
            },
            {
                "question": "2. Как создать пустой список?",
                "options": [
                    "empty_list = []",
                    "empty_list = list()",
                    "empty_list = {}",
                    "empty_list = ()"
                ],
                "answer": 0
            },
            {
                "question": "3. Как получить длину списка?",
                "options": [
                    "len(list)",
                    "list.len()",
                    "length(list)",
                    "size(list)"
                ],
                "answer": 0
            },
            {
                "question": "4. Какой метод добавляет элемент в конец списка?",
                "options": [
                    "add()",
                    "append()",
                    "insert()",
                    "extend()"
                ],
                "answer": 1
            },
            {
                "question": "5. Как удалить элемент по индексу?",
                "options": [
                    "remove()",
                    "pop()",
                    "delete()",
                    "clear()"
                ],
                "answer": 1
            }
        ]
        self.show_question()

    def initUI(self):
        self.setWindowTitle("Тест по теории списков")
        self.resize(400, 300)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def show_question(self):
        self.layout.addWidget(QLabel(self.questions[self.current_question]["question"]))
        self.radio_buttons = []
        for i, option in enumerate(self.questions[self.current_question]["options"]):
            radio_button = QRadioButton(option)
            self.radio_buttons.append(radio_button)
            self.layout.addWidget(radio_button)
        self.submit_button = QPushButton("Ответить")
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)

    def check_answer(self):
        selected_option = next((i for i, rb in enumerate(self.radio_buttons) if rb.isChecked()), None)
        if selected_option is not None:
            if selected_option == self.questions[self.current_question]["answer"]:
                self.score += 1
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.clear_layout()
                self.show_question()
            else:
                self.show_result()

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def show_result(self):
        self.clear_layout()
        result_label = QLabel(f"Ваш результат: {self.score} из {len(self.questions)}")
        self.layout.addWidget(result_label)
        self.exit_button = QPushButton("Выход")
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuestionsWindow()
    window.show()
    sys.exit(app.exec_())