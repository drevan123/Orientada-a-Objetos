class Subtracao:
    def calcular(self, numeros):
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado -= num
        return resultado

    def operacao(self, numeros):
        return '-'