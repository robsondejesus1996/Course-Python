from pyexpat.errors import messages


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.name = nome
        self.idade = idade
    def saudacao(self):
        # print(f"Olá meu nome é {self.name} e eu tenho {self.idade} anos.")
        return f"Olá meu nome é {self.name} e eu tenho {self.idade} anos."

pessoa1 = Pessoa("Robson", 28)
print("Nome: ", pessoa1.name)
print("Idade: ", pessoa1.idade)
mensagem = pessoa1.saudacao()
print(messages)


