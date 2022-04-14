from importlib.util import module_for_loader


class Carro:
    def __init__(self, marcam, modelo, placa, ano):
        self.marca = marcam
        self.modelo = modelo 
        self.placa = placa
        self.ano = ano

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def comprar_carro(self, carro):
        self.carro = carro

meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)                            # imprime: João
print('Modelo do meu carro: ', eu.carro.modelo)         # imprime :Gol
print('Placa do meu carro: ', eu.carro.placa)           # imprime: AAA-1111


    