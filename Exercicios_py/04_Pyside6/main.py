from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget,
    QGridLayout, QMainWindow,QLabel,QVBoxLayout
)
import sys
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from info import Info
from styles import setupTheme
from buttons import Button,ButtonsGrid

from display import Display

def temp_label(texto):
    label1= QLabel(texto)
    label1.setStyleSheet('font-size: 150px;')
    return label1

if __name__ == '__main__':

    #cria a aplicacação
    app = QApplication(sys.argv)
    setupTheme(app)
    window=MainWindow()  #importado

    #titulo
    window.setWindowTitle('Calculadora')

    #icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #info 
    info = Info('2.0 ^10.0 = 1024.0')
    window.addWidgetToVLayout(info)

    #display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display,info,window)
    window.v_layout.addLayout(buttonsGrid)

    #Executar

    window.show()
    app.exec() 
    print('linha final')  
