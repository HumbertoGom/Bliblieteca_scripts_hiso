from typing import TYPE_CHECKING
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import isEmpty, isNumOrDot, isValidNumber,converToNumber
from variables import MEDIUM_FONT_SIZE
import math


if TYPE_CHECKING:
    from info import Info
    from display import Display
    from main_window import MainWindow

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
#        self.setCheckable(True)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display,info : Info,window: MainWindow, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInintialValue = 'Sua Conta'
        self._makeGrid()
        self.equation = '1-1'
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInintialValue
      
      
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
    
    

        
        
    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)
        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, colNumber)
                slot = self._makeSlot(self._insertToDisplay,buttonText,)
                self._connectButtonClicked(button,slot)

    def _connectButtonClicked(self,button,slot):
        button.clicked.connect(slot)  # type: ignore

    def _configSpecialButton(self,button):
        text= button.text()


        if text in '+-/*^':
            self._connectButtonClicked(
                button,
            self._makeSlot(self._configLeftOp, text))

        if text == 'D':
            slot = self._connectButtonClicked(button, self.display.backspace)

        if text == 'C':
            slot = self._makeSlot(self._clear)
            self._connectButtonClicked(button,slot)

        if text =='+/-':
            slot = self._connectButtonClicked(button, self._invertNumber)

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
    
    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            return
        newNumber = converToNumber(displayText) * -1
        self.display.setText(str(newNumber))
        self.display.setFocus()

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.display.clear()
        self.equation = self._equationInintialValue
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self,text):
        displayText = self.display.text()
        self.display.clear()
        #se o usuario clicou sem apertar qualquer numero
        if not isValidNumber(displayText) and self._left is None:
            self._showError('voçê não digitou nada')
            return

        #tem um núemero válido na esquerda
        if self._left is None:
            self._left = float(displayText)
        
        self._op = text
        self.equation  = f'{self._left} {self._op} ??'
        self.display.setFocus()

    @Slot()
    def _eq(self):
        displayText = self.display.text()
        if not isValidNumber(displayText) or self._left is None:
            print('sem nada para direita')
            self._showError('voçê não digitou o outro número')
            return
        self._right=float(displayText)
        self.equation = f'{self._left}{self._op}{self._right}'
        print(self.equation)
        result ='error'

        try:
            if '^' in self.equation:
                result = math.pow(self._left,self._right)
                result = converToNumber(str(result))
            else:
                result= eval(self.equation)
            print(result)
        except ZeroDivisionError:
            result = ''
            self._showError('voçê dividiu por 0')
        except OverflowError:
            self._showError('número grande demais na memória')
        


        self.display.clear()
        self._insertToDisplay(str(result))
        self.info.setText(f'{self.equation}= {result}')
        self._left = result
        self._right = None
        self.display.setFocus()


        if result == 'error':
            self._left = None
        
    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _showError(self,text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setInformativeText(' ive come to make an announcmenent shadow the hedgehog is a bitch ass mother fucker he pissed on my fucking wife,thats right...')
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.setStandardButtons(msgBox.StandardButton.Ok |
                                  msgBox.StandardButton.Cancel)

        result = msgBox.exec()

        if result == msgBox.StandardButton.Ok:
            print('usario cliclou em OK')
        elif result == msgBox.StandardButton.Cancel:
            print('usario cliclou em Cancel')
    
    def _showInfo(self,text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
#        msgBox.setInformativeText(' ive come to make an announcmenent shadow the hedgehog is a bitch ass mother fucker he pissed on my fucking wife,thats right...')
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
 