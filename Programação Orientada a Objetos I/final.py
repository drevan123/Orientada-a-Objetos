class Conceito:
    def __init__(self):
        self.texto = "Uma classe é uma estrutura genérica que define como serão os objetos de um determinado tipo."

class Definicao(Conceito):
    def __init__(self):
        super().__init__()
        self.texto += " Ela é uma estrutura que encapsula dados e comportamentos."

class Componentes(Definicao):
    def __init__(self):
        super().__init__()
        self.texto += " Uma classe possui atributos (variáveis) e métodos (funções) que operam nesses atributos."

class Reutilizacao(Componentes):
    def __init__(self):
        super().__init__()
        self.texto += " A herança permite a reutilização de código, possibilitando que uma classe herde características de outra."

class Exemplo(Reutilizacao):
    def __init__(self):
        super().__init__()
        self.texto += " Um exemplo comum é a classe 'Pessoa', que pode ter atributos como 'nome' e 'idade', e métodos como 'caminhar'."

minha_classe = Exemplo()

print("\nConceito:", minha_classe.texto)
print("\nDefinicao:", minha_classe.texto[len(Conceito().texto):len(Definicao().texto)])
print("\nComponentes:", minha_classe.texto[len(Definicao().texto):len(Componentes().texto)])
print("\nReutilizacao:", minha_classe.texto[len(Componentes().texto):len(Reutilizacao().texto)])
print("\nExemplo:", minha_classe.texto[len(Reutilizacao().texto):])
