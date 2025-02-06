print("\nImportação e uso de um módulo de terceiros")
import requests


url = "https://www.unidavi.edu.br"
response = requests.get(url)
print(f"Solicitação HTTp para {url} retornou o status {response.status_code}")

