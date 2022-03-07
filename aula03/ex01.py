"""
Preencha um dicionário com as informações de 5 produtos.
Utilize o nome do produto como chave e o preço como valor. 
Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00

Exemplo:
Veja um exemplo da estrutura do dicionário.
{'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0, 'Lápis': 1.50}

"""

produto = {}

for i in range(5):
    nome = input(f'digite o nome do produto {i+1}: ')
    preco = int(input(f'digite o preço do produto {i+1}: '))
    produto[nome] = preco    
    if produto[nome] < 50:
        produto.pop(nome)

print(produto)
