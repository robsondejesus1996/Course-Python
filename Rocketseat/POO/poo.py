# POO


#Classes modelo do mundo real Pessoa()

class Pessoa:
    #Construtor da classe, metodo que não tem retorno
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos."

#Objetos da classe pessoa
pessoa1 = Pessoa('Robson', 28)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa('Fernado', 32)
mensagem = pessoa2.saudacao()
print(mensagem)