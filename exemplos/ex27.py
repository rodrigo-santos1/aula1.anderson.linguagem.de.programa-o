#contar até 10
#mostrar quais numeros sao pares
#mostrar quais numeros sao impares
#no intervalo de 0 até 10

a = 0
while a <= 10:
    if a == 0:
        print("O número é zero.", a)
    if a % 2 == 0:
        print(f"{a} é par")
    else:
        print(f"{a} é ímpar")
    a += 1