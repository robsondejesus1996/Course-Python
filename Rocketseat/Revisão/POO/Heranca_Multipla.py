class Animal:
    def __init__(self, nome):
        self.nome = nome


    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."


class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."


class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrassonicos"

morcego = Morcego(nome="Batman")

print("NOme do morcego: ", morcego.nome)
print("Som do morcego: ", morcego.emitir_som())

print("Morcego amamentando: " , morcego.amamentar())
print("Morcego voando: " , morcego.voar())







