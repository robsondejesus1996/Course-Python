num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

# print(num1.isnumeric())
# print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Não da pra converter os numeros')

