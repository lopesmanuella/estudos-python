senha = input("Digite sua senha: ")

tem_numero = False
tem_maiuscula = False

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True
    if caractere.isupper():
        tem_maiuscula = True

if len(senha) >= 8 and tem_numero and tem_maiuscula:
    print("Senha forte")
else:
    print("Senha fraca")