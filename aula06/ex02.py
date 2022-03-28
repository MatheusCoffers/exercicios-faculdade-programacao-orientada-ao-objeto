'''
Nome da classe
    Funcionario
Atributos:
    nome
    sobrenome
    salario_mensal
Métodos:
    __init__(self, nome, sobrenome, salario_mensal)
        O construtor deve fazer uma validação do salario_mensal,
        e se o salário mensal não for positivo, deve configurá-lo como zero.
    aumentar_salario(self)
        Aumenta o salario do funcionário em 10%
'''
class Funcionario():
    def __init__(self, nome, sobrenome, salario_mensal):
        self.nome = nome
        self.sobrenome = sobrenome
        if(salario_mensal<0):
            self.salario_mensal = 0
        else: 
            self.salario_mensal = salario_mensal
    def aumentar_salario(self):
        self.salario_mensal *= 1.1

funcionario1 = Funcionario('Matheus', 'Coffers', 4500)
funcionario2 = Funcionario('Lucas', 'Denobile', 2000)

funcionario1.aumentar_salario()
funcionario2.aumentar_salario()