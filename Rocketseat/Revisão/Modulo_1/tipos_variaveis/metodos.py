nome = 'Robson'
nome_completo = "Robson de Jesus"

print(nome.upper())
print(nome.lower())

print(nome_completo.count("s"))

print(nome_completo.find("s"))


print(nome.encode())
print(nome.encode().decode())

print(nome_completo.replace("R", "T"))


print("-".join(nome_completo))

print(nome_completo.split(" "))

nomeTeste = "xRobson de Jesusx"
print(nomeTeste.strip("x"))
print(nomeTeste.rstrip("x"))
print(nomeTeste.lstrip("x"))


print(nome_completo.startswith("Ro"))

print("abc"in nome_completo)
print("abc"not in nome_completo)