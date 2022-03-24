nome = input('Digite seu nome: ')
salario = float(input('Digite seu salario: '))
taxa = float(input('Digite o aumento do salario em %: ')) / 100

#definição de classe
class Funcionario():
    #metodo construtor
    def __init__(self,nome,salario):
        self.nome = nome 
        self.salario = salario
        
    def aumentar_salario(self,taxa):
        self.salario += self.salario * taxa

#instanciando objeto
funcionario = Funcionario(nome, salario)

funcionario.aumentar_salario(taxa)
print(funcionario.salario)


