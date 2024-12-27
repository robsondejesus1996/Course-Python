name = 'Robson de Jesus'
idade = 28
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura * altura)

print(f'{name} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(name, idade, imc))