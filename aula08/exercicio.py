"""
1 - Criar variaveis para nome (str), idade (int) OK
2 - altura (float) e peso (float) de uma pessoa OK
3 - Criar variavel com o ano atual (int)
4 - Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
5 - Obter O IMC da pessoa com 2 cadas decimais (peso e na altura da pessoa)
6 - Exibir um texto com todos os valores na tela usando F-String (com as chaves)
"""
from datetime import date

nome = "Robson"
idade = 28
altura = 1.8
peso = 85
anoAtual = date.today().year
anoNascimento = anoAtual - idade
imc = peso / (altura * altura)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é de {imc:.2f}.')
print(f'{nome} nasceu em {anoNascimento}.')
