class Funcionario:
    def __init__(self, nome, idade, salario, departamento, id_funcionario):
        self.__nome = nome  
        self.idade = idade
        self.salario = salario
        self.departamento = departamento
        self.id_funcionario = id_funcionario
    
    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}, Idade: {self.idade}, Salário: {self.salario}, Departamento: {self.departamento}, ID: {self.id_funcionario}")
    
    def calcular_bonus(self, porcentagem):
        bonus = self.salario * porcentagem / 100
        return bonus


class Produto:
    def __init__(self, nome, preco, estoque, categoria, id_produto):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque  
        self.categoria = categoria
        self.id_produto = id_produto
    
    def exibir_informacoes(self):
        print(f"Produto: {self.nome}, Preço: {self.preco}, Estoque: {self.__estoque}, Categoria: {self.categoria}, ID: {self.id_produto}")
    
    def atualizar_estoque(self, quantidade):
        self.__estoque += quantidade
    

class Cliente:
    def __init__(self, nome, email, endereco, telefone, id_cliente):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.__telefone = telefone
        self.id_cliente = id_cliente
    
    def exibir_informacoes(self):
        print(f"Cliente: {self.nome}, Email: {self.email}, Endereço: {self.endereco}, Telefone: {self.__telefone}, ID: {self.id_cliente}")
    
    def atualizar_telefone(self, novo_telefone):
        self.__telefone = novo_telefone

funcionario1 = Funcionario("João", 30, 5000, "RH", 1)
produto1 = Produto("Notebook", 1500, 10, "Eletrônicos", 101)
cliente1 = Cliente("Maria", "maria@example.com", "Rua A, 123", "555-1234", 201)


funcionario1.exibir_informacoes()
produto1.exibir_informacoes()
cliente1.exibir_informacoes()
