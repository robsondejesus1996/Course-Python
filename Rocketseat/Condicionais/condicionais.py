# if, elif e else

idade = int(input("Quantos anos voce tem? "))

print("Exemplo de comando if")
if idade >= 18:
    print("Você é maior de idade")
elif idade >=12:
    print("Voce é um adolescente")
else:
    print("Voce é menor de idade")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Voce não pode tirar a carteira de habilitação"
print(mensagem)



# if idade == 19:
#     print("Você tem 19 anos")
#
# if idade <= 18:
#     print("Você é menor de idade")
#
# if idade != 10:
#     print("Você não tem 10 anos")

