import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class FinalWindow(QWidget):
    def __init__(self, score, total):
        super().__init__()
        self.score = score
        self.total = total
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Результаты теста")
        self.resize(300, 200)
        layout = QVBoxLayout()
        result_label = QLabel(f"Вы ответили правильно на {self.score} из {self.total} вопросов.")
        layout.addWidget(result_label)
        exit_button = QPushButton("Закрыть")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    score = 3 
    total = 5 
    final_window = FinalWindow(score, total)
    final_window.show()
    sys.exit(app.exec_())