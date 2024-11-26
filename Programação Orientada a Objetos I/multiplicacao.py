class Multiplicacao:
    def calcular(self, numeros):
        resultado = 1
        for num in numeros:
            resultado *= num
        return resultado

    def operacao(self, numeros):
        return '*'