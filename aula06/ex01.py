'''
Nome da classe
    Carro
Atributos:
    marca
    modelo
    placa
Métodos:
    __init__(self, marca, modelo, placa)
    exibir_dados(self)

No programa principal, crie dois objetos da classe Carro.
Utilize o método exibir_dados para exibir os atributos de cada carro.
'''

class Carro():
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
    
    def exibir_dados(self):
        print(f'a marca é: {self.marca}')
        print(f'o modelo é: {self.modelo}')
        print(f'a placa á: {self.placa}')
        print('--------------------------------------------------')

carro1 = Carro('Chevrollet', 'Spin', 'FFS4414')
carro2 = Carro('Volksvagem', 'Fox', 'DRJ0126')

carro1.exibir_dados()
carro2.exibir_dados()