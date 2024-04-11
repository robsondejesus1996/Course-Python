"""
Aula de variaveis
"""

nome = 'Robson de Jesus'
idade = 27
altura = 1.80
e_maior = idade >= 18
peso = 80


print(nome, type(nome))
print("Idade : ", idade)
print("Altura:" , altura)
print("É maior ", e_maior)

print(idade * altura)


#calculo de indice de massa corporal
imc = peso/altura**2


print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)