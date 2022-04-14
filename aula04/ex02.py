'''
O código abaixo lança uma exceção e interrompe a execução do programa. 
Utilizando tratamento de exceções, corrija o programa com o objetivo de alertar o usuário sobre o erro ocorrido, e impedir que o programa seja interrompido bruscamente.

def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(15):
        print(lista[i])
    print('Fim da função')
 
print('Início do programa')
funcao_1()
print('Fim do programa')

'''

from ast import Index


def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        for i in range(15):
            print(lista[i])         
    except IndexError:
        print('indice não encontrado')
    print('Fim da função')e

 
print('Início do programa')
funcao_1()
print('Fim do programa')
    
