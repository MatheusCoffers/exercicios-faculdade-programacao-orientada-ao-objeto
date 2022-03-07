print('lista 1')
lista1 = []
for i in range(3):
    n = input('Digite um valor: ')
    lista1.append(int(n))

print('lista 2')
lista2 = []
for i in range(3):
    n = input('Digite um valor: ')
    lista2.append(int(n))

lista=[]

for i in range(3):
    lista.append(lista1[i])
    lista.append(lista2[i])

print(lista)

