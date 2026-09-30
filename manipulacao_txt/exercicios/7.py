def criar_arquivo():
    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana\n")
        arquivo.write("Bruno\n")
        arquivo.write("Carlos\n")
        arquivo.write("Daniela\n")
        arquivo.write("Eduardo\n")
        arquivo.write("Fernanda\n")
        arquivo.write("Gabriel\n")

def buscar_nome():
    nomes = []

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nomes.append(linha.strip())

    nome = input("Digite o nome que deseja pesquisar: ")

    if nome in nomes:
        print("Nome encontrado!")
    else:
        print("Nome não encontrado!")

criar_arquivo()
buscar_nome()