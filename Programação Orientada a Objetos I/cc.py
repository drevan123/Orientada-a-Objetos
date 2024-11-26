import random

def escolher_palavra():
    palavras = ['ABACAXI', 'BANANA', 'CARRO', 'DADO', 'ELEFANTE', 'FLORESTA', 'GIRASSOL']
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    palavra_mostrada = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_mostrada += letra + ' '
        else:
            palavra_mostrada += '- '
    return palavra_mostrada.strip()

def jogar_jogo():
    palavra = escolher_palavra()
    letras_corretas = set()
    erros = 0

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra: ", mostrar_palavra(palavra, letras_corretas))

    while erros < 5:
        tentativa = input("Digite uma letra ou a palavra inteira: ").upper()

        if len(tentativa) == 1:
            if tentativa in palavra:
                letras_corretas.add(tentativa)
                print("Letra correta!")
            else:
                erros += 1
                print("Letra incorreta! Você tem", 5 - erros, "tentativas restantes.")
        else:
            if tentativa == palavra:
                print("Parabéns! Você adivinhou a palavra correta!")
                return
            else:
                erros += 1
                print("Palavra incorreta! Você tem", 5 - erros, "tentativas restantes.")

        print("Palavra atual: ", mostrar_palavra(palavra, letras_corretas))

        if '-' not in mostrar_palavra(palavra, letras_corretas):
            print("Parabéns! Você ganhou!")
            return

    print("Você perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogar_jogo()
