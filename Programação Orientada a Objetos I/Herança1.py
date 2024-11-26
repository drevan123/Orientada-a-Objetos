class Pessoa:
    def __init__(self, nome, idade, trabalha, saude, endereco):
        self.nome = nome
        self.__idade = idade
        self.__trabalha = trabalha
        self.saude = saude
        self.endereco = endereco
    
    def mostrar_atributos(self):
        print("Nome:", self.nome)
        print("Idade:", self.__idade)
        print("Trabalho:", self.__trabalha)
        print("Saúde:", self.saude)
        print("Endereço:", self.endereco)
    
    def modificar_atributos(self, idade, trabalha):
        self.__idade = idade
        self.__trabalha = trabalha
    
        
class avos (Pessoa):
    def __init__(self):
        Pessoa.__init__(self,"Augusto", "68", "agricultor", "rui", "ponte alta")

class Pai(Pessoa):
    def __init__(self):
        Pessoa.__init__(self,"Silvio", "51", "caminhoneiro", "boa", "rua jose linhares")

class Eu(Pessoa):
    def __init__(self):
        Pessoa.__init__(self,"William", "23", "não", "boa", "rua jose linhares")

avo_instancia = avos()
pai_instancia = Pai()
eu_instancia = Eu()

print("2023")
print("Atributos dos Avós:")
avo_instancia.mostrar_atributos()
print("\nAtributos dos Pais:")
pai_instancia.mostrar_atributos()
print("\nMeus Atributos:")
eu_instancia.mostrar_atributos()

# Modificando atributos
avo_instancia.modificar_atributos("70", "jardineiro")
pai_instancia.modificar_atributos("52", "taxista")
eu_instancia.modificar_atributos("24", "TI")

print("2024")
print("\nAtributos dos Avós após modificação:")
avo_instancia.mostrar_atributos()
print("\nAtributos dos Pais após modificação:")
pai_instancia.mostrar_atributos()
print("\nMeus Atributos após modificação:")
eu_instancia.mostrar_atributos()
    
 