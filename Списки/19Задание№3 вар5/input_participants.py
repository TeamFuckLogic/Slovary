import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class ParticipantInput(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ввод количества участников')
        layout = QVBoxLayout()

        self.label = QLabel('Введите количество участников:')
        self.input = QLineEdit()
        self.button = QPushButton('Далее')
        self.button.clicked.connect(self.submit)

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def submit(self):
        try:
            count = int(self.input.text())
            if count > 0:
                self.close()
                self.openParticipantDataWindow(count)
            else:
                self.label.setText("Введите положительное число!")
        except ValueError:
            self.label.setText("Введите корректное число!")

    def openParticipantDataWindow(self, count):
        from input_data import ParticipantData
        self.participantDataWindow = ParticipantData(count)
        self.participantDataWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ParticipantInput()
    window.show()
    app.exec_()


