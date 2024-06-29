#abstração
#encapsulamento
#polimorfismo
#herença


#Exemplo de herança
print("\nExemplo de herança")

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O anomal {self.nome} andou.")
    def emitir_som(self):
        pass

class Cachoro(Animal):
    def emitir_som(self):
        return f"Au, au som {self.nome}!"

class Gato(Animal):
    def emitir_som(self):
        return f"Miau som {self.nome}!"

dog = Cachoro(nome="Rex")
cat = Gato(nome="felix")


print("\nExemplo de polimorfismo")
animais = [dog, cat]
for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsulamento:")

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar(self):
        return self.__saldo

conta = ContaBancaria(saldo = 1000)
print(f"Saldo da conta bancaria: {conta.consultar()}")
conta.depositar(valor = 500)
print(f"Saldo da conta bancaria: {conta.consultar()}")
conta.sacar(valor = 500)
print(f"Saldo da conta bancaria: {conta.consultar()}")
