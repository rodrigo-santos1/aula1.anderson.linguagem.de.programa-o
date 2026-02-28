idade = int(input("Digite sua idade: "))
dinheiro = int(input("Digite quanto dinheiro você tem: "))
carteira = input("Você tem carteira de motorista? (s/n): ")

if (idade >= 18 and dinheiro >= 100) or carteira == "s":
    print("Você pode alugar o carro , BOYZINHO")
else:
    print("Você não pode alugar o carro , POBRE")