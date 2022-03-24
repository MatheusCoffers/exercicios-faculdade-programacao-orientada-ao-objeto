lado = []
for i in range(3):
    l = int(input(f'Digite o tamanho do {i + 1}º lado do triangulo em cm: '))
    print (l)
    lado.append(l)

#definimos a classe 
class Triangulo():
    #metodo construtor
    def __init__(self,lado):
        self.lado_a = lado[0]
        self.lado_b = lado[1]
        self.lado_c = lado[2]
    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c 

triangulo1 = Triangulo(lado)
print(f'o perimetro é {triangulo1.calcular_perimetro()} cm')
