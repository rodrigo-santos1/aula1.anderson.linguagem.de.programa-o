#Exercicio 1
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2 + numero3:
    print("Sim, o número", numero1, "é maior que a soma do", numero2, "e", numero3)
if numero2 > numero1 + numero3:
    print("Sim, o número", numero2, "é maior que a soma do", numero1, "e", numero3)
if numero3 > numero1 + numero2:
    print("Sim, o número", numero3, "é maior que a soma do", numero1, "e", numero2)
else:
    print("e nenhum número é maior que a soma dos outros dois.")