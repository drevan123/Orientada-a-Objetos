class Funcionario:
    def __init__(self, nome, salario_por_hora, horario):
        self.nome = nome
        self.salario_por_hora = salario_por_hora
        self.horario = horario

    def exibir_informacoes(self):
        print(f"{self.nome} trabalha {self.horario}. Função: {self.get_funcao()}. Salário: {self.calcular_pagamento()}")

    def calcular_pagamento(self):
        # Calcular o pagamento baseado nas horas de trabalho
        return self.salario_por_hora

    def get_funcao(self):
        return "Funcionário Padrão"

class GerenteDeLoja(Funcionario):
    def __init__(self, nome, salario_por_hora, horario):
        super().__init__(nome, salario_por_hora, horario)

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Função: Gerente\nGerenciando a equipe da loja")

    def calcular_pagamento(self):
        # (40 horas semanais)
        return self.salario_por_hora * 40

    def get_funcao(self):
        return "Gerente"

class Vendedor(Funcionario):
    def calcular_pagamento(self):
        # (30 horas semanais)
        return self.salario_por_hora * 30

    def get_funcao(self):
        return "Vendedor"

class SupervisorDeEstoque(Funcionario):
    def calcular_pagamento(self):
        # (35 horas semanais)
        return self.salario_por_hora * 35

    def get_funcao(self):
        return "Supervisor de Estoque"

class Caixa(Funcionario):
    def calcular_pagamento(self):
        # (25 horas semanais)
        return self.salario_por_hora * 25

    def get_funcao(self):
        return "Caixa"

gerente = GerenteDeLoja("Maria", 15.00, "40 horas semanais")
vendedor = Vendedor("João", 9.30, "30 horas semanais")
supervisor = SupervisorDeEstoque("Ana", 11.00, "35 horas semanais")
caixa = Caixa("Carlos", 9.25, "25 horas semanais")

# Chamando os métodos exibir_informacoes para exibir os detalhes de cada funcionário
gerente.exibir_informacoes()
vendedor.exibir_informacoes()
supervisor.exibir_informacoes()
caixa.exibir_informacoes()
