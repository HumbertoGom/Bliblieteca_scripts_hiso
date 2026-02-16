# class Animal:
#     def __init__(self,nome):
#         self.nome = nome
#     def falar():
#         raise ImportError

# class cachorro(Animal):
#     def falar(self):
#         print('au au')

# class gato(Animal):
#     def falar(self):
#         print('miau miau')


# g1 = gato('shampoo')
# g1.falar()
# c1 = cachorro('rush' )
# c1.falar()

class aluno():
    contagem = 0

    def __init__(self):
        ...
        aluno.contagem += 1
    @classmethod
    def total_alunos(cls):
        print({cls.contagem}, cls.contagem**2)


osaka = aluno()
chiyo = aluno()
eliwood = aluno()
vanderwalls= aluno()
bojack_unbound = aluno()
wild_battle_RB = aluno()


aluno.total_alunos()