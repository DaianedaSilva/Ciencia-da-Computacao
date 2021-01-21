while True:
    dados = open('Dados.txt', 'r')

    final_arquivo = False
    str_vazia = ''

    print(
        f"Programa Para Ver As Taxas de Isolamento da Cidade de São Paulo Durante a Quarentena do COVID-19"
    )

    num_cidades = 0

    taxa_usu = int(input("\033[34mTaxa que deseja verificar:\033[m"))
    print(f"As cidades com  taxa de {taxa_usu}% são:")

    while not final_arquivo:

        linha = dados.readline()

        if linha == str_vazia:
            final_arquivo = True
        else:
            comp = len(linha)
            taxa = str(linha[comp - 3:])
            taxa = int(taxa)
            cidade = str(linha[:comp - 3])

            if taxa == taxa_usu:
                num_cidades += 1
                print(f"\033[35m{cidade}\033[m")
    print(f"Totalizando: \033[31m{num_cidades}\033[m cidade(s) ")

    cont = input("Procurar outra taxa? \na.SIM\nb.Não\nOpção:").upper()
    while cont not in "AB":
        print("OPÇÃO NÃO DISPONIVEL!!")
        cont = input("Procurar outra taxa? \na.SIM\nb.Não\nOpção:").upper()

    if cont == "B":
        print("\033[31m Programa Finalizado!!\033[m")
        break
    print("\n")

    dados.close()
