#entrar com 4 notas
#calcular a media
#media(soma) / quantidade
#media >= 7 APROVADO
#media >= 5 RECUPERAÇÃO
#media < 5 REPROVADO

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4 
if media >= 7:
    print("APROVADO")
if media >= 5:
    print("RECUPERAÇÃO")
if media < 5:
    print("REPROVADO")