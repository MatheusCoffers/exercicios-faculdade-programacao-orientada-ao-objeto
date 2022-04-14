# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Matheu Denobile Coffers
# ALUNO 2: Thamiris Arce Bezerra da Silva
# ALUNO 3: Gabriel Magalhães Fontes
# ALUNO 4: Ester Barbosa Gomes


class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_maerial = 147.0
        self.__valor_fixo_letra = 0.35
        self.__valor_total = 0

    def get_valor_total(self):
        area = self.altura * self.largura
        custo_material = area * self.__valor_fixo_maerial
        num_letras = len(self.frase.replace(" ", ""))
        custo_desenho = num_letras * self.__valor_fixo_letra
        valor_placa = custo_material + custo_desenho
        return valor_placa


class Historico:
    def __init__(self):
        self.__pedidos = []

    def inserir_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def calcular_faturamento(self):
        faturamento = 0
        for i in range(len(self.__pedidos)):
            faturamento += self.__pedidos[i].get_valor_total()
        return faturamento
