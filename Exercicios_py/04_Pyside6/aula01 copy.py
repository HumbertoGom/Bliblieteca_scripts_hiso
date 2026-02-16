from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget,
    QGridLayout, QMainWindow
)
import sys


app = QApplication(sys.argv)

window = QMainWindow()

central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela')

layout = QGridLayout()
central_widget.setLayout(layout)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px;')

botao2 = QPushButton('DOOMGUY DO MEXICO')
botao2.setStyleSheet('font-size: 80px;')

layout.addWidget(botao, 1, 1)
layout.addWidget(botao2, 2, 1, 1, 2)


# status bar
status_bar = window.statusBar()
status_bar.showMessage('This is a message from lord nergal')

#slot exemple
def slot_exemple(sb):
    sb.showMessage('o meu slot foi executado')

#menu bar
menu = window.menuBar()
primeiro_menu = menu.addMenu('primeiro menu ')
primeira_acao = primeiro_menu.addAction('Primeira ação ')
primeira_acao.triggered.connect(lambda: slot_exemple(status_bar)) #type:ignore




window.show()              
sys.exit(app.exec())       
