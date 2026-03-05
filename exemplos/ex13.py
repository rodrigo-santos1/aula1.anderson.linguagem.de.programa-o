# Leia dois números
numero1 = int(input("Entre com o primeiro número: "))
numero2 = int(input("Entre com o segundo número: "))
numero3 = int(input("Entre com o terceiro número: "))


# Escolha o maior
if numero1 > numero2:
    maior_numero = numero1
if numero2 > numero3:
    maior_numero = numero2
else:
    maior_numero = numero3

# imprima o resultado
print("O maior número é:", maior_numero)