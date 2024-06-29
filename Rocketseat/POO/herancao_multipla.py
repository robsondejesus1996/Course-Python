class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentado."

class Ave(Animal):
    def voar(self):
        return f'{self.nome} esta voando.'


#Heranda multipla
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        super().emitir_som()
        return "Morcegos emitem sons ultrassonicos"


morcego = Morcego(nome="batman")

#acesando os metodos da classe base animal
print("Nome do morcego: ", morcego.nome)
print("Som do morcego: ", morcego.emitir_som())

# Acessar metodos das classes mamifero e ave
print("Morcego amamentando", morcego.amamentar())
print("Morcego voando", morcego.voar())