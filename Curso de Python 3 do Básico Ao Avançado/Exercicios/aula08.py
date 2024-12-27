"""
* Criar variaveis para nome (str), idade (int),
* Altura (float) e  peso (float) de uma pessoa
* Criar variáveis com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obther o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando f-string (com chaves)
"""

nome = 'Robson'
idade = 27
altura = 1.80
peso = 80
ano_atual = 2024
ano_nascimento = ano_atual - idade;
imc = peso /altura ** 2
print(f'{nome} tem {idade} de idade, {altura} de altura e peso de {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')