from PySide6.QtWidgets import QApplication,QPushButton,QWidget, QVBoxLayout,QGridLayout,QMainWindow
import sys

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px;')
botao.show()

botao2 = QPushButton('DOOMGUY DO MEXICO')
botao2.setStyleSheet('font-size: 80px;')
botao2.show()
#QApplications executa 1 widget por janela

#QWidget - widget genérico
central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao,1,1)
layout.addWidget(botao2,2,1, 1,2 )


central_widget.show()
app.exec()