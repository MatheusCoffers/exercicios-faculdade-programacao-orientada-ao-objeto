# ALUNO 1: Gabriel Áquila Santos Silva
# ALUNO 2: Gabriel Magalhaes Fontes
# ALUNO 3: Aline de oliveira silva
# ALUNO 4: Lucas gomes do prado
# ALUNO 5: Matheus Denobile Coffers
# ALUNO 6: Ester barbosa gomes


'''
Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada
uma lista e dois itens e retorna True, se os dois itens estiverem
armazenado na lista, e False, caso contrário.
'''
lista = [1, 2, 3, 4, 5]
def pertence(lista, item1, item2):
    if item1 and item2 in lista:
        return True       
    else:
        return False

print(pertence(lista,1,6))

'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada
uma lista e dois itens (velho e novo) e retorna uma lista onde todas as
ocorrências do item velho são substituídas pelo item novo.
'''
lista= [1, 2, 3, 1, 2, 3, 1, 2, 3]

def substituir(lista, velho, novo):
    i = 0
    for i in range(len(lista)):
        if(velho == lista[i]):
            lista.pop(i)
            lista.insert(i,novo)
    return lista

print(substituir(lista, 2, 5))
    
'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''

tupla = (1, 2, 3, 2, 3, 2)

def posicoes(tupla, item):
    lista = []
    i = 0
    for i in range(len(tupla)):
        if item == tupla[i]:
            lista.append(i)
    return lista

print(posicoes(tupla, 3))

'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'reprovados' que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos reprovados.
Considere que o aluno é reprovado se a média das suas notas é inferior a 6.
Caso nenhum aluno seja reprovado, deve retornar uma lista vazia.
'''
alunos = {
    'gabriel' : [4, 5, 6],
    'matheus' : [2, 5, 7],
    'aline' : [5, 6, 8]
}

def reprovados(alunos):
    lista = []
    for item in alunos:
        media = 0
        i = 0
        for i in range(len(alunos[item])):
            media += alunos[item][i]
        if media / 3 <= 6:
            lista.append(item)
    return(lista)
print(reprovados(alunos))
        


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos de
entrada o dicionário e o nome de um aluno. A função deve excluir a primeira
nota desse aluno e retornar o dicionário com as alterações realizadas.
Se o aluno não existir no dicionário, deve retornar o dicionário sem alterações
'''
alunos = {
    'gabriel' : [4, 5, 6],
    'matheus' : [2, 5, 7],
    'aline' : [5, 6, 8]
}

def excluir_nota(alunos, nome):
    for item in alunos:
        if nome == item:
            alunos[nome].pop(0)
    return alunos
print(excluir_nota(alunos,'x'))


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada maior_nota que recebe como argumentos
de entrada o dicionário e retorna outro dicionário com o nome e a maior nota
de cada aluno.
'''
alunos = {
    'gabriel' : [4, 5, 6],
    'matheus' : [2, 5, 7],
    'aline' : [5, 6, 8]
}

def maior_nota(alunos):
    alunos_novo = {}
    for item in alunos:
        alunos[item].sort(reverse = True)
        nota = alunos[item][0]
        alunos_novo[item] = nota
    return alunos_novo
print(maior_nota(alunos))
