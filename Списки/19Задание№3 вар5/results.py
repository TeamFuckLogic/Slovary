
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class Results(QWidget):
    def __init__(self, participants):
        super().__init__()
        self.participants = participants
        self.initUI()

    def initUI(self):
        max_score = -1
        second_max_score = -1

        # Собираем баллы участников
        scores = [score for _, _, _, score in self.participants]

        # Находим наибольший и второй наибольший баллы
        for score in scores:
            if score > max_score:
                second_max_score = max_score
                max_score = score
            elif max_score > score > second_max_score:
                second_max_score = score

        # Подсчитываем количество призеров
        prize_winners_count = scores.count(second_max_score)

        # Выводим результаты
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'Наибольший балл призера: {second_max_score}'))
        layout.addWidget(QLabel(f'Количество участников с таким баллом: {prize_winners_count}'))

        self.setLayout(layout)
        self.setWindowTitle('Результаты олимпиады')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Results()
    window.show()
    app.exec_()

