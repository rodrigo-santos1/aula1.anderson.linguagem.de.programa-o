idade = int(input("Digite sua idade: "))
autorizacao_pais = input("Você tem autorização dos pais? (s/n): ")

if idade >= 18 or autorizacao_pais == "s":
    print("acesso legal")
else:
    print("acesso negado")
