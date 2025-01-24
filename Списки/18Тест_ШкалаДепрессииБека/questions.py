import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QRadioButton, QMessageBox

from text import questions

class QuestionsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вопросы")

        self.layout = QVBoxLayout()
        self.current_question = 0
        self.scores = []
        self.questions_per_set = 1  # Количество вопросов, отображаемых за раз

        self.question_labels = []
        self.answer_buttons = []

        for i in range(self.questions_per_set):
            question_label = QLabel()
            question_label.setStyleSheet("font-size: 16px;")
            self.layout.addWidget(question_label)
            self.question_labels.append(question_label)

            btns = []
            for j in range(4):  # 4 варианта ответа
                btn = QRadioButton()
                btn.setStyleSheet("font-size: 14px;")
                self.layout.addWidget(btn)
                btns.append(btn)
            self.answer_buttons.append(btns)

        self.next_button = QPushButton("Далее")
        self.layout.addWidget(self.next_button)
        self.next_button.clicked.connect(self.next_question)

        self.setLayout(self.layout)
        self.load_questions()

    def load_questions(self):
        for i in range(self.questions_per_set):
            if self.current_question + i < len(questions):
                question = questions[self.current_question + i]
                self.question_labels[i].setText(question["question"])
                for j, answer in enumerate(question["answers"]):
                    self.answer_buttons[i][j].setText(answer)
                    # Устанавливаем состояние радиокнопок в зависимости от предыдущих ответов
                    if len(self.scores) > self.current_question + i:
                        self.answer_buttons[i][self.scores[self.current_question + i]].setChecked(True)
            else:
                self.question_labels[i].setText("")  # Очистить метку, если нет вопросов
                for btn in self.answer_buttons[i]:
                    btn.setText("")  # Очистить текст кнопок

    def next_question(self):
        scores_for_set = []
        all_answered = True

        for i in range(self.questions_per_set):
            score = None
            for j in range(4):
                if self.answer_buttons[i][j].isChecked():
                    score = j
                    break

            if score is None:
                all_answered = False
                break
            scores_for_set.append(score)

        if not all_answered:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, ответьте на все вопросы перед продолжением.")
            return

        # Сохраняем результаты для текущего набора вопросов
        self.scores.extend(scores_for_set)

        self.current_question += self.questions_per_set
        if self.current_question < len(questions):
            self.load_questions()
        else:
            self.show_result()

    def show_result(self):
        total_score = sum(self.scores)
        result_text = ""
        if total_score < 9:
            result_text = "Отсутствие депрессивных симптомов."
        elif total_score < 19:
            result_text = "Легкая депрессия."
        elif total_score < 30:
            result_text = "Умеренная депрессия."
        else:
            result_text = "Явно выраженная депрессивная симптоматика."

        QMessageBox.information(self, "Результат", f"Ваш суммарный балл: {total_score}\n{result_text}")
        self.close()






