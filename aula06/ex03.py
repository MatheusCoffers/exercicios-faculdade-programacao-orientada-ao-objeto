'''
Nome da classe
    ContaBancaria
Atributos:
    numero
    titular
    senha
    saldo (deve ser inicializado no construtor com o valor zero)
Métodos:
    __init__(self, numero, titular, senha)
    depositar(self, valor, senha)
    sacar(self, valor, senha)
'''
class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0

    def depositar(self,valor,senha):
        if(senha == self.senha):
            self.saldo += valor
        else:
            print('Senha incorreta')

    def sacar(self,valor,senha):
        if(senha == self.senha):
            self.saldo -= valor
        else:
            print('Senha incorreta')

conta1 = ContaBancaria(123, 'Matheus Coffers', 4496)

conta1.depositar(20, 4496)
conta1.sacar(10, 4496)

print(conta1.saldo)