'''
Nome da classe
    Aluno
Atributos:
    ra
    nome
    turma
    notas (lista que deve ser inicializada como vazia)
Métodos:
    __init__(self, ra, nome, turma)
    inserir_nota(self, nota)
    calcular_media(self)

Crie 3 objetos da classe aluno. Insira algumas notas para os alunos.
Insira os objetos em uma lista.
Percorra a lista, calcule e exiba a média aritmética de cada aluno.
'''
class Aluno():
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []
    
    def inserir_nota(self,nota):
        if (nota >= 0 and nota <= 10):
            self.notas.append(nota)
            print('Nota aplicada com sucesso!!')
        else:
            print('Nota Inválida!!')
    
    def calcular_media(self):
        media = sum(self.notas)/len(self.notas)
        return media

aluno1 = Aluno(1234567, 'Paulo', 'SI2A')
aluno2 = Aluno(5678789, 'Maria', 'SI2A')
aluno3 = Aluno(5555666, 'João', 'SI2A')


aluno1.inserir_nota(9)
aluno1.inserir_nota(6)

aluno2.inserir_nota(8)
aluno2.inserir_nota(7)

aluno3.inserir_nota(9.5)

print(aluno1.notas)
print(aluno2.notas)
print(aluno3.notas)

alunos = [aluno1, aluno2, aluno3]

for aluno in alunos:
    print(f'o aluno {aluno.nome} ficou com média {aluno.calcular_media()}')
