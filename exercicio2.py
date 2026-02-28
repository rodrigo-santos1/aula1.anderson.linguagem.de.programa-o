nota1 = float(input("Digite a primeira nota (entre 0 e 100): "))
nota2 = float(input("Digite a segunda nota (entre 0 e 100): "))

if nota1 + nota2 >= 60 and nota1 >= 40 and nota2 >= 40:
    print("O aluno passou.")
else:
    print("O aluno não passou.")