from Rocketseat.Dicionarios.dicionarios import valores

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("Meu dicionario de ex: " , pessoa)

print("Nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31
print("idade:", pessoa["idade"])

del pessoa["sobrenome"]
print(pessoa)

chaves = list(pessoa.keys())
print("Chave", chaves)
print(chaves[0])


valores = list(pessoa.values())
print(valores)
print(valores[0])

itens = list(pessoa.items())
print(itens)
print(itens[0][1])