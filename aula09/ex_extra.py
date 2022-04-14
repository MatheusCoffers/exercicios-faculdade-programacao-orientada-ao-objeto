class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria

class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []
    
    def adicionar_super_poder(self, superpoder):
        if(len(self.__poderes)<= 3):
           self.__poderes.append(superpoder)
        else: 
            raise ValueError
            

    def get_poder_total(self):
        soma = 0
        for i in range(len(self.__poderes)):
            soma += self.__poderes[i].get_categoria()
        return soma
            

    
class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao

class SuperHeroi(Personagem):
    def get_poder_total(self):
        return super().get_poder_total() * 1.1

    

class Confronto:
    def lutar(self, superheroi, vilao):
        if (superheroi.get_poder_total() > vilao.get_poder_total()):
            return 1
        elif (superheroi.get_poder_total() < vilao.get_poder_total()):
            return 2
        else:
            return 0
