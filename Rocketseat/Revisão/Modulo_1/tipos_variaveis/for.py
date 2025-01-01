lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

print('----------------')

tupla = (1, 2, 3, 4, 5, 6)

for elemento in tupla:
    print(elemento)

pessoa = {"nome": "João", "idade": 30, "cidade": "São paulo"}
for chave in pessoa.keys():
    print(chave)

    print('----------------')

for valor in pessoa.values():
    print(valor)
    print('----------------')
for chave, valor in pessoa.items():
    print(chave,":", valor)
    print('----------------')
