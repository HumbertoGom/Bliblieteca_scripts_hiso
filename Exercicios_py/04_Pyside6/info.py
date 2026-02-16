from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

class Info(QLabel):
    def __init__(self,text : str, parent : QWidget | None = None)-> None:
        super().__init__(text,parent)

    def configSetStyle(self):
        self.setStyleSheet(f'fonte-size: 10')
        self.alignment(Qt.AlignmentFlag.AlignRight)