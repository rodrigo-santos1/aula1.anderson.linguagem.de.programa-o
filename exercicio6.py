idade = int(input("Digite sua idade: "))
categoria = input("Digite sua categoria (estudante, aposentado, professor): ")
dia_semana = input("Digite o dia da semana: ")

desconto = False

if categoria == "estudante" and (dia_semana == "terça-feira" or dia_semana == "quinta-feira"):
    desconto = True
if categoria == "aposentado" and dia_semana == "quarta-feira":
    desconto = True
if idade >= 60:
    desconto = True

if desconto:
    print("Você tem direito a desconto.")
else:
    print("Você não tem direito a desconto.")