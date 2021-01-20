def CriarArquivo(nomeCidade, tipo):
    arquivo = nomeCidade + ".txt"
    nomeCidade = open(arquivo, f'{tipo}')

    return nomeCidade


def verificarTaxa(taxa):
    while not (taxa >= 0 and taxa <= 100):
        print ("TAXA FORA DO RANGE!!")
        taxa = int(input("Digite a taxa, entre 0 e 100:"))
    return taxa

nome_cidade = str(input("\nEscreva o nome da cidade:")).upper()
arquivo_cidade = CriarArquivo(nome_cidade, 'a')
taxa_usu = int(input("Digite a taxa, entre 0 e 100:"))
taxa_usu = verificarTaxa(taxa_usu)


taxa = str(taxa_usu) + "\n"

print(taxa)
print(arquivo_cidade)
arquivo_cidade.write(taxa)

arquivo_cidade.close()