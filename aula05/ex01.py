#definição de classe
class Livro():

    #metodo construtor
    def __init__(self,titulo,autor,quantidade_paginas):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas
    
#instanciando o objeto
livro1 = Livro('Harry Potter e a Pedra Filosofal','J. K. Rowling',264)
livro2 = Livro("Poeira em alto mar", "Alan Bida", 100)

print(livro1.autor)