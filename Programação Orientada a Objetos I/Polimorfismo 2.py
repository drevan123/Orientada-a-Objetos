class Calculadora:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

    def multiplicar(self, x, y):
        return x * y

    def dividir(self, x, y):
        if y == 0:
            return "Erro: divisao por zero"
        return x / y

class Area(Calculadora):
    def area_quadrado(self, lado):
        return self.multiplicar(lado, lado)

    def area_triangular(self, base, altura):
        return self.dividir(self.multiplicar(base, altura), 2)

    def area_circular(self, raio):
        return self.multiplicar(self.multiplicar(raio, raio), 3.14)

calculadora_area = Area()

#calculos de area
print("Area do quadrado:", calculadora_area.area_quadrado(5))
print("Area do triangulo:", calculadora_area.area_triangular(9, 6))
print("Area do circulo:", calculadora_area.area_circular(1))
