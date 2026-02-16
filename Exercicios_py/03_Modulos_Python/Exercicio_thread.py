

from time import sleep

from threading import Thread
'''
class MeuThread(Thread):
    def __init__(self,texto,tempo):
        self.texto= texto
        self.tempo= tempo
        super().__init__()
    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1= MeuThread('Thread 1', 2 )
t1.start()


t2= MeuThread('Thread 2', 3 )
t2.start()


t3= MeuThread('Thread 3', 5 )
t3.start()
for i in range(20):
    print(i)
    sleep(i)
'''

'''
def vai_demorar(texto,tempo):
    sleep(tempo)
    print(texto)

t= Thread(target=vai_demorar,args=('ola mundo',5))

t.start()


while t.is_alive():
    print('esperando a thread')
    sleep(2)
'''

class Ingressos:
    def __init__(self,estoque):
        self.estoque = estoque
    def comprar(self,quantidade):
        if self.estoque < quantidade:
            print('não temos ingresos ')
            return
        self.estoque -= quantidade
        print(f'voçê comprou {quantidade} ingressos\n ainda temos {self.estoque} em estoque' )

    

Ing = Ingressos(10)
for i in range(1,20):
    t = Thread(target=Ing.comprar,args=(i,))
