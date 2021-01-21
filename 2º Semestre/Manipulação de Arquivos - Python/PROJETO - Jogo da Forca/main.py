# Daiane da Silva Urias Pereira TIA: 4199227-1
# Gisely Garcia Pereira Souza TIA: 4190351-1
# Ciência da Computação - Turma: 02N
import random

################### FUNÇÕES #################################


def lerArquivo(Nomearquivo):
    nome = Nomearquivo + ".txt"
    arquivo = open(nome, "r")

    for linha in arquivo:
        l = linha.rstrip()
        print(l)


def vetores(arquivo):
    palavra = [] * 50
    for linha in arquivo:
        palavra.append(linha)
    return palavra


def separar(aleatorio):
    dica = []
    palavra = []
    data = aleatorio.rstrip().split("=")
    palavra.append(data[0])
    dica.append(data[1])

    return palavra, dica


def BonecoEnforcado(errou):

    if errou == 0:
        nome = "0"
        lerArquivo(nome)

    if errou == 1:
        nome = "1"
        lerArquivo(nome)

    if errou == 2:
        nome = "2"
        lerArquivo(nome)

    if errou == 3:
        nome = "3"
        lerArquivo(nome)

    if errou == 4:
        nome = "4"
        lerArquivo(nome)

    if errou == 5:
        nome = "5"
        lerArquivo(nome)

    if errou == 6:
        nome = "enforcado"
        lerArquivo(nome)
        jogarnovamente()


def LetrasErradas(letra, vetor):
    print("-----------------------------")
    print(f"A letra {letra} Não está na palavra")
    vetor.append(letra)

    print("letras erradas:")
    for letra in vetor:
        print(letra, end=" - ")
    print("\n")


def jogarnovamente():
    print("-----------------------------")
    jogar = input(
        "Deseja jogar novamente?\n Digite apenas 1 ou 2 \n 1. SIM\n 2. NAO\nOpção:"
    )

    if jogar not in "12":
        print("OPÇÃO ERRADA!! Digite uma opção válida!")
        jogar = input(
            "Deseja jogar novamente?\n Digite apenas 1 ou 2 \n 1. SIM\n 2. NAO\nOpção:"
        )

    if jogar == "1":
        return main_Jogo()
    elif jogar == "2":
        print("FIM")


def main_Jogo():
    file = open("forcapalavras.txt", "r")

    #guardando os vetores
    vetorPalavraDica = vetores(file)

    #sorteando a palavra
    aleatorio = random.choice(vetorPalavraDica)
    #print(aleatorio)

    #separando dica e fruta
    fruta, dica = separar(aleatorio)

    #tamanho da palavra
    tamanhoPalavra = len(fruta[0])

    palavrasecreta = fruta[0]

    letrasdescobertas = []

    for i in range(0, tamanhoPalavra):
        letrasdescobertas.append("_")

    titulo = "titulo"
    lerArquivo(titulo)
    errou = 0

    print(f"\nPALAVRA SORTEADA!!")

    acertou = False
    letraerrada = []
    while acertou == False:

        print("\n")
        BonecoEnforcado(errou)

        print("\nPalavra: ", end="")
        for i in letrasdescobertas:
            print(i, end=" ")

        print(f"\nA Sua Dica é: {dica[0]}")
        letra = str(input("\n\nDigite a letra: ")).upper()

        if letra not in palavrasecreta:
            LetrasErradas(letra, letraerrada)
            errou += 1
        else:
            print("------------------------------------")
            print(f"Muito bem! A letra {letra} está na palavra")

        for i in range(0, tamanhoPalavra):
            if letra == palavrasecreta[i]:
                letrasdescobertas[i] = letra

        acertou = True

        for x in range(0, tamanhoPalavra):
            if letrasdescobertas[x] == "_":
                acertou = False

    print("\n")
    BonecoEnforcado(errou)
    print("\n\nPARABÉNS VOCÊ DESCOBRIU A PALAVRA!!")
    jogarnovamente()

    print("\n")

    file.close()


###############################################

main_Jogo()
