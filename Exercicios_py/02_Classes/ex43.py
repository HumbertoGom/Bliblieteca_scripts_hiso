# class contabancaria:
#     def __init__(self, _saldo):
#         self._saldo = _saldo
#     @property
#     def saldo(self):
#         return self._saldo
    
#     @saldo.setter
#     def saldo(self, novosaldo):
#         if novosaldo<0:
#             print('erro não pode ter saldo negativo')
#         else:
#             self._saldo = novosaldo
        
# conta = contabancaria(100)
# print(conta._saldo)
# conta.saldo = 500
# print(conta._saldo)

# class endereco():
#     def __init__(self,rua,numero,cidade):
#         self.rua = rua
#         self.numero = numero
#         self.cidade = cidade
# class pessoa():
#     def __init__(self,nome,idade,endereco):
#         self.nome = nome
#         self.idade = idade
#         self.endereco = endereco
#     def falar(self):
#         print(f'meu nome é {self.nome} e moro na {self.endereco.rua} de {self.endereco.cidade} tem {self.idade} anos')
    
# morioh= endereco('nordeste',143,'morioh')
# kira = pessoa('yoshikage',33,morioh)
# kira.falar()

GASES_IDEAIS_SI= 8.314

class funcionario():
    def __init__(self,nome,cargo,salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario 
    @classmethod
    def criar_gerente(cls,nome):
        return cls(nome,'gerente',10000)
    
funcionario.criar_gerente('Jonny') # eu tinha outro nome mente, em um aniversario anterior a 2016 brandão, tinha chamado um gato(eu acho) de um nome ingles como esse, nos meninos ficavamos repetindo esse nome e as garotas confusas, bons tempos quando eu era parte da sociedade; eu tinha lembrando desse nome hoje mais cedo 6/6/2025


        