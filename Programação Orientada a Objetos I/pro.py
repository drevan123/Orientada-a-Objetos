class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def informacoes(self, *args):
        if len(args) == 0:
            print(f"Carro {self.modelo} ({self.ano}), Cor: {self.cor}")
        elif len(args) == 1:
            print(f"Carro {self.modelo} ({self.ano}), Cor: {self.cor}, Preço: {args[0]}")
        else:
            print("\nNúmero inválido de argumentos")

    @staticmethod
    def criar_carro(modelo, ano, cor):
        return Carro(modelo, ano, cor)


class LojaDeCarro:
    def __init__(self, nome):
        self.nome = nome
        self.carros_em_estoque = []

    def adicionar_carro(self, carro):
        self.carros_em_estoque.append(carro)

    def mostrar_carros_em_estoque(self):
        print(f"\nCarros em estoque na loja {self.nome}:")
        for carro in self.carros_em_estoque:
            carro.informacoes()


#polimorfismo de sobrecarga
carro1 = Carro("Sedan", 2022, "Azul")
carro1.informacoes()
carro1.informacoes(50000)

#linha 12
#carro1.informacoes(50000, "extra_argument")

# Instancia de metodo estatico
carro2 = Carro.criar_carro("Hatch", 2023, "Vermelho")
carro2.informacoes()

# Instanciade agregação
carro3 = Carro("SUV", 2023, "Prata")
loja = LojaDeCarro("Carros Toupeira")
loja.adicionar_carro(carro3)


loja.mostrar_carros_em_estoque()
