import time

class Passaro:
    def voar(self):
        print("Pássaro voando")
 
class Aviao:
    def voar(self):
        print("Avião voando")
 
class Baleia:
    def nadar(self):
        print("Baleia nadando")
    
    def voar(self):  # A baleia decide "voar" sarcasticamente
        time.sleep(2)  #segundo
        print("A baleia está voando... em seus sonhos! Ops Baleia não voa kkk")
 
def decolar(entidade):
    
    try:
        entidade.voar()
    except AttributeError:
        print(f"A entidade {type(entidade).__name__} não pode voar.")

passaro = Passaro()
aviao = Aviao()
baleia = Baleia()

decolar(passaro)
decolar(aviao)
decolar(baleia)

 
