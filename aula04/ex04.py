'''
Crie um dicionário para armazenar uma listagem de alunos. 
Utilize como chave o RA do aluno e como valor o nome do aluno.
a - Os dados devem ser informados pelo usuário
b - O RA de cada aluno deve ser composto por um número inteiro de exatamente 7 dígitos.
c - aso o RA informado não esteja no formato correto, deve ser gerada uma exceção do tipo ValueError (utilize a instrução raise).
Caso o RA informado já exista no dicionário, deve ser gerada uma exceção do tipo TypeError (utilize a instrução raise).
'''

alunos = {}
for i in range(5):
    try:
        ra = int(input('RA: '))
        if (len(str(ra))) != 7:
            raise ValueError
        if ra in alunos:
            print('[ERRO]')

        nome = input('Nome: ')
        alunos[ra] = nome
    except ValueError:
        print('[ERRO] O RA do aluno deve conter 7 dígitos')
    
       

print(alunos)

