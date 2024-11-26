import random

# Função para criar a matriz vazia
def criar_matriz():
    return [[0 for _ in range(20)] for _ in range(20)]

# Função para colocar os barcos na matriz oculta
def colocar_barcos(matriz):
    for tamanho, quantidade in [(2, 2), (3, 2), (4, 1), (5, 1)]:
        for _ in range(quantidade):
            while True:
                direcao = random.choice(['horizontal', 'vertical'])
                if direcao == 'horizontal':
                    linha = random.randint(0, 19)
                    coluna = random.randint(0, 20 - tamanho)
                    if all(matriz[linha][coluna+i] == 0 for i in range(tamanho)):
                        for i in range(tamanho):
                            matriz[linha][coluna+i] = 1
                        break
                else:
                    linha = random.randint(0, 20 - tamanho)
                    coluna = random.randint(0, 19)
                    if all(matriz[linha+i][coluna] == 0 for i in range(tamanho)):
                        for i in range(tamanho):
                            matriz[linha+i][coluna] = 1
                        break

# Função para imprimir a matriz visível
def imprimir_matriz_visivel(matriz):
    for linha in matriz:
        print(" ".join(map(lambda x: x if x in ['X', 'O', 'F'] else 'O', linha)))

# Função para verificar se o ataque acertou um navio
def verificar_ataque(matriz_oculta, matriz_visivel, linha, coluna):
    if matriz_oculta[linha][coluna] == 1:
        matriz_visivel[linha][coluna] = 'X'
        return True
    if matriz_visivel[linha][coluna] == 0:
        matriz_visivel[linha][coluna] = 'F'
    return False

# Função para contar os navios restantes
def contar_navios(matriz):
    return sum(cell == 1 for row in matriz for cell in row)

# Função principal do jogo
def batalha_naval():
    matriz_oculta = criar_matriz()
    matriz_visivel = criar_matriz()
    colocar_barcos(matriz_oculta)
    navios_restantes = contar_navios(matriz_oculta)
    
    while navios_restantes > 0:
        imprimir_matriz_visivel(matriz_visivel)
        print("Digite a linha e a coluna que deseja atacar (0-19), separadas por espaço:")
        entrada = input("Ataque: ").split()
        if len(entrada) != 2 or not entrada[0].isdigit() or not entrada[1].isdigit():
            print("Entrada inválida. Por favor, digite a linha e a coluna separadas por espaço.")
            continue
        linha, coluna = map(int, entrada)
        if linha < 0 or linha > 19 or coluna < 0 or coluna > 19:
            print("Entrada inválida. Linha e coluna devem estar entre 0 e 19.")
            continue
        if matriz_visivel[linha][coluna] in ['X', 'F']:
            print("Você já atacou essa posição. Tente novamente.")
            continue
        if verificar_ataque(matriz_oculta, matriz_visivel, linha, coluna):
            print("Você acertou um navio!")
            navios_restantes -= 1
        else:
            print("Você errou.")
    
    print("Parabéns! Você destruiu todos os navios!")

# Iniciar o jogo
if __name__ == "__main__":
    batalha_naval()
