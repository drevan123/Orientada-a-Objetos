import re
import random
from adicao import Adicao
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao

class Calculator3000(Adicao, Subtracao, Multiplicacao, Divisao):
    def __init__(self):
        super().__init__()
        self.operacoes = {
            '+': Adicao().calcular,
            '-': Subtracao().calcular,
            '*': Multiplicacao().calcular,
            '/': Divisao().calcular,
        }

    def inverter_operador(self, operador):
        operadores_possiveis = ['+', '-', '*', '/']
        operadores_possiveis.remove(operador)  # Remove o operador atual
        return random.choice(operadores_possiveis)
    
    def calcular_expressao(self, expressao):
        partes = re.findall(r'(\d+|\D)', expressao)
        numeros = [int(partes[i]) for i in range(0, len(partes), 2)]
        operadores = [partes[i] for i in range(1, len(partes), 2)]

        if len(numeros) < 2:
            print("Erro: É necessário pelo menos dois operandos para efetuar o cálculo.")
            return None
        
        if len(numeros) == 2:
            operadores[0] = self.inverter_operador(operadores[0])
            print(f"Operador invertido: {operadores[0]}")

        resultado = numeros[0]
        calculo_string = str(numeros[0])

        for i in range(len(operadores)):
            operador = operadores[i]
            if operador in self.operacoes:
                resultado = self.operacoes[operador]([resultado, numeros[i+1]])
                calculo_string += f" {operador} {numeros[i+1]}"
            else:
                print("Erro: Operador inválido.")
                return None
        
        print(f"Cálculo efetuado: {calculo_string} = {resultado}")
        return resultado

if __name__ == "__main__":
    calculadora = Calculator3000()
    expressao = input("Digite a expressão matemática (por exemplo, 2+3-1): ")
    resultado = calculadora.calcular_expressao(expressao)
    print("Resultado:", resultado)
