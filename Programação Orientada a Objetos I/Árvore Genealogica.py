class avos:
    def __init__(self):
        self.nome = "augusto"
        self.__idade = "68"
        self.__trabalha = "agricutor"
        self.saude = "rui"
        self.endereso = "ponte auta"
    
    def mostrar_atributos(self):
        print("Nome:", self.nome)
        print("Idade:", self.__idade)
        print("Trabalho:", self.__trabalha)
        print("Saúde:", self.saude)
        print("Endereço:", self.endereso)
    
    def modificar_atributos(self, idade, trabalha):
        self.__idade = idade
        self.__trabalha = trabalha

#-------------------------------------------------------------------
class pai:
    def __init__(self):
        self.nome = "silvio"
        self.__idade = "51"
        self.__trabalha = "caminhoneiro"
        self.saude = "boa"
        self.endereso = "rua jose linhares"
    
    def mostrar_atributos(self):
        print("Nome:", self.nome)
        print("Idade:", self.__idade)
        print("Trabalho:", self.__trabalha)
        print("Saúde:", self.saude)
        print("Endereço:", self.endereso)
    
    def modificar_atributos(self, idade, trabalha):
        self.__idade = idade
        self.__trabalha = trabalha

#-------------------------------------------------------------------
class eu:
    def __init__(self):
        self.nome = "william"
        self.__idade = "23"
        self.__trabalha = "não"
        self.saude = "boa"
        self.endereso = "rua jose linhares"
    
    def mostrar_atributos(self):
        print("Nome:", self.nome)
        print("Idade:", self.__idade)
        print("Trabalho:", self.__trabalha)
        print("Saúde:", self.saude)
        print("Endereço:", self.endereso)
    
    def modificar_atributos(self, idade, trabalha):
        self.__idade = idade
        self.__trabalha = trabalha

#-------------------------------------------------------------------
# Criando instâncias das classes
avo_instancia = avos()
pai_instancia = pai()
eu_instancia = eu()

#-------------------------------------------------------------------
print("2023")
print("Atributos dos Avós:")
avo_instancia.mostrar_atributos()
print("\nAtributos dos Pais:")
pai_instancia.mostrar_atributos()
print("\nMeus Atributos:")
eu_instancia.mostrar_atributos()

#-------------------------------------------------------------------
# modificando

avo_instancia.modificar_atributos("70", "jardineiro")
pai_instancia.modificar_atributos("52", "taxista")
eu_instancia.modificar_atributos("24", "TI")

#-------------------------------------------------------------------
#apos modificaçao
print("2024")
print("\nAtributos dos Avós após modificação:")
avo_instancia.mostrar_atributos()
print("\nAtributos dos Pais após modificação:")
pai_instancia.mostrar_atributos()
print("\nMeus Atributos após modificação:")
eu_instancia.mostrar_atributos()

#-------------------------------------------------------------------