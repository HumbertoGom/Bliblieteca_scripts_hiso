from PySide6.QtWidgets import (
    QWidget,
     QMainWindow,QLabel,QVBoxLayout,QMessageBox
)
from PySide6.QtGui import QIcon
import sys
from PySide6.QtCore import Slot
from variables import WINDOW_ICON_PATH


class MainWindow(QMainWindow):
    def __init__(self, parent : QWidget | None = None,*args,**kwargs) -> None:
        super().__init__(parent, *args , **kwargs)

        #layout basico
        self.cw= QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)


        self.setCentralWidget(self.cw)

        self.setWindowTitle('Coloque o título')

        

        #ultima coisa a ser feita
        self.setFixedSize(self.width()+100,self.height()+100)

    def addWidgetToVLayout(self,Widget : QWidget):
        self.v_layout.addWidget(Widget)
    
    def makeMsgBox(self):
        return QMessageBox(self)