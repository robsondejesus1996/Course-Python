from Rocketseat.POO.decoradoresComuns import configuracao1, Matematica


class MinhaClasse:
    valor = 10

    def __init__(self, nome):
        self.nome = nome

    def metodo_instancia(self):
        return f"Método de instancia chamado para {self.valor}"

    @classmethod
    def metodo_class(cls):
        return f"Método de classe chamado para valor={cls.valor}"

    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"

obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_class())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))


configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")


class Metamatica:

    @staticmethod
    def somar(a, b):
        return a + b

print(Matematica.somar(a=10, b=15))

