
print("\nImportação de modulo de terceiro")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitatação HTTP para {url} retornou o status {response.status_code}")