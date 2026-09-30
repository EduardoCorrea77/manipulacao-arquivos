def criar_arquivo():
    with open("vendas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;Notebook;3500.00\n")
        arquivo.write("Bruno;Mouse;80.00\n")
        arquivo.write("Carlos;Teclado;150.00\n")
        arquivo.write("Ana;Monitor;900.00\n")
        arquivo.write("Daniela;Notebook;3500.00\n")
        arquivo.write("Bruno;Headset;200.00\n")
        arquivo.write("Carlos;Mouse;80.00\n")
        arquivo.write("Ana;Teclado;150.00\n")
        arquivo.write("Daniela;Monitor;900.00\n")


def gerar_relatorio():
    vendas = []
    quantidade_vendas = {}

    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(";")

            venda = {
                "vendedor": vendedor,
                "produto": produto,
                "valor": float(valor)
            }

            vendas.append(venda)

    total = 0

    for venda in vendas:
        total += venda["valor"]

        if venda["vendedor"] in quantidade_vendas:
            quantidade_vendas[venda["vendedor"]] += 1
        else:
            quantidade_vendas[venda["vendedor"]] = 1

    print(f"TOTAL DE VENDAS: R$ {total:.2f}")

    print("\nQuantidade de vendas:")

    for vendedor in quantidade_vendas:
        print(f"{vendedor}: {quantidade_vendas[vendedor]}")


criar_arquivo()
gerar_relatorio()