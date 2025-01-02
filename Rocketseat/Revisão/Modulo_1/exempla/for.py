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

print(list(range(0,10)))

for numero in range(5):
    print(numero)
print('--------------')
for indice in range(0, len(lista)):
    print(indice)
    print(lista[indice])
    if indice == 3:
        lista[indice] = 5
    print(lista)

lista_enumerate = ["a","b","c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")