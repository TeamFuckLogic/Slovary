import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class InitialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.label = QLabel("Python | Списки")
        self.label.setStyleSheet("font-size: 18px; font: bold")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
# Теория по спискам
        self.explanation_label = QLabel("")
        self.explanation_label.setStyleSheet("font-size: 14px;")

        self.start_button = QPushButton("Проверить знания по теме")

        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignLeft)
        layout.addWidget(self.explanation_label, alignment=Qt.AlignLeft)
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def connects(self):
        self.start_button.clicked.connect(self.start_test)

    def set_appear(self):
        self.setWindowTitle("Python | Списки")
        self.resize(700, 600)
        self.move(100, 100)

    def start_test(self):
        from questions import QuestionsWindow
        self.hide()
        self.questions_window = QuestionsWindow()
        self.questions_window.show()