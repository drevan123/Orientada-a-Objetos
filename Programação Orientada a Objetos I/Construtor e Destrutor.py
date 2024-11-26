class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @classmethod
    def por_ano(cls, marca, ano):
        return cls(marca, f"Modelo Desconhecido {ano}")

    @staticmethod
    def info():
        return "Carro não existe ."

    def __del__(self):
        print(f"O carro {self.marca} {self.modelo} foi destruído.")

carro1 = Carro.por_ano("Toyota", 2020)
carro2 = Carro.por_ano("gol", 2004)

print(f"Carro: {carro1.marca}, {carro1.modelo}")
print(f"Carro: {carro2.marca}, {carro2.modelo}")

print(Carro.info())

del carro1
