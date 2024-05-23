# Criando um dicionario de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}


print("Meu dicionario de exemplo: ", pessoa)


#Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
pessoa["sobrenome"] = "Silva"
print("Sobrenome", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade Atualizada:", pessoa["idade"])

#Removendo um par chave-valor
del pessoa["sobrenome"]

print(pessoa)


#metodo keys() values() items()
chaves = list(pessoa.keys())
print("Chaves do dicionario ", chaves)
print("Primeira chave", chaves[0])

valores = list(pessoa.values())
print("Valores do dicionario", valores)
print("Primeiro valor", valores[0])


itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeiro valor", itens[0][1])
