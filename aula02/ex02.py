valores = []
for i in range(10):
    n = input('Digite um valor: ')
    valores.append(int(n))

valores_pares = []
valores_impares = []


for item in valores:
    if (item % 2 == 0):
        valores_pares.append(item)
    else:
        valores_impares.append(item)

print(f'valores pares: {valores_pares}')
print(f'valores impares: {valores_impares}')