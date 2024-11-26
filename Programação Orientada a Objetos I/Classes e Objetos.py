class Carro:
    def __init__(self, marca, modelo, ano, preco, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.cor = cor

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco

    def informacoes(self):
        return f"{self.ano} {self.marca} {self.modelo}, {self.cor}, R${self.preco}"


class Cliente:
    def __init__(self, nome, cpf, endereco, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

    def comprar_carro(self, carro):
        if self.verificar_credito(carro.preco):
            print(f"{self.nome} comprou o carro {carro.modelo} por R${carro.preco}.")
        else:
            print(f"{self.nome} não possui crédito suficiente para comprar o carro.")

    def verificar_credito(self, valor_carro):
        
        return True


class Gerente:
    def __init__(self, nome, cpf, salario, area_responsavel):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.area_responsavel = area_responsavel

    def aumentar_salario(self, novo_salario):
        self.salario = novo_salario

    def adicionar_carro(self, carro, estoque):
        estoque.append(carro)
        print(f"O carro {carro.modelo} foi adicionado ao estoque.")

# Exemplo de uso
carro1 = Carro("Toyota", "Corolla", 2023, 800000, "Prata")
cliente1 = Cliente("Maria", "987.654.321-00", "Rua B, 456", "maria@email.com", "(21) 98765-4321")
gerente1 = Gerente("João", "123.456.789-00", 50000, "Vendas")

estoque_carros = [carro1]
cliente1.comprar_carro(carro1)
print("Estoque de carros:", len(estoque_carros))
