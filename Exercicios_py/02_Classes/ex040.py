class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f'Ola me chamo{self.nome} e tenho {self.idade} anos')
    
yoshikage= Pessoa('yoshikage',33)

yoshikage.apresentar()