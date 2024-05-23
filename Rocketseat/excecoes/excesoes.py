print('Exemplo de captura de excções')
try:
    numero = int(input("digite um numero inteiro: "))
    resultado = 10 / numero

except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Opeação finalizada")