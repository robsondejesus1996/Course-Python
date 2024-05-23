lista = [1,2,3,4,5]

for elemento in lista:
    print(elemento)

print(100*'-')

tupla = (1,2,3,4,5)
for elemento in tupla:
    print(elemento)

print(100*'-')

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("for utilizando dicionario")
for chave in pessoa.keys():
    print(chave)

print("for utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)

print(100*'-')
print("for utilizando dicionario todos os valores")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range(): intervalo numerico em lista
print(list(range(0,10)))

for numero in range(5):
    print("Número: ",numero)

#len
for indice in range(0, len(lista)):
    print("Indice: ",indice)
    print("Elemento: ", lista[indice])
    if indice == 3:
        lista[indice] = 5

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")