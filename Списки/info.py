import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("Введите информацию")
        self.resize(400, 200)

        self.name_label = QLabel("ФИО:")
        self.name_input = QLineEdit()

        self.group_label = QLabel("Группа:")
        self.group_input = QLineEdit()

        self.submit_button = QPushButton("Далее")
        self.submit_button.clicked.connect(self.submit_info)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.group_label)
        layout.addWidget(self.group_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_info(self):
        name = self.name_input.text()
        group = self.group_input.text()
        if name and group:
            from test import QuestionsWindow
            self.hide()
            self.questions_window = QuestionsWindow(name, group)
            self.questions_window.show()
        else:
            # Здесь можно добавить обработку ошибок, если поля не заполнены
            print("Пожалуйста, заполните все поля.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InfoWindow()
    sys.exit(app.exec_())