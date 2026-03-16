import random

numero_secreto = random.randint(1, 100)

print("JOGO DE ADIVINHAÇÃO")
print("Tente adivinhar o número entre 1 e 100")

while True:
    palpite = int(input("Digite seu palpite: "))

    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print("Parabéns! Você acertou!")
        break