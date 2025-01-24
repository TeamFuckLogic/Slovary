import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class InitialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.label = QLabel("Добро пожаловать! \nНажмите 'Начать тест', чтобы продолжить.")
        self.label.setStyleSheet("font-size: 18px;")

        self.explanation_label = QLabel("\n\n\nЭтот тест поможет вам оценить ваше эмоциональное состояние. "
                                         "\nОн состоит из 10 вопросов, на которые нужно ответить честно. "
                                         "\nОжидаемое время прохождения теста — около 5-10 минут. "
                                         "\nРезультаты теста могут помочь вам понять, нуждаетесь ли вы в поддержке. "
                                         "\nВсе ваши ответы останутся анонимными и конфиденциальными. "
                                         "\nЕсли вы почувствуете необходимость в помощи, пожалуйста, обратитесь к специалисту.")
        self.explanation_label.setStyleSheet("font-size: 14px;")

        self.start_button = QPushButton("Начать тест")

        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignLeft)
        layout.addWidget(self.explanation_label, alignment=Qt.AlignLeft)
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def connects(self):
        self.start_button.clicked.connect(self.start_test)

    def set_appear(self):
        self.setWindowTitle("Тест на депрессию")
        self.resize(700, 600)
        self.move(100, 100)

    def start_test(self):
        from questions import QuestionsWindow
        self.hide()
        self.questions_window = QuestionsWindow()
        self.questions_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InitialWindow()
    sys.exit(app.exec_())




