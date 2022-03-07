"""
Preencha um dicionário com os dados de 5 alunos.
Utilize o ra do aluno como chave e uma lista de três notas como valor.
Solicite os dados ao usuário.
Percorra o dicionário e exiba a média de cada aluno.

Exemplo:
Veja um exemplo da estrutura do dicionário.
{1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}

"""
notas = {}

for i in range (5):
    lista = []
    ra = input('Digite se ra: ')
    for i2 in range(3):
        nota = int(input('Digite sua nota: '))
        lista.append(nota)
    notas[ra] = lista

for item in notas:
    soma = 0
    for i3 in range(3):
        soma += notas[item][i3]
    print(f'A média do aluno de ra {item} é {soma/3}')


        
    




    
