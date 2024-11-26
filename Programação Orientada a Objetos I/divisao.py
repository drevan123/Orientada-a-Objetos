class Divisao:
    def calcular(self, numeros):
        resultado = numeros[0]
        for num in numeros[1:]:
            if num == 0:
                return "Erro! Divisão por zero não é permitida."
            resultado /= num
        return resultado

    def operacao(self, numeros):
        return '/'