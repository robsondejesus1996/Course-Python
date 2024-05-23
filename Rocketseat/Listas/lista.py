#Declaracao

minha_lista = [1,2,3,4,5, "Robson", True, False]

print("Minha lista exemplo: ", minha_lista)

minha_lista[0] = "Python"
#Exibindo a lista por indice
print("minha_lista[0]: ",minha_lista[0])
print("minha_lista[5]: ",minha_lista[5])
print(minha_lista[1:7])


#metodo append adiciona um elemento ao  final da lista
minha_lista.append(6)
print(minha_lista)


#Metodo index
indice = minha_lista.index(6)
print(indice)


#metodo insert insere um elemento em um indice especifico
minha_lista.insert(2, 10)
print(minha_lista)


#Metodo pop
elemento_removido = minha_lista.pop(3)
print(elemento_removido)
print(minha_lista)


#Metodo remove
minha_lista.remove(True)
print(minha_lista)


#Metodo sort
minha_lista.sort()
print(minha_lista)