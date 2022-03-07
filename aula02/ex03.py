print('lista 1')
lista1 = []
for i in range(5):
    n = input('Digite um valor: ')
    lista1.append(int(n))

print('lista 2')
lista2 = []
for i in range(5):
    n = input('Digite um valor: ')
    lista2.append(int(n))

tupla1 = tuple(lista1)
tupla2 = tuple(lista2)

tupla = tupla1 + tupla2

print(tupla)