from pyexpat.errors import messages

idade = int(input("Digite sua idade:"))

if idade >=18:
    print("Voce é maior de idade")
elif idade >=12:
    print("Voce e uma adolescente")
else:
    print("Voce é menor de idade")

mensagem = "Pode tirar a carteira de habilitação" if idade >=18 else "Voce não pode tirar a carteira de habilitação"
print(mensagem)


# if idade == 19:
#     print("Voce tem 19 anos")
# if idade <= 18:
#     print("Voce é menor de idade")
#
# if idade != 10:
#     print("Voce não tem 10 anos")



