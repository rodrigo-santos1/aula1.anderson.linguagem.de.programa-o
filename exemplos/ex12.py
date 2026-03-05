# Leia três números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
 
# Assumimos temporariamente que o primeiro número
# é o maior.
# Verificaremos isso em breve.
maior_numero = numero1
# Verificamos se o segundo número é maior 
# que o maior_numero atual
# e atualize o maior_numero, se necessário.
if numero2 > maior_numero:
    maior_numero = numero2
 
# Verificamos se o terceiro número é maior
# que o maior_numero atual
# e atualize o maior_numero, se necessáio.
if numero3 > maior_numero:
    maior_numero = numero3
 
# Imprime o resultado
print("O maior número é:", maior_numero)