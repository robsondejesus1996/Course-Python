print("Exemplo de importação de um módulo padrão: ")
# import math
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

print("\nExemplode modulo personalizado")
# import meu_modulo
from meu_modulo import saudacao, dobro


mensagem = saudacao("Robson")
resultado_dobro = dobro(5)
print(mensagem)
print(resultado_dobro)