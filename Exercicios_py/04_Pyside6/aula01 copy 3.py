from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget,
    QGridLayout, QMainWindow
)
import sys
from PySide6.QtCore import Slot

app = QApplication(sys.argv)

class MyWindows(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

    
        #botao
        self.botao1 = QPushButton('Texto do botão')
        self.botao1.setStyleSheet('font-size: 40px;')
        self.botao1.clicked.connect(self.outro_slot)

        self.botao2 = QPushButton('DOOMGUY DO MEXICO')
        self.botao2.setStyleSheet('font-size: 80px;')

        self.layout = QGridLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela')
        self.central_widget.setLayout(self.layout)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('This is a message from lord nergal')

        
        self.layout.addWidget(self.botao1, 1, 1)
        self.layout.addWidget(self.botao2, 2, 1, 1, 2)
        

        #menu bar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('primeiro menu ')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação ')
        self.primeira_acao.triggered.connect(lambda: slot_exemple(status_bar)) #type:ignore

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação ')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.outro_slot)
        self.segunda_acao.hovered.connect(self.outro_slot)

    @Slot()
    def outro_slot(self,checked):
        print(f'esta marcado? {checked}')

    @Slot()
    def slot_exemple(self):
        self.showMessage('o meu slot foi executado')


window = MyWindows()



window.show()              
sys.exit(app.exec())       

#slot exemple



@Slot()
def outro_slot(self,checked):
    print(f'esta marcado? {checked}')

@Slot()
def terceiro_slot(self,action):
    def inner():
        self.outro_slot(action.isChecked())
    return inner




