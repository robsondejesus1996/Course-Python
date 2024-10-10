
# a = 2
# b = 3
#
# if not b > a:
#     print('B é maior do que A')
# else:
#     print('A é maior do que B')
#
#
# nome = "Robson"
#
# if 'son' in nome:
#     print("Existe.")
# else:
#     print("Não existe")


usuarios = input('Nome de usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = 'robson'
senha_bd = '12345'

if usuario_bd == usuarios and senha_bd == senha:
    print('Voce está logado')
else:
    print('Não esta logado')
