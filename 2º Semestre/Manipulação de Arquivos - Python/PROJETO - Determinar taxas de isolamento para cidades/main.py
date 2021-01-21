import sys

def RankingCidades():
    cidades = open('cidades.txt', 'r')
    lista_cid = []

    for cidade in cidades:
        print(cidade, end="")
        lista_cid.append(cidade.rstrip())
    return lista_cid
    cidades.close()

def verificarCidade(cidade,lista):
    while cidade not in lista:
        print("NOME ERRADO OU NÃO ESTA NA LISTA!!")
        cidade = str(input("\n\nEscreva o nome da cidade:")).upper()
    return cidade


def verificarTaxa(taxa):
    while not (taxa >= 0 and taxa <= 100):
        print("TAXA FORA DO RANGE!!")
        taxa = int(input("Digite a taxa, entre 0 e 100:"))
    return taxa



def CriarArquivo(nomeCidade, tipo):
    arquivo = nomeCidade + ".txt"
    nomeCidade = open(arquivo, f'{tipo}')
    return nomeCidade



def Media(nomeCidade):
    c = 0
    soma = 0
    arquivo= CriarArquivo(nomeCidade, 'r')
    for taxa_str in arquivo:
        taxa = int(taxa_str)
        soma = taxa + soma
        c += 1
    media = soma / c

    arquivo.close()
    print(f"\nMédia: {media}")
    Menu(nomeCidade)



def Menu(nomeCidade):
  opção = input( "\nO que deseja fazer?\na.Digitar Taxa\nb.Ver Média das taxas ja resgistradas na Cidade\nc.Escolher outra cidade\nd.Parar o Programa\nOpção:").upper()

  while opção not in "ABCD":
      print("OPÇÃO INVÁLIDA!!")
      opção = input(
          "\nO que deseja fazer?\na.Digitar Taxa\nb.Ver Média das taxas ja resgistradas na Cidade\nc.Escolher outra cidade\nd.Parar o Programa\nOpção:").upper()
  if opção == "C":
    print("\n")

  if opção == "D":
      sys.exit()

  if opção == "B":
      arquivo = CriarArquivo(nomeCidade, 'r')
      if arquivo.readline() == "":
        print("\nNenhum Dado no Arquivo!!\n Digite um Dado")
        arquivo.close()
        Menu(nomeCidade)
      else:
        Media(nomeCidade)


  if opção == "A":      
    Taxa(nomeCidade)
  

def Taxa(nomeCidade):
  taxa_usu = int(input("\nDigite a taxa, entre 0 e 100:"))
  taxa_usu = verificarTaxa(taxa_usu)
  taxa = str(taxa_usu) + "\n"
  arquivo= CriarArquivo(nomeCidade, 'a')
  arquivo.write(taxa)
  arquivo.close()
  cont = input("\nDigitar nova taxa?\na.Sim \nb.Não\nOpção:").upper()
  while cont not in "AB":
    print("Opção Inválida")
    cont = input("\nDigitar nova taxa?\na.Sim \nb.Não\nOpção:").upper()
  if cont == "A":
    Taxa(nomeCidade)
  if cont == "B":
    Menu(nome_cidade)

#############################################################

while True:
  resetar = "SIM"

  if resetar == "SIM":
    print("Escolha umas das 20 cidades listadas abaixo:")

    #trazendo as cidades e guardando numa lista
    lista_cidades = RankingCidades()

    nome_cidade = str(input("\n\nEscreva o nome da cidade:")).upper()
    
    nome_cidade = verificarCidade(nome_cidade,lista_cidades)
    
    #criando arquivo com o nome dado pelo usuário
    arquivo_cidade = CriarArquivo(nome_cidade, 'a')
    arquivo_cidade.close()

    Menu(nome_cidade)

    print("\n\n")