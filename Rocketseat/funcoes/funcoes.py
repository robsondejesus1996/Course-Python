# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\nChamado a função saudação")
saudacao("Alice")
saudacao("Bob")


# função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamado a função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da função quadrado: ", resultado_quadrado)


# Função com multiplos parametros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamado a função soma")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma de {} e {} e: ".format(numero1, numero2), resultado_soma)
