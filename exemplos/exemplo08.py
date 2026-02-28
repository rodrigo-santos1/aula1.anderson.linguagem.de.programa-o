#Calcular a velocidade final
#o usuario deve entrar com os valores
#v = v0 + a*t
# s = s0 + a*t + (a*t*t)

a = float(input("Entre com a aceleracao:"))
v0 = float(input("Entre com a velocidade inicial:"))
t = float(input("Entre com o tempo:"))
s = v0*t + (a*t*t)/2
v = v0 + a*t
print("A velocidade final é:", v)
print("A velocidade final é:", s)
