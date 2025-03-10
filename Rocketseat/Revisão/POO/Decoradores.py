def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper


@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()


class MeuDecoradorDeClass:
    def __init__(self, func):
        self.func = func
    def __call__(self,):
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada")

@MeuDecoradorDeClass
def segunda_funcao():
    print("segunda função foi chamada")


segunda_funcao()
