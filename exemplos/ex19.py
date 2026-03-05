x = int(input("Entre com um número:"))
y = int(input("Entre com um número:"))
z = int(input("Entre com um número:"))

if x > y and x > z:
    resultado = "x é o maior número"
elif y > x and y > z:
    resultado = "y é o maior número"
elif z > x and z > y:
    resultado = "z é o maior número"
else:
    resultado = "números iguais"
print(resultado)