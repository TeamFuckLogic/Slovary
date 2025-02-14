import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QApplication

class StudentInfoWindow(QWidget):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Информация о студенте")
        self.resize(300, 150)
        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("ФИО")
        layout.addWidget(self.name_input)

        self.group_input = QLineEdit(self)
        self.group_input.setPlaceholderText("Группа")
        layout.addWidget(self.group_input)

        submit_button = QPushButton("Начать тест")
        submit_button.clicked.connect(self.submit_info)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submit_info(self):
        name = self.name_input.text()
        group = self.group_input.text()
        if name and group:
            self.callback(name, group)
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")

def start_app():
    app = QApplication(sys.argv)
    def open_test_window(name, group):
        test_window = TestWindow(name, group)
        test_window.show()

    student_info_window = StudentInfoWindow(open_test_window)
    student_info_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start_app()