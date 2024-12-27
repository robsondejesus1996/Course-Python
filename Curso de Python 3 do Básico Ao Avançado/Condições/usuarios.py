usuario = input('Nome de usuario: ')
senha = input('Senhado usuario: ')


usuario_bd = 'robson'
senha_db = '123456'


if usuario_bd == usuario and senha_db == senha:
    print('Voce está logado no sistema')
else:
    print('Usuario ou senha invalidos.')