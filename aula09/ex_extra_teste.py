from ex_extra import SuperHeroi, SuperPoder, Personagem, Confronto, Vilao


acertos = 0

# Teste do construtor da classe Superpoder
try:
    # cria os poderes
    poder1 = SuperPoder("soltar teia", 3)
    poder2 = SuperPoder("andar em paredes", 2)
    poder3 = SuperPoder("sentido apurado", 1)
    poder4 = SuperPoder("voar", 3)
    poder5 = SuperPoder("força", 5)
    poder6 = SuperPoder("visão de raio x", 4)
    poder7 = SuperPoder("sopro congelante", 4)
    poder8 = SuperPoder("supersoldado", 3)
    poder9 = SuperPoder("escudo", 3)
    poder10 = SuperPoder("velocidade", 5)
    poder11 = SuperPoder("armadura", 4)
    poder12 = SuperPoder("dispositivos eletrônicos", 2)
    poder13 = SuperPoder("velocidade", 3)
    poder14 = SuperPoder("forca", 3)
    poder15 = SuperPoder("braceletes", 1)
    poder16 = SuperPoder("força", 5)
    poder17 = SuperPoder("mente aguçada", 5)
    poder18 = SuperPoder("voar", 3)
    poder19 = SuperPoder("força", 5)
    poder20 = SuperPoder("visão de raio x", 4)
    poder21 = SuperPoder("sopro congelante", 4)
    poder22 = SuperPoder("tentáculos indestrutíveis", 5)
    poder23 = SuperPoder("velocidade", 1)

    # verifica se os atributos da classe SuperPoder são privados
    assert hasattr(poder1, '_SuperPoder__nome') is True, "Atributo 'nome' não \
é privado"
    assert hasattr(poder1, '_SuperPoder__categoria') is True, "Atributo \
'categoria' não é privado"
except AssertionError as erro:
    print('ERRO...: Construtor da classe SuperPoder:', erro)
except Exception as erro:
    print('ERRO...: Construtor da classe SuperPoder:', erro)
else:
    print('CORRETO: Construtor da classe SuperPoder')
    acertos += 1


# Teste do construtor da Classe Personagem
try:
    # Cria os personagens
    personagem1 = Personagem("Octopus", "Otto Octavius")
    personagem2 = Personagem("Octopus", "Otto Octavius")

    # verifica se os atributos da classe Personagem são privados
    assert hasattr(personagem1, '_Personagem__nome') is True, "Atributo \
'nome' não é privado"
    assert hasattr(personagem1, '_Personagem__nome_vida_real') is True, \
        "Atributo 'nome_vida_real' não é privado"
    assert hasattr(personagem1, '_Personagem__poderes') is True, "Atributo \
'poderes' não é privado"
except AssertionError as erro:
    print('ERRO...: Construtor da classe Personagem:', erro)
except Exception as erro:
    print('ERRO...: Construtor da classe Personagem:', erro)
else:
    print('CORRETO: Construtor da classe Personagem')
    acertos += 1


# Teste do construtor da classe Vilao
try:
    vilao1 = Vilao("Duende-Verde", "Norman Osbourne", 3)
    vilao2 = Vilao("Lex Luthor", "Lex Luthor", 2)
    vilao3 = Vilao("Bizarro", "Bizarro", 1)
    vilao4 = Vilao("Octopus", "Otto Octavius", 5)

    # verifica se o atributo da classe Vilao é público
    assert hasattr(vilao1, 'tempo_de_prisao') is True, "Atributo \
'tempo_de_prisao' não é público"

except AssertionError as erro:
    print('ERRO...: Construtor da classe Vilao:', erro)
except Exception as erro:
    print('ERRO...: Construtor da classe Vilao:', erro)
else:
    print('CORRETO: Construtor da classe Vilao')
    acertos += 1


# Teste do construtor da classe SuperHeroi
try:
    heroi1 = SuperHeroi("Homem-Aranha", "Peter Park")
    heroi2 = SuperHeroi("Super-Homem", "Crark Kent")
    heroi3 = SuperHeroi("Capitão América", "Steven Rogers")
    heroi4 = SuperHeroi("Flash", "Barry Allen")
    heroi5 = SuperHeroi("Homem de Ferro", "Tony Stark")
    heroi6 = SuperHeroi("Mulher-Maravilha", "Diana")
except Exception as erro:
    print('ERRO...: Construtor da classe SuperHeroi:', erro)
else:
    print('CORRETO: Construtor da classe SuperHeroi')
    acertos += 1


# Teste do método get_nome da classe SuperPoder
try:
    assert poder1.get_nome() == "soltar teia", 'Método get_nome incorreto'
    assert poder2.get_nome() == "andar em paredes", 'Método get_nome incorreto'
    assert poder3.get_nome() == "sentido apurado", 'Método get_nome incorreto'
except AssertionError as erro:
    print('ERRO...: Método get_nome da classe SuperPoder:', erro)
except Exception as erro:
    print('ERRO...: Método get_nome da classe SuperPoder:', erro)
else:
    print('CORRETO: Método get_nome da classe SuperPoder')
    acertos += 1


# Teste do método get_categoria da classe SuperPoder
try:
    assert poder1.get_categoria() == 3, 'Método get_categoria incorreto'
    assert poder2.get_categoria() == 2, 'Método get_categoria incorreto'
    assert poder3.get_categoria() == 1, 'Método get_categoria incorreto'
except AssertionError as erro:
    print('ERRO...: Método get_categoria da classe SuperPoder:', erro)
except Exception as erro:
    print('ERRO...: Método get_categoria da classe SuperPoder:', erro)
else:
    print('CORRETO: Método get_categoria da classe SuperPoder')
    acertos += 1


# Teste do método adicionar_super_poder da classe Personagem
try:
    personagem1.adicionar_super_poder(poder1)
    personagem1.adicionar_super_poder(poder5)

    personagem2.adicionar_super_poder(poder5)
    personagem2.adicionar_super_poder(poder10)
    personagem2.adicionar_super_poder(poder20)

    # verifica a quantidade de poderes de cada Personagem
    assert len(personagem1._Personagem__poderes) == 2
    assert len(personagem2._Personagem__poderes) == 3
except AssertionError as erro:
    print('ERRO...: Método adicionar_super_poder da classe Personagem:', erro)
except Exception as erro:
    print('ERRO...: Método adicionar_super_poder da classe Personagem:', erro)
else:
    print('CORRETO: Método adicionar_super_poder da classe Personagem')
    acertos += 1


# Teste da exceção ValueError ao adicionar mais que 4 poderes
try:
    personagem3 = Personagem("Nome", "Nome Real")
    personagem3.adicionar_super_poder(poder1)
    personagem3.adicionar_super_poder(poder2)
    personagem3.adicionar_super_poder(poder3)
    personagem3.adicionar_super_poder(poder4)
    personagem3.adicionar_super_poder(poder5)
except ValueError:
    print('CORRETO: Gerou exceção ValueError ao adicionar mais que 4 \
poderes ao Personagem')
    acertos += 1
except Exception as erro:
    print('ERRO...: Não gerou exceção ValueError ao adicionar mais que \
4 poderes ao Personagem:', erro)
else:
    print('ERRO...: Não gerou exceção ValueError ao adicionar mais que \
4 poderes ao Personagem')


# Teste do método get_poder_total da classe SuperPoder
try:
    assert personagem1.get_poder_total() == 8
    assert personagem2.get_poder_total() == 14
except AssertionError as erro:
    print('ERRO...: Método get_poder_total da classe Personagem:', erro)
except Exception as erro:
    print('ERRO...: Método get_poder_total da classe Personagem:', erro)
else:
    print('CORRETO: Método get_poder_total da classe Personagem')
    acertos += 1


# Teste do método adicionar_super_poder da classe Vilao
try:
    vilao1.adicionar_super_poder(poder16)

    vilao2.adicionar_super_poder(poder17)

    vilao3.adicionar_super_poder(poder18)
    vilao3.adicionar_super_poder(poder19)
    vilao3.adicionar_super_poder(poder20)
    vilao3.adicionar_super_poder(poder21)

    vilao4.adicionar_super_poder(poder22)
    vilao4.adicionar_super_poder(poder23)

    # verifica a quantidade de poderes de cada Vilao
    assert len(vilao1._Personagem__poderes) == 1
    assert len(vilao2._Personagem__poderes) == 1
    assert len(vilao3._Personagem__poderes) == 4
    assert len(vilao4._Personagem__poderes) == 2
except AssertionError as erro:
    print('ERRO...: Método adicionar_super_poder da classe Vilao:', erro)
except Exception as erro:
    print('ERRO...: Método adicionar_super_poder da classe Vilao:', erro)
else:
    print('CORRETO: Método adicionar_super_poder da classe Vilao')
    acertos += 1


# Teste do método get_poder_total da classe Vilao
try:
    assert vilao1.get_poder_total() == 5
    assert vilao2.get_poder_total() == 5
    assert vilao3.get_poder_total() == 16
    assert vilao4.get_poder_total() == 6
except AssertionError as erro:
    print('ERRO...: Método get_poder_total da classe Vilao:', erro)
except Exception as erro:
    print('ERRO...: Método get_poder_total da classe Vilao:', erro)
else:
    print('CORRETO: Método get_poder_total da classe Vilao')
    acertos += 1


# Teste do método adicionar_super_poder da classe SuperHeroi
try:
    heroi1.adicionar_super_poder(poder1)
    heroi1.adicionar_super_poder(poder2)
    heroi1.adicionar_super_poder(poder3)

    heroi2.adicionar_super_poder(poder4)
    heroi2.adicionar_super_poder(poder5)
    heroi2.adicionar_super_poder(poder6)
    heroi2.adicionar_super_poder(poder7)

    heroi3.adicionar_super_poder(poder8)
    heroi3.adicionar_super_poder(poder9)

    heroi4.adicionar_super_poder(poder10)

    heroi5.adicionar_super_poder(poder11)
    heroi5.adicionar_super_poder(poder12)

    heroi6.adicionar_super_poder(poder13)
    heroi6.adicionar_super_poder(poder14)
    heroi6.adicionar_super_poder(poder15)

    # verifica a quantidade de poderes de cada SuperHeroi
    assert len(heroi1._Personagem__poderes) == 3, 'Quantidade de poderes do \
vilao1 está incorreta'
    assert len(heroi2._Personagem__poderes) == 4, 'Quantidade de poderes do \
vilao2 está incorreta'
    assert len(heroi3._Personagem__poderes) == 2, 'Quantidade de poderes do \
vilao3 está incorreta'
    assert len(heroi4._Personagem__poderes) == 1, 'Quantidade de poderes do \
vilao4 está incorreta'
    assert len(heroi5._Personagem__poderes) == 2, 'Quantidade de poderes do \
vilao5 está incorreta'
    assert len(heroi6._Personagem__poderes) == 3, 'Quantidade de poderes do \
vilao6 está incorreta'
except AssertionError as erro:
    print('ERRO...: Método adicionar_super_poder da classe SuperHeroi:', erro)
except Exception as erro:
    print('ERRO...: Método adicionar_super_poder da classe SuperHeroi:', erro)
else:
    print('CORRETO: Método adicionar_super_poder da classe SuperHeroi')
    acertos += 1


# Teste do método get_poder_total da classe SuperHeroi
try:
    assert round(heroi1.get_poder_total(), 2) == 6.6

    assert round(heroi2.get_poder_total(), 2) == 17.6

    assert round(heroi3.get_poder_total(), 2) == 6.6

    assert round(heroi4.get_poder_total(), 2) == 5.5

    assert round(heroi5.get_poder_total(), 2) == 6.6

    assert round(heroi6.get_poder_total(), 2) == 7.7
except AssertionError as erro:
    print('ERRO...: Método get_poder_total da classe SuperHeroi:', erro)
except Exception as erro:
    print('ERRO...: Método get_poder_total da classe SuperHeroi:', erro)
else:
    print('CORRETO: Método get_poder_total da classe SuperHeroi')
    acertos += 1


# Teste do método lutar da classe Confronto
try:
    confronto = Confronto()
    assert confronto.lutar(heroi1, vilao1) == 1, 'heroi1 deve vencer do vilao1'
    assert confronto.lutar(heroi1, vilao2) == 1, 'heroi1 deve vencer do vilao2'
    assert confronto.lutar(heroi1, vilao3) == 2, 'heroi1 deve perder do vilao3'
    assert confronto.lutar(heroi1, vilao4) == 1, 'heroi1 deve vencer do vilao4'

    assert confronto.lutar(heroi2, vilao1) == 1, 'heroi2 deve vencer do vilao1'
    assert confronto.lutar(heroi2, vilao2) == 1, 'heroi2 deve vencer do vilao2'
    assert confronto.lutar(heroi2, vilao3) == 1, 'heroi2 deve vencer do vilao3'
    assert confronto.lutar(heroi2, vilao4) == 1, 'heroi2 deve vencer do vilao4'

    assert confronto.lutar(heroi3, vilao1) == 1, 'heroi3 deve vencer do vilao1'
    assert confronto.lutar(heroi3, vilao2) == 1, 'heroi3 deve vencer do vilao2'
    assert confronto.lutar(heroi3, vilao3) == 2, 'heroi3 deve perder do vilao3'
    assert confronto.lutar(heroi3, vilao4) == 1, 'heroi3 deve vencer do vilao4'

    assert confronto.lutar(heroi4, vilao1) == 1, 'heroi4 deve vencer do vilao1'
    assert confronto.lutar(heroi4, vilao2) == 1, 'heroi4 deve vencer do vilao2'
    assert confronto.lutar(heroi4, vilao3) == 2, 'heroi4 deve perder do vilao3'
    assert confronto.lutar(heroi4, vilao4) == 2, 'heroi4 deve perder do vilao4'

    assert confronto.lutar(heroi5, vilao1) == 1, 'heroi5 deve vencer do vilao1'
    assert confronto.lutar(heroi5, vilao2) == 1, 'heroi5 deve vencer do vilao2'
    assert confronto.lutar(heroi5, vilao3) == 2, 'heroi5 deve perder do vilao3'
    assert confronto.lutar(heroi5, vilao4) == 1, 'heroi5 deve vencer do vilao4'

    assert confronto.lutar(heroi6, vilao1) == 1, 'heroi6 deve vencer do vilao1'
    assert confronto.lutar(heroi6, vilao2) == 1, 'heroi6 deve vencer do vilao2'
    assert confronto.lutar(heroi6, vilao3) == 2, 'heroi6 deve perder do vilao3'
    assert confronto.lutar(heroi6, vilao4) == 1, 'heroi6 deve vencer do vilao4'
except AssertionError as erro:
    print('ERRO...: Método lutar da classe Confronto (vitorias/derrotas):',
          erro)
except Exception as erro:
    print('ERRO...: Método lutar da classe Confronto (vitorias/derrotas):',
          erro)
else:
    print('CORRETO: Método lutar da classe Confronto (vitorias/derrotas)')
    acertos += 1


# Teste de confronto com empate
try:
    heroi = SuperHeroi("Flash", "Barry Allen")
    heroi.adicionar_super_poder(poder3)
    heroi.adicionar_super_poder(poder5)
    heroi.adicionar_super_poder(poder6)

    vilao = Vilao("Bizarro", "Bizarro", 1)
    vilao.adicionar_super_poder(poder2)
    vilao.adicionar_super_poder(poder5)
    vilao.adicionar_super_poder(poder6)
    assert confronto.lutar(heroi, vilao) == 0, 'A luta deveria estar empatada'
except AssertionError as erro:
    print('ERRO...: Método lutar da classe Confronto (empates):', erro)
except Exception as erro:
    print('ERRO...: Método lutar da classe Confronto (empates):', erro)
else:
    print('CORRETO: Método lutar da classe Confronto (empates)')
    acertos += 1

print()
print('Quantidade de acertos: ', acertos)
print('quantidade de erros..: ', 15-acertos)
