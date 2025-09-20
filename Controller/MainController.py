from PySide6.QtWidgets import QApplication

from View.UI import UI


class MainController:
    def __init__(self):
        self.app = QApplication([])
        self.ui = UI(self)
        self.ui.SetupMainWindow()
