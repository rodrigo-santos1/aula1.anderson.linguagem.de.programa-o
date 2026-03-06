import random
numero_secreto = random.randint(1,100)
tentativa = 1
while tentativa <=3:
    palpite = int(input("Adivinhe o núemro secreto:"))
    if palpite == numero_secreto:
        print("Parabéns , você acertou sua mula")
        break
    else:
        if palpite > numero_secreto:
            print("O número secreto é menor que:" ,palpite)
        else:
            print("O número secreto é maior que:" ,palpite)
    tentativa += 1
if tentativa > 3:
    print("Você perdeu seu trouxa")
    print("o número secreto era:" ,numero_secreto)
    print("seu babaca, tente depois")