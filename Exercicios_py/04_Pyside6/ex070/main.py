from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtCore import QObject,Signal,Slot,QThread
from ui_worker import Ui_Form
import time
import sys


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = 0
        self.started.emit(str(value))
        for i in range(5):
            value+=1
            self.progressed.emit(str(value))
            print(i)
            time.sleep(1)
        self.finished.emit(str(value))
        
    
 
class MyWidget(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.Button1.clicked.connect(self.hardWork1)
        self.Button2.clicked.connect(self.hardWork2)

    
 
    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        thread.start()

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('worker 2 iniciado')

    def worker2Progressed(self, value):
        self.label2.setText(value)
        print('2 em progresso')

    def worker2Finished(self, value):
        self.label2.setText(value)
        self.button2.setDisabled(False)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()
        worker = self._worker
        thread =  self._thread 

        #mover worker para thread
        worker.moveToThread(thread)

        #Run
        thread.started.connect(worker.doWork)

        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater) #limpar da memória
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        thread.start()

    def worker1Started(self,value):
        print('worker iniciado')
        self.Label1.setText(value)
        self.Button1.setDisabled(True)

    def worker1Progressed(self,value):
        print('em progresso')
        self.Label1.setText(value)

    def worker1Finished(self,value):
        print('worker terminado')
        self.Label1.setText(value)
        self.Button1.setDisabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()