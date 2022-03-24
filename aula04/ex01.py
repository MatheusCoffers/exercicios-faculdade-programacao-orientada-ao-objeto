'''
Nesta questão você deve identificar as partes problemáticas do código e reescrevê-lo utilizando tratamento de exceções. 
Ou seja, devem ser identificadas todas as exceções que podem ser geradas e, para cada uma, deve ser dado o tratamento adequado que, nesse exercício, significa alertar o usuário quanto ao problema. 

x = int(input('Primeiro valor:'))
y = int(input('Segundo valor:'))
z = x / y
print('O resultado da divisão é:', z)
'''
try: 
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z = x / y

except ZeroDivisionError:
    print('não dá pra dividir por zero')

except ValueError:
    print('Digite valores válidos')
else:
    print('O resultado da divisão é:', z)

