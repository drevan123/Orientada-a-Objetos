
class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.orgaos = []

    def adicionar_orgao(self, orgao):
        self.orgaos.append(orgao)

class Mamifero(Animal):
    def __init__(self, nome):
        super().__init__(nome)

class Ave(Animal):
    def __init__(self, nome):
        super().__init__(nome)

class Peixe(Animal):
    def __init__(self, nome):
        super().__init__(nome)

class Orgao:
    def __init__(self, nome):
        self.nome = nome

class Coracao(Orgao):
    def __init__(self):
        super().__init__('Coração')

class Pulmao(Orgao):
    def __init__(self):
        super().__init__('Pulmão')

class Braco(Orgao):
    def __init__(self):
        super().__init__('Braço')

class Asa(Orgao):
    def __init__(self):
        super().__init__('Asa')

class Nadadeira(Orgao):
    def __init__(self):
        super().__init__('Nadadeira')

class Parasita:
    def __init__(self, nome):
        self.nome = nome

mamifero1 = Mamifero('Leão')
mamifero1.adicionar_orgao(Coracao())
mamifero1.adicionar_orgao(Pulmao())
mamifero1.adicionar_orgao(Braco())

ave1 = Ave('Águia')
ave1.adicionar_orgao(Coracao())
ave1.adicionar_orgao(Asa())
ave1.adicionar_orgao(Pulmao())

peixe1 = Peixe('Tubarão')
peixe1.adicionar_orgao(Coracao())
peixe1.adicionar_orgao(Nadadeira())
peixe1.adicionar_orgao(Pulmao())

parasita1 = Parasita('Carrapato')
animal_hospedeiro = mamifero1  #associa ao leão
animal_hospedeiro.parasita = parasita1

animal_amigo1 = Mamifero('Girafa')
animal_amigo2 = Ave('tucano')
animal_amigo1.amigo = animal_amigo2
animal_amigo2.amigo = animal_amigo1


print(f"Nome do mamífero: {mamifero1.nome}")
print(f"Órgãos do mamífero: {[orgao.nome for orgao in mamifero1.orgaos]}")

print(f"Nome da ave: {ave1.nome}")
print(f"Órgãos da ave: {[orgao.nome for orgao in ave1.orgaos]}")

print(f"Nome do peixe: {peixe1.nome}")
print(f"Órgãos do peixe: {[orgao.nome for orgao in peixe1.orgaos]}")

print(f"Parasita: {parasita1.nome}")
print(f"Parasita associado ao animal: {animal_hospedeiro.nome}")

print(f"Amigo do mamífero: {animal_amigo1.amigo.nome}")
print(f"Amigo da ave: {animal_amigo2.amigo.nome}")
