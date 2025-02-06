
print("Exemplo de Importação de um módulo Padrão:")
# import math
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada é {raiz_quadrada}")


print("\nExemplo de criação e utilização de um módulo personalizado")
# import meu_modulo
from meu_modulo import saudacao, dobro

mensagem = saudacao("Robson")
resultado = dobro(5)
print(mensagem)
print(resultado)