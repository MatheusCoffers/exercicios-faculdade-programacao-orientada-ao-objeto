"""
Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade de vezes que essa vogal aparece no texto. 
A função deve receber o texto como entrada, e retornar o dicionário.

Exemplo:
Para o texto abaixo:
'faculdade de tecnologia impacta'	

A função deve retornar o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o': 2, 'i': 2}

"""

x = input('digite um texto: ')
x.lower()
letras = list(x)
qntd = [0,0,0,0,0]

vogais = {}
i=0
while(i<len(letras)):
    if letras[i] == 'a':
        qntd[0] += 1
    elif letras[i] == 'b':
        qntd[1] += 1
    elif letras[i] == 'c':
        qntd[2] += 1
    elif letras[i] == 'd':
        qntd[3] += 1
    elif letras[i] == 'e':
        qntd[4] += 1
    
    i += 1

vogais['a'] = qntd[0]
vogais['b'] = qntd[1]
vogais['c'] = qntd[2]
vogais['d'] = qntd[3]
vogais['e'] = qntd[4]

print(vogais)





