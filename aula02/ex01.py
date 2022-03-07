valores = []
for i in range(10):
    n = input('Digite um valor: ')
    valores.append(int(n))
    

print('o maior número da lista')
print(max(valores))

print('o menor número da lista')
print(min(valores))

print('a quantidade de números pares contidos na lista')
qtd_pares = 0
for item in valores:
    if (item % 2 == 0):
        qtd_pares = qtd_pares + 1
print(qtd_pares)

print('a média dos números contidos na lista')
media = sum(valores)/len(valores)
print(media)

print('todos os números menores do que a média calculada no item anterior')
for item in valores:
    if item < media:
        print(item)