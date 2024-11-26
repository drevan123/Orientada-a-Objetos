import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 3

    print("Bem-vindo ao jogo de adivinhação!")
    print("Eu escolhi um número entre 1 e 10. Tente adivinhar!")

    while tentativas > 0:
        print("\nTentativas restantes:", tentativas)
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            return
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

        tentativas -= 1

    print("\nFim de jogo! O número secreto era:", numero_secreto)

jogo_adivinhacao()
