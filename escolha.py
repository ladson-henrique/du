print("Bem-vindo à Escolha do Caminho!\n")

print("Escolha um caminho para prosseguir:\n")
escolha = ""
while escolha not in ["A" or "a","B" or "b","C" or "c"]:

    print("Caminho A")
    print("Caminho B")
    print("Caminho C\n")

    escolha = input("Escolha um caminho:")

    if escolha == 'a' or 'A':
        print("Caminho Errado")
    elif escolha == 'b' or 'B':
        print("Caminho Errado")
    elif escolha == 'c' or 'C':
        print("Caminho Correto")
    else:
        print("print nenhum caminho selecionado")