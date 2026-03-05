#o usuario deve entrar com um numero e fazer a tabuada do numero até 10 , 5x2 = 10...

a = int(input("Entre com um número: "))
i = 1
while i <= 10:
    print(f"{a}x{i} = {a*i}")
    i += 1