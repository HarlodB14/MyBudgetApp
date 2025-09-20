from PySide6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel

from Controller import MainController


class UI:
    def __init__(self, maincontroller: MainController):
        self.controller = maincontroller

    def SetupMainWindow(self):
        width = 400
        height = 400
        window = QWidget()
        window.setWindowTitle("Budget App")
        window.setMinimumWidth(width)
        window.setMinimumHeight(height)
        layout = QVBoxLayout()
        label = QLabel("Welkom bij je budget app!")
        button = QPushButton("Voeg een budgetItem toe")
        layout.addWidget(label)
        layout.addWidget(button)
        window.setLayout(layout)
        window.show()
        self.controller.app.exec()
