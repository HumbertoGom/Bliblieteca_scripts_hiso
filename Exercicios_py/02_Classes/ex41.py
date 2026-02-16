# class retangulo:
#     def __init__(self,largura,altura):
#         self.largura = largura
#         self.altura = altura
#     def area(self):
#         return (self.largura*self.altura)
#     def perimetro(self):
#         return(2* self.largura+2*self.altura)
        
# r1 = retangulo(30,40)
# print(r1.area())
# print(r1.perimetro())

# class contabancar():
#     def __init__(self,titular,saldo):
#         self.titular = titular
#         self.saldo = saldo
#     def depositar(self, deposito):
#         self.saldo += deposito
#         print(f'valor de {deposito} depositado com sucesso')
#     def sacar(self,saque):
#         if (self.saldo - saque) < 0:
#             print('Não é possivel sacar essa quantidade')
#         elif (self.saldo - saque >= 0):
#             self.saldo -= saque
#             print('saque efeituado com sucesso')
#     def estado(self):
#         print(f'a conta bancaria de {self.titular} tem {self.saldo} de saldo')


# c1 = contabancar('naruto', 0.001)
# c1.depositar(500)
# c1.sacar(300)
# c1.estado()
# c1.sacar(200)
# c1.estado()
# print('quem ta roubando 1.10^-12 centavos?')


class carro:
    def __init__(self,modelo,ano,velocidade):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
    def acelerar(self):
        self.velocidade+=10
    def frear(self):        
        self.velocidade -=10
        if self.velocidade < 0:
            self.velocidade = 0
    def estado(self):
        print(f'o carro {self.modelo} {self.ano} esta com a velocidade de {self.velocidade}Km/h')

c1= carro('fiat UNO',1995,35)
c1.frear()
c1.frear()
c1.frear()
c1.estado()
c1.frear()
c1.estado()