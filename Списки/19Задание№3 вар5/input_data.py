import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class ParticipantData(QWidget):
    def __init__(self, count):
        super().__init__()
        self.count = count
        self.current_participant = 0
        self.participants = []
        self.results_window = None  # Добавляем атрибут для хранения окна результатов
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ввод данных об участниках')
        self.layout = QVBoxLayout()

        self.label = QLabel(f'Введите данные для участника {self.current_participant + 1}/{self.count}:')
        self.surname_input = QLineEdit()
        self.name_input = QLineEdit()
        self.school_input = QLineEdit()
        self.score_input = QLineEdit()

        self.submit_button = QPushButton('Сохранить участника')
        self.submit_button.clicked.connect(self.save_participant)

        self.layout.addWidget(self.label)
        self.layout.addWidget(QLabel('Фамилия:'))
        self.layout.addWidget(self.surname_input)
        self.layout.addWidget(QLabel('Имя:'))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel('Школа:'))
        self.layout.addWidget(self.school_input)
        self.layout.addWidget(QLabel('Баллы:'))
        self.layout.addWidget(self.score_input)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def save_participant(self):
        if self.current_participant < self.count:
            surname = self.surname_input.text()
            name = self.name_input.text()
            school = int(self.school_input.text())
            score = int(self.score_input.text())

            # Сохраняем данные об участнике
            self.participants.append((surname, name, school, score))

            # Переход к следующему участнику
            self.current_participant += 1
            if self.current_participant < self.count:
                self.label.setText(f'Введите данные для участника {self.current_participant + 1}/{self.count}:')
                self.surname_input.clear()
                self.name_input.clear()
                self.school_input.clear()
                self.score_input.clear()
            else:
                # После ввода всех участников открываем окно результатов
                self.close()
                from results import Results
                self.results_window = Results(self.participants)  # Сохраняем ссылку на окно результатов
                self.results_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ParticipantData()  # Передаем количество участников
    window.show()
    app.exec_()
