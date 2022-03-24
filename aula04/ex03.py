'''
Preencha uma lista com 5 nomes de pessoas, informados pelo usuário.
Criar uma função que recebe como parâmetro de entrada a lista e uma posição (índice) dessa lista e retorna o nome que está nessa posição. 
Essa função deve gerar e tratar uma exceção do tipo IndexError caso o índice não exista na lista.
'''
lista = []

def preencher_lista():
    for i in range(5):
        a = input('Digite um nome: ')
        lista.append(a)

def percorrer_lista(lista,index):
    try:
        return lista[index]
    except IndexError:
        print('O índice informado não está na lista')

preencher_lista()

indice = int(input('Digite um indice para essa lista'))
print(percorrer_lista(lista,indice))