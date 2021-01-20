while True:
    dados = open('Dados.txt', 'r')

    final_arquivo = False
    str_vazia = ''
    print(f"\033[34mPrograma Para Ver As Taxas de Isolamento da Cidade de São Paulo Durante a Quarentena do COVID-19\033[m")

    num_cidades = 0

    taxa_usu_menu = str(input("Qual faixa de dados deseja verificar:\na. <50%\nb. 50% até 60%\nc. 60% ou mais\nd. Sair do Programa\nOpção:")).upper()


    while taxa_usu_menu not in "ABCD":
        print("OPÇÃO NÃO DISPONIVEL!!")
        taxa_usu_menu = str(input("Qual faixa de dados deseja verificar:\na. <50%\nb. 50% até 60%\nc. 60% ou mais\nOpção:")).upper()

    if taxa_usu_menu == "D":
        print("\033[31m Programa Finalizado!!\033[m")
        break

    if taxa_usu_menu == "A":
        print(f"As cidades com  taxa menores que 50% são:")
    elif taxa_usu_menu == "B":
        print(f"As cidades com  taxa entre 50% até 60% são:")
    else:
        print(f"As cidades com  taxa maiores que 60% são:")
    while not final_arquivo:

        linha = dados.readline()

        if linha == str_vazia:
            final_arquivo = True
        else:
            comp = len(linha)
            taxa = str(linha[comp - 3:])
            taxa = int(taxa)
            #<50%
            if taxa_usu_menu == "A":

                if taxa < 50:
                    cidade = str(linha[:comp - 3])
                    num_cidades += 1
                    print(f"\033[35m{cidade}\033[m com \033[34m{taxa}%\033[m")
            elif taxa_usu_menu == "B":
                if taxa >=50 and taxa <=60:
                    comp = len(linha)
                    cidade = str(linha[:comp - 3])

                    num_cidades += 1
                    print(f"\033[35m{cidade}\033[m com \033[32m{taxa}%\033[m")
            else:
                if taxa >60:
                    cidade = str(linha[:comp - 3])

                    num_cidades += 1
                    print(f"\033[35m{cidade}\033[m com \033[33m{taxa}%\033[m")
    print(f"Totalizando: \033[31m{num_cidades}\033[m cidade(s) ")
    print("\n")
    dados.close()