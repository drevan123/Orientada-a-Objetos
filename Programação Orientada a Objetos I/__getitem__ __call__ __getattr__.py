class ListaPersonalizada:
    def __init__(self, itens):
        self.itens = itens
    
    # O metodo __getitem__ permite acessar elementos do objeto como se fosse uma sequencia ou mapeamento.
    def __getitem__(self, index):
        return self.itens[index]

lista = ListaPersonalizada([1, 2, 3, 4, 5])
print(lista[0])  # Saida: 1
print(lista[2])  # Saida: 3

class FuncaoPersonalizada:
    # O metodo __call__ permite que o objeto seja chamado como uma fucao.
    def __call__(self, *args, **kwargs):
        print("Funcao personalizada foi chamada com os seguintes argumentos:", args, kwargs)
    #"kwargs" é um termo comumente usado em Python que significa "argumentos de palavra-chave". 
funcao = FuncaoPersonalizada()
funcao(1, 2, a=3, b=4)
    # Saida: Funçao personalizada foi chamada com os seguintes argumentos:
    #  (1, 2) 
    # {'a': 3, 'b': 4}

class AtributoPersonalizado:
    # O metodo __getattr__ é chamado quando você tenta acessar um atributo que nao existe.
    def __getattr__(self, name):
        return f"Atributo '{name}' nao existe!"

objeto = AtributoPersonalizado()
print(objeto.atributo_inexistente)
    # Saida: Atributo 'atributo_inexistente' nao existe!
