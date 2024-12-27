"""
Operadores Relacionais
"""
num_1 = 3
num_2 = 2

print( num_1 <= num_2)



var_1 = 'Luiz'
var_2 = 'Otavio'

expressao = (var_1 != var_2)
print(expressao)

print('-------------------------')

nome = input('Qual é o seu nome ')
idade = int(input('Qual é sua idade :'))

#limite para pegar o emprestimo
idade_menor = 20
idade_maior = 30


if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} NÃO PODE PEGAR O EMPRESTIMO ')

