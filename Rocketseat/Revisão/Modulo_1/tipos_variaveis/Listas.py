minha_lista = [1,2,3,4,5, "Robson", True, False]

minha_lista[2] = "Alterado"

print("Minha lista de ex: ",minha_lista)
print(minha_lista[2])
print(minha_lista[5])
print(minha_lista[6])
# print(minha_lista[12])

print(minha_lista[1:7])
print(minha_lista[:6])


minha_lista.append(6)
print(minha_lista)

indice = minha_lista.index(6)
print('Indice do elemento 6 é:', indice)

minha_lista.insert(2, 10)
print(minha_lista)


elemento_removido = minha_lista.pop(3)
print(elemento_removido)
print(minha_lista)

minha_lista.remove(True)
print(minha_lista)


minha_lista_int = [8,7,3,2,1,6,5,4]
minha_lista_int.sort()
print(minha_lista_int)