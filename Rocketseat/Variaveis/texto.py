nome_completo = "Robson de Jesus"

nome = 'Robson'
sobrenome = 'De Jesus'

#Formatação
print("Nome completo", nome_completo)
print("Nome completo" + nome_completo)
print("Nome completo " + "Robson" + " de Jesus")
print("Nome completo ", nome_completo)
print("Nome completo %s" %nome_completo )
print(f"Nome Completo: {nome} {sobrenome}")
print("Nome Completo: {} {}".format(nome, sobrenome))

print(nome_completo.count("R"))
print(nome_completo.find("R"))

print(nome_completo.encode())

print(nome_completo.encode().decode())
print(nome_completo.replace("R", "T"))


print("-".join("Robson"))
print(nome_completo.split(" "))

nomeTeste = "XRobsonx"
print(nome.strip("x"))


print("abc" not in nome_completo)
print("abc" in nome_completo)