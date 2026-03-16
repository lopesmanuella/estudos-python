import random
import string

print("GERADOR DE SENHAS SEGURAS")

tamanho = int(input("Digite o tamanho da senha: "))

letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

todos = letras + numeros + simbolos

senha = ""

for i in range(tamanho):
    senha += random.choice(todos)

print("\nSua senha segura é:")
print(senha)