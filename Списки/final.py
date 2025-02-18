import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class FinalWindow(QWidget):
    def __init__(self, name, group, score, total, elapsed_time):
        super().__init__()
        self.name = name
        self.group = group
        self.score = score
        self.total = total
        self.elapsed_time = elapsed_time 
        self.initUI()

    def calculate_grade(self):
        if self.score >= 0 and self.score <= 3:
            return 2
        elif self.score >= 4 and self.score <= 7:
            return 3
        elif self.score >= 8 and self.score <= 11:
            return 4
        elif self.score == 12:
            return 5
        else:
            return None 

    def initUI(self):
        self.setWindowTitle("Итоги теста") 
        self.resize(300, 300)  
        layout = QVBoxLayout()
        
        result_label = QLabel(f"Вы ответили правильно на {self.score} из {self.total} вопросов.")
        grade = self.calculate_grade()
        grade_label = QLabel(f"Ваша оценка: {grade}")
        
        time_label = QLabel(f"Время прохождения: {self.elapsed_time}")  
        
        criteria_label = QLabel("Критерии оценки:\n"
                                "0-3 правильных ответа: оценка 2\n"
                                "4-7 правильных ответов: оценка 3\n"
                                "8-13 правильных ответов: оценка 4\n"
                                "14-15 правильных ответов: оценка 5")
        
        layout.addWidget(result_label)
        layout.addWidget(grade_label)
        layout.addWidget(time_label)
        layout.addWidget(criteria_label) 
        
        exit_button = QPushButton("Закрыть")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)
        self.setLayout(layout)

        # Записываем результаты в файл
        self.save_results()

    def save_results(self):
        with open("rec.txt", "a") as file:  # Открываем файл в режиме добавления
            file.write(f"\nФИО: {self.name}, Группа: {self.group} \n"
                       f"Правильные ответы: {self.score} \n"
                       f"Всего вопросов: {self.total} \n"
                       f"Время: {self.elapsed_time}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec_())