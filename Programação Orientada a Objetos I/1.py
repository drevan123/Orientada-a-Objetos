# Definindo uma metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        # Adicionando um método adicional a todas as classes que usam esta metaclass
        dct['metaclass_method'] = lambda self: f"Este método é da metaclass {cls.__name__}"
        return super().__new__(cls, name, bases, dct)

# Explicação: Meta é uma metaclass que herda de type. Ela adiciona um método chamado
# metaclass_method a qualquer classe que use Meta como sua metaclass.

# Definindo mixins
class Mixin1:
    def mixin1_method(self):
        return "Este método é do Mixin1"

# Explicação: Mixin1 define um método mixin1_method. Mixins são usados para adicionar
# funcionalidades a outras classes através da herança múltipla.

class Mixin2:
    def mixin2_method(self):
        return "Este método é do Mixin2"

# Explicação: Mixin2 define um método mixin2_method.

class Mixin3:
    def mixin3_method(self):
        return "Este método é do Mixin3"

# Explicação: Mixin3 define um método mixin3_method.

# Definindo a classe base que usa a metaclass e os mixins
class BaseClass(metaclass=Meta):
    def base_method(self):
        return "Este método é da BaseClass"

# Explicação: BaseClass usa a metaclass Meta. Isso significa que todas as instâncias de BaseClass
# (e suas subclasses) terão o método metaclass_method adicionado pela metaclass. BaseClass também
# define um método base_method.

# Definindo uma classe derivada que herda de BaseClass e dos Mixins
class DerivedClass(BaseClass, Mixin1, Mixin2, Mixin3):
    def derived_method(self):
        return "Este método é da DerivedClass"

# Explicação: DerivedClass herda de BaseClass, Mixin1, Mixin2 e Mixin3. Isso significa que ela terá
# todos os métodos de BaseClass e dos mixins, além do método derived_method.

# Instanciando a classe derivada
obj = DerivedClass()

# Chamando os métodos para verificar o comportamento
print(obj.base_method())            # Método da BaseClass
print(obj.mixin1_method())          # Método do Mixin1
print(obj.mixin2_method())          # Método do Mixin2
print(obj.mixin3_method())          # Método do Mixin3
print(obj.derived_method())         # Método da DerivedClass
print(obj.metaclass_method())       # Método adicionado pela metaclass

# Explicação: Aqui, estamos criando uma instância de DerivedClass e chamando vários métodos para verificar
# seu comportamento. Cada chamada de método segue a MRO para encontrar o método correto na hierarquia de classes.

# Verificando a MRO (Method Resolution Order)
print(DerivedClass.__mro__)         # Mostra a ordem de resolução dos métodos

# Metaclasses
# Meta é uma metaclass que herda de type. Ela redefine o método __new__ para adicionar um método chamado metaclass_method a todas as classes que usam Meta 
# como metaclass. Isso significa que qualquer classe que especificar Meta como sua metaclass terá automaticamente o método metaclass_method.

# Mixins
# Exemplo, Mixin1, Mixin2 e Mixin3 são classes mixin que fornecem os métodos mixin1_method, mixin2_method e mixin3_method, respectivamente. Essas classes
# são projetadas para adicionar funcionalidades específicas a outras classes.

# Herança Múltipla e MRO
# A DerivedClass herda de BaseClass, Mixin1, Mixin2 e Mixin3. Isso significa que DerivedClass possui todos os métodos de BaseClass e dos mixins. A MRO 
# (Method Resolution Order) define a ordem em que Python procura métodos na hierarquia de classes. No exemplo, a MRO de DerivedClass pode ser verificada
# com DerivedClass.__mro__, que mostra a ordem exata de resolução dos métodos, garantindo que o método correto seja chamado, especialmente em casos de herança múltipla.

# Funcionamento do Código
# instanciar DerivedClass e chamar seus métodos, vemos a aplicação de herança múltipla, mixins e metaclasses em ação. A MRO garante que os métodos sejam encontrados na ordem 
# correta, e a metaclass adiciona um método especial a todas as classes que a utilizam.