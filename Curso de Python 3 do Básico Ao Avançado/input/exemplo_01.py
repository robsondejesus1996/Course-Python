nome = input("Qual é o seu nome? ")
idade = input('Qual a sua idade? ')


ano_nascimento = 2024 - int(idade);


print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}')

print(f'{nome} tem {idade} anos '
      f'{nome} nasceu em {ano_nascimento}')

