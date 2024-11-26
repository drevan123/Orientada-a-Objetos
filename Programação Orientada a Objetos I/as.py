import random

class Gerente:
    def __init__(self, estado):
        self.estado = estado
        if self.estado == 'PR':
            self.nome = 'Gerente Paraná'
        elif self.estado == 'SC':
            self.nome = 'Gerente Santa Catarina'
        elif self.estado == 'RS':
            self.nome = 'Gerente Rio Grande do Sul'

class Conta:
    def __init__(self, numero_conta, nome, estado):
        self.numero_conta = numero_conta
        self.nome = nome
        self.estado = estado
        self.gerente = Gerente(estado)

# Função para criar uma nova conta bancária com número aleatório
def criar_conta(contas_exist):
    while True:
        nome = input("Digite seu nome: ")
        if nome:
            break
        else:
            print("Nome é obrigatório.")

    while True:
        estado = input("Digite o estado (PR, SC, RS): ").upper()
        if estado in ['PR', 'SC', 'RS']:
            break
        else:
            print("Estado inválido. Digite PR, SC ou RS.")
    
    # Gerando um número de conta aleatório no formato "XXX-XXXX"
    while True:
        numero_conta = f"{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        if numero_conta not in contas_exist:
            break
    
    contas_exist.append(numero_conta)
    nova_conta = Conta(numero_conta, nome, estado)
    return nova_conta

# Função para mostrar as contas criadas
def mostrar_contas(contas):
    print("\nContas criadas:")
    for conta in contas:
        if isinstance(conta, Conta):
            print("Nome do cliente:", conta.nome)
            print("Número da conta:", conta.numero_conta)
            print("Estado:", conta.estado)
            print("Gerente:", conta.gerente.nome)
            print("------------------------")
        else:
            print("Erro: Objeto de conta inválido.")

# Função principal
def main():
    contas_criadas = []  # Lista para armazenar as contas criadas
    
    while True:
        print("\nOpções:")
        print("1. Criar uma nova conta")
        print("2. Ver lista de contas criadas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nova_conta = criar_conta(contas_criadas)
            contas_criadas.append(nova_conta)
        elif opcao == '2':
            mostrar_contas(contas_criadas)
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
