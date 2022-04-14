class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

class ImovelNovo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def calcular_preco(self):
        return self.preco + self.adicional

class ImovelVelho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def calcular_preco(self):
        return self.preco - self.desconto

imovel = Imovel("Rua Silva, 123", 300000.0)
imovel_novo = ImovelNovo("Rua Joaquim, 999", 250000.0, 20000.0)
imovel_velho = ImovelVelho("Av. Brasil, 777", 500000.0, 35000.0)

print(imovel.endereco)                                      # Rua Silva, 123
print('Preço:', imovel.preco)                               # 300000.0

print(imovel_novo.endereco)                                 # Rua Joaquim, 999
print('Preço:', imovel_novo.preco)                          # 250000.0
print('Preço Atualizado:', imovel_novo.calcular_preco())    # 270000.0

print(imovel_velho.endereco)                                # Av. Brasil, 777
print('Preço:', imovel_velho.preco)                         # 500000.0
print('Preço Atualizado:', imovel_velho.calcular_preco())   # 465000.0

