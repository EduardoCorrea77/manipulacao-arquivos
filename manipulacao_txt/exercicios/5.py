def criar_arquivo():
    with open("texto.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Python")

def contar_caracteres():
    with open("texto.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    print(f"Quantidade de caracteres: {len(conteudo)}")

criar_arquivo()
contar_caracteres()