class Forma:
    def area(self):
        pass
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura)/2
    
class Trapezio(Forma):
    def __init__(self, basem, baseM, altura):
        self.basem = basem
        self.baseM = baseM
        self.altura = altura
    def area(self):
        return ((self.basem + self.baseM) * self.altura)/2

formas = [Retangulo(10,5), Triangulo(10,5), Trapezio(4,24,8)]
for forma in formas:
    print("Área", forma.area(), "cm²")