alfabetizada = input("Você é alfabetizado? (s/n): ")
idade = int(input("Digite sua idade: "))

if alfabetizada == "s" and idade > 25:
    print("A pessoa é alfabetizada e tem mais de 25 anos.")
else:
    print("A pessoa não atende aos critérios.")
