import requests

print("BUSCADOR DE CEP")

cep = input("Digite o CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

dados = resposta.json()

if "erro" in dados:
    print("CEP não encontrado.")
else:
    print("\nResultado:")
    print("Rua:", dados["logradouro"])
    print("Bairro:", dados["bairro"])
    print("Cidade:", dados["localidade"])
    print("Estado:", dados["uf"])