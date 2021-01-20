'''
Introdução do Jogo Revenge e menu
'''
#BIBLIOTECA IMPRIMIR LENTAMENTE
#dados
import sys
import time
import random


velocidade = 0.05

vida = 100


#função para print com pausa
def f_stringar(n_f_str: str):
    return eval(f'f"""{n_f_str}"""')

def print_pausado(texto, velocidade):
  for caracter in range(0, len(texto)):
    if '{' in texto:
      strin = ''
      if caracter in range(texto.find('{'), texto.find('}') + 1):
        for contador in range(texto.find('{'), texto.find('}') + 1):
          strin +=  texto[contador]
        if caracter == texto.find('{'):
          strin = f_stringar(strin)
          for carac in range(0, len(strin)):
            sys.stdout.write(strin[carac])
            sys.stdout.flush()
            time.sleep(velocidade)
      else:
        sys.stdout.write(texto[caracter])
        sys.stdout.flush()
        time.sleep(velocidade)
    else:
      sys.stdout.write(texto[caracter])
      sys.stdout.flush()
      time.sleep(velocidade)

def print_pausado_titulo(texto, velocidade):
  print(' '*20, end='')
  for caracter in range(0, len(texto)):
    if '{' in texto:
      strin = ''
      if caracter in range(texto.find('{'), texto.find('}') + 1):
        for contador in range(texto.find('{'), texto.find('}') + 1):
          strin +=  texto[contador]
        if caracter == texto.find('{'):
          strin = f_stringar(strin)
          for carac in range(0, len(strin)):
            sys.stdout.write(strin[carac])
            sys.stdout.flush()
            #time.sleep(velocidade)
      else:
        sys.stdout.write(texto[caracter])
        sys.stdout.flush()
        time.sleep(velocidade)
    else:
      sys.stdout.write(texto[caracter])
      sys.stdout.flush()
      time.sleep(velocidade)
      
#função para jogar dados
#função para print com pausa

def centralizar (texto):
  print(texto.center(60, ' '))

def desenhar (texto):
  print(texto.center(60, '┈'))
#dados

def dados ():
  dado1 = random.randrange(1, 6, 1)
  dado2 = random.randrange(1, 6, 1)
  return([dado1, dado2, dado1 + dado2])


def evento_sorte(valor_nescessario_para_passar, evento):
  temp_dados = dados()
  if temp_dados[2] >= valor_nescessario_para_passar:
    print_pausado('Para {evento}, você precisa tirar ', velocidade)
    print_pausado(f'{valor_nescessario_para_passar}', velocidade)
    print_pausado(' ou um valor maior.\n', velocidade)
    desenhar('┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')
    desenhar('┈┈┈_______ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈') 
    desenhar('┈┈/\       \ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')       
    desenhar('┈/()\   ()  \ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')    
    desenhar('/    \_______\┈JOGANDO OS DADOS...┈┈┈ ')
    desenhar('\    /()     /┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈') 
    desenhar('┈\()/   ()  /┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')
    desenhar('┈┈\/_____()/┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')
    desenhar('┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')
    print_pausado('\n', velocidade)
    print_pausado('...\n', 0.3)
    print_pausado('Você ganhou! O valor dos dados que você jogou foram ', velocidade)
    print_pausado(f'{temp_dados[0]}', velocidade)
    print_pausado(' e ',velocidade)
    print_pausado(f'{temp_dados[1]}', velocidade)
    print_pausado('.\n',velocidade)
    return(True)
  else:
    print_pausado('Para {evento}, você precisa tirar ', velocidade)
    print_pausado(f'{valor_nescessario_para_passar}', velocidade)
    print_pausado(' ou um valor maior.\n', velocidade)
    desenhar('┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')
    desenhar('┈┈┈_______ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈') 
    desenhar('┈┈/\       \ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')       
    desenhar('┈/()\   ()  \ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')    
    desenhar('/    \_______\┈JOGANDO OS DADOS...┈┈┈┈')  
    desenhar('\    /()     /┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')
    desenhar('┈\()/   ()  /┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')
    desenhar('┈┈\/_____()/┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')
    desenhar('┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈')
    print_pausado('\n', velocidade)
    print_pausado('...\n', 0.3)
    print_pausado('Você perdeu, o valor dos dados que você jogou foram ', velocidade)
    print_pausado(f'{temp_dados[0]}', velocidade)
    print_pausado(' e ',velocidade)
    print_pausado(f'{temp_dados[1]}', velocidade)
    print_pausado('.\n',velocidade)
    return(False)

#DEFINIÇAÕ PARA AS CORES
RED   = "\033[1;31m"  
RESET = "\033[0;0m"
AMARELO=  '\033[1;33m'
AZUL= '\033[1;34m'


def barra_vida(dano):
  pontos_vida= (100-dano)
  print(pontos_vida)
  #VIDA 0%
  if pontos_vida <=0:
    print(f'''
              Você tem {pontos_vida} de vida
      ''',end='')
    print(
      '''
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @                           @
          @                           @
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      '''
      )
  # vida de 0 até 25
  elif 25>=pontos_vida>0:
    print(f'''
              Você tem {pontos_vida} de vida
      ''',end='')
    print(
      '''
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @ ''', end="")
    print(RED + 
      '''########''' + RESET + "                  @"
      )
    print('          @' + RED + 
      ''' ########''' + RESET + "                  @"
      '''
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      '''
      )   

  #vida de 26 a 50
  elif 50>=pontos_vida>=26:
    print(f'''
              Você tem {pontos_vida} de vida
      ''',end='')
    print(
      '''
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @ ''', end="")
    print(RED + 
      '''#############''' + RESET + "             @"
      )
    print('          @' + RED + 
      ''' #############''' + RESET + "             @"
      '''
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      '''
      )   

  #vida de 51 até 99
  elif 99>=pontos_vida>=51:

    print(f'''
              Você tem {pontos_vida} de vida
      ''',end='')
    print(
      '''
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @ ''', end="")
    print(RED + 
      '''###################''' + RESET + "       @"
      )
    print('          @' + RED + 
      ''' ###################''' + RESET + "       @"
      '''
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      '''
      )

  elif pontos_vida ==100:
    print(f'''
              Você tem {pontos_vida} de vida
    ''',end='')
    print(
        '''
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @ ''', end="")
    print(RED + 
      '''#########################''' + RESET + " @"
        )
    print('        @' + RED + 
        ''' #########################''' +RESET+ " @"
        '''
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        '''
        )

#decidir caminho
def decidir_caminho(caminho):
  if caminho==1:
    print_pausado(AZUL + f'-Para eu conseguir minha vingança terei que chegar vivo até la, irei para a Cidade do Carvalhos. Muito obrigado meu senhor, irei lhe recompensar algum dia.\n \n'+ RESET,velocidade)
    print_pausado(f'Dizendo isto, {_nome} pega o caminho da direita e segue o seu destino.',velocidade)
  elif caminho==2:
    print_pausado(AZUL + f'-Eu não temo a morte, meu único objetivo é matar o miserável que comanda este reino, e para isso até por cima dela eu passarei!!!' + RESET ,velocidade)
    print_pausado(f'Dizendo isto, {_nome} pega o caminho da esquerda e segue o seu destino.',velocidade)




'''
1 =  100%
2 =  91.66%
3 =  83.33%
4 =  75.0%
5 =  66.66%
6 =  58.33%
7 =  50.0%
8 =  41.66%
9 =  33.33%
10 = 25.0%
11 = 16.66%
12 = 8.33%
resultado = dados()
print(f'Os resultados obtidos nos dados são dado 1 = {resultado[0]} dado2 = {resultado[1]} dado 1 + 2 = {resultado[2]}')
'''

def centralizar (texto):
  print(texto.center(60, ' '))

def desenhar (texto):
  print(texto.center(60, '┈'))

#Regras 
centralizar('REVENGE\n') 
desenhar('┈┈┈┈┈╭━━━╮┈┈┈')
desenhar('┈┈╭━━╯┊▇┊┃┈┈┈')
desenhar('┈┈▽▽▽▽╲ ╰╮┈┈┈')
desenhar('┈┈┈┈┈┈▕┊┊┊╰╮┈┈')
desenhar('┈┈△△△△╱ ┊┊╰╮┈┈')
desenhar('┈┈╰━━━━╮┊┊┊┊╰╮┈')
print('\n')
centralizar('Regras do jogo: Para você jogar, digite o número correspondente a sua escolha\n\n')
centralizar('Você Entendeu? SIM (1), NÃO (2)')
_pronto= int (input(""))

while (_pronto!=1):
    centralizar('LEIA NOVAMENTE AS REGRAS')
    centralizar('Regras do jogo: Para você jogar, digite o número correspondente a sua escolha\n\n Público-alvo: jovens\n\n')
    centralizar('Você Entendeu? SIM (1), NÃO (2)')
    _pronto= int (input(""))

else:
    centralizar('Iniciar o Jogo (1)      Créditos (2)')
    _menu= int (input(''))

#ESCOLHA DO MENU (2- CREDITO/ 1- INICIO DA HISTORIA)
#entrar nos creditos
while (_menu==2):
    centralizar("REVENGE")
    centralizar("Público-alvo: jovens")
    centralizar('CRIADORES DO JOGO:')
    centralizar('Daiane, Hugo e Maria Laura')
    centralizar('RPG desenvolvido para aula de Algoritmos e Programação I na linguaguem Python')
    centralizar('VOLTAR PARA O MENU? SIM (1) NÃO (2)')
    _vmenu= int (input(""))
    

#SAIR DOS CRÉDITOS
    if _vmenu==1:
        centralizar('Iniciar o Jogo (1)      Créditos (2)')
        _menu= int (input(''))
             

#INICIAR A HISTÓRIA   
else:
    centralizar('PARA MELHOR EXPERIÊNCIA NO JOGO, COLOQUE-SE NO LUGAR DO PERSONAGEM E FAÇA AS MELHORES ESCOLHAS!!\n')

    centralizar('        Boa Sorte!!!\n')

print_pausado_titulo('Século XII - Heguanau, França\n \n',0.07)

print_pausado_titulo('       Sexta feira\n \n',0.07)

print_pausado('Você está deitado na sua cama e são exatamente 22:35 hrs\n',velocidade)

print_pausado('Ao seu lado está deitada a Ana, sua linda esposa que você ama muito. E dormindo no berço, o fruto deste amor, sua adorável e linda filha Isabel de 3 anos de idade.\n',velocidade) 

print_pausado(' Sem elas você não saberia o que fazer, por elas faria tudo, até mesmo largar a guarda real para cuidar e ama-lás incondicionalmente, e foi extamente isto que você fez. Acabou sendo a  melhor escolha já feita, tudo o que viveu e viu lhe tira o sono de madrugada, matar pessoas pela inquisição não foi uma boa escolha, e tudo isto para quê? No fundo sabe que é simplemente para manter no poder pessoas fúteis sem misericórdia, que apenas querem cada vez mais dinheiro. Agora não é  hora de se perder no passado, vc observa sua linda familia e adormece nos braços de sua amada \n',velocidade)

_nome = input("\nEscreva o nome do personagem: \n \n")


print_pausado_titulo('Domingo\n', 0.07)

print_pausado('\nIsabel acorda com febre e com falta de ar. Ana não sabia mais o que fazer para ajudar a filha, todo tipo de remedio caseiro não funcionava, nada tinha efeito. Passam dois dias, a situação piora. A única opção seria buscar um médico na cidade vizinha, mas isso levaria 3 dias, e {_nome} temia deixa-las sozinhas, porém não há muitas escolhas... \n', velocidade)

print_pausado('Assim que amanheceu, {_nome} reuniu suas coisas e pegou seu cavalo para ir atrás de um médico...\n', velocidade)

print_pausado('Depois de 3 dias você consegue encontrar o médico. \n \n Você está exausto e não vê a hora de chegar em casa. \n \n Ao chegar perto de sua vila, você suspeita do grande movimento que estava acontenco ali, tendo muitas pessoas assustadas ao redor...', velocidade)

print_pausado(' \n \n Um cheiro de queimado pairava no ar, provavelmente uma floresta vizinha deveria ter pego fogo, pensou você. {_nome} não liga para nada disso, só quer encontrar sua família. \n Com o cansaço pesando, cruza a esquina de sua casa...\n \n', velocidade)

desenhar('┈┈┈┈ ) _(___[]_┈┈┈┈┈┈')
desenhar('┈┈┈┈(;`       /\┈┈┈┈┈┈┈┈')
desenhar('___/_____)__/ _\__┈┈┈┈┈')
desenhar('/ (_()   (  | /____/\┈┈┈')
desenhar('|(  |LI (.)I| | LI ||┈┈┈')
desenhar('----|__||___|_|____||┈┈┈')


print_pausado('{_nome} cai do cavalo, não acredita no que vê, não poderia ser verdade, SUA CASA ERAM CINZAS, o desespero toma conta\n ', velocidade)
print_pausado('Vasculha a casa em plantos e gritos, por fim encontra dois corpos ao pé de um móvel que aparentava ser um berço, {_nome} surta, nunca ouviram tantos gritos naquela vila. ', velocidade)
print_pausado('Aproxima-se sua vizinha, e ela diz:\n', velocidade)
print_pausado('\033[35m   - Acusaram Ana de bruxaria por estar fazendo poções em casa. Muitos guardas reais chegaram, não tivemos muito o que fazer. O próprio rei veio para dar uma lição aqueles que não o seguissem.\n\033[m', velocidade)
	
print_pausado('O ódio atinge a sua alma, não consegue ver mais nada além de sede por vingança, e aos pés do cadaver queimado de sua esposa, você jura vingança. \n \n Sobe em seu cavalo e sai da vila com os olhos em chamas e com suas armas para matar o rei.\n\n', velocidade)

print_pausado('           CAPÍTULO 1: A ENCRUZILHADA\n \n', velocidade)

print_pausado(f'{_nome} segue para a cidade visinha por uma estrada....\n', velocidade)


#CHAMAR AS COISAS ALEÁTORIAS


#ENCRUZILHADA
print_pausado(f'Na sua frente tem uma encruzilhada, e guardando o local, um senhor de aparência suspeita que aparentava lhe esperar, o enxergando ele branje:\n', velocidade)

print_pausado(AMARELO + f'-Olha só, um cavalheiro por essas bandas, pra onde vai meu jovem?\n \n' + RESET, velocidade)

_responderV = int (input("Responder o Senhor Estranho (1)    Apenas Encara-ló (2)\n\n"))

#RESPONDE O VELHO
if _responderV==1:
  print_pausado(AZUL + f'-Estou indo ao encontro daquele que você chama de Rei, irei acabar com o mal que assombra este reino!!!\n'+ RESET, velocidade)
  print_pausado(AMARELO + f' -Você parece muito determinado, e gostei do que você branda, irei te ajudar. \n \n Aqui nesta encruzilhada você tem dois caminhos, o primeiro te leva para a Cidade dos Carvalhos, é um caminho seguro e tranquilo, porém, você demorará mais para chegar ao seu destino final. Já a outra estrada te levará para a Cidade Santa, você poderá enfrentar grandes perigos, mas com certeza chegará mais rápido. \n  E, então meu cavalheiro, irá ir pelo caminho mais seguro ou enfrentará a morte?\n' + RESET, velocidade)

  decisao_caminho1= int (input('Cidade dos Carvalhos (1)  Cidade Santa (2)\n\n'))
    
  decidir_caminho (decisao_caminho1)
  

#ENCARA O VELHO
else:
  print_pausado(AMARELO + f' -Não é muito educado ficar encarando , estou com cara de fantasma? Sei que estou velho mas ainda estou vivo, não gostaria de uma informação para qual cidade deve ir? Tenho certeza que sem mim, jamais chegará em seu destino. Estou disposto a lhe ajudar por $10\n'+ RESET,velocidade)
  print_pausado(f'Sem saber para onde ir e com medo do que lhe aguarda, você paga para o senhor em troca de informações.\n',velocidade)
  #COLOCAR CODIGO DE DINHEIRO AQUI
  print_pausado(AZUL + f'-Estou indo ao encontro daquele que você chama de Rei, irei acabar com o mal que assombra este reino, qual o melhor caminho para mim?\n' + RESET, velocidade)
  print_pausado(AMARELO + f'- Você parece muito determinado, e gostei do que você branda. Irei te ajudar, aqui nesta encruzilhada você tem dois caminhos, o primeiro te leva para a Cidade dos Carvalhos, é um caminho seguro e tranquilo, porém, você demorará mais para chegar ao seu destino final. Já a outra estrada te levará para a Cidade Santa, você poderá enfrentar grandes perigos, mas com certeza chegará mais rápido. E, então meu cavalheiro, irá ir pelo caminho mais seguro ou enfrentará a morte?\n' + RESET,velocidade)
  
  decisao_caminho1= int (input('Cidade dos Carvalhos (1)  Cidade Santa (2) \n'))
    
  decidir_caminho (decisao_caminho1)
  
#caminho para a cidade dos carvalhos
####EVENTO ALEATORIO
print_pausado('{_nome} estava caminhando quando.....\n \n', velocidade)
evento = 'acontecer coisas boas'
if evento_sorte(8,evento):
  print_pausado("{_nome} está seguindo seu caminho tranquilamente em seu cavalo, quando vê alo brilhando no chão, UMA MOEDA DE OURO.Você se aproxima, e escondido em um arbusto estava um saco de moedas de ouro, aparentemente algum saqueador deixou cair. Hoje você está com sorte,não? Você guarda as moedas e segue seu caminho \n \n",velocidade)
else:
  print_pausado('Você está na estrada andando calmamente.\n', velocidade)
  print_pausado('O chão começa a tremer, sua espada cai no seu pé. ', velocidade)
  print_pausado('Você levou 7 de dano', velocidade)

  barra_vida(7)
  


if decisao_caminho1==1:
  print_pausado_titulo('CAPÍTULO II - A ESCOLHA\n \n', velocidade)
  
  print_pausado_titulo ('BEM-VINDO A CIDADE DOS CARVALHOS \n \n', velocidade)
  print_pausado(f'Finalmente você chega na cidade, não via a hora de comer algo.\n {_nome} observa ao redor e vê duas pessoas, um senhor em um banco e um guarda. \n Não seria nada mau pedir informações para alguém. E então decide....\nPedir Informações Para o Guarda (3) \nPedir Informações Para o Senhor (4) \n\n', velocidade )
  _cidadeA= int(input())


  #diálogos com o guarda
  if _cidadeA==3:
    print_pausado(f"\n\n Mesmo com ódio de todos que trabalham para o rei, {_nome} segue em direção do Guarda Real. \n  -Olá, gostaria de saber se poderia me ajudar dizendo o caminho correto para o castelo. \n\n ", velocidade )
    print_pausado(AMARELO + f'- Zzzzzzzzzzzzzz. Opá, desculpe, a dama disse alguma coisa???? \n Adorei o seu vestido, combinou com seu tom de pele!! \n {_nome} quase desmaiou com o hálito do guarda. Ele está visivelmente bêbado, lhe impressiona ainda estar de pé. {_nome} insiste\n - Eu quero saber o caminho para o castelo, você sabe?\n - Você quer um martelo???? Eu sou guarda não ferreiro!!\n -CASTELOOOO, CASTELO DO REI, ONDE FICA?? \n - Ahh sim, castelo, por que não disse antes? Fica na direção da Floresta Sem Misericórdia, só seguir por ela, uma moça não deveria ir lá sozinha, posso lhe acompanhar!\n {_nome} se afasta do guarda que aparentemente iria lhe beijar, mas caiu de cara no chão antes que conseguisse.....\n' + RESET, velocidade )
    print_pausado ('O que {_nome} fará agora?\n\nSeguir o Caminho do Guarda - A Floresta Sem Misericórdia (3) \nPedir Informações Para o Senhor (4) \n\n',  velocidade)
    dialogo_guarda= int(input())


    #PEDIR INFORMAÇÃO PARA O SENHOR APÓS TER FALADO COM O GUARDA
    if dialogo_guarda==4:
      print_pausado(f'-Desculpe incomodar meu senhor, não sou da região e estou procurando a estrada correta para ir ao Castelo Real. O senhor saberia para onde devo ir ?\n -OI??? FALOU ALGO? EU TO MEIO SURDO, PODERIA REPETIR?\n {_nome} se assusta com o grito.. \n -Queria saber o caminho para o castelo\n - AHH SIM, O CASTELO!!! ELE NÃO ESTÁ TÃO LONGE, SE VOCÊ PEGAR A ESTRADA PARA O LAGO DA DISCÓRDIA VOCÊ CHEGARÁ COM CERTEZA!!!\n Apesar de quase ficar surdo, {_nome} agradece ao senhor e se afasta.\n\nSeguir o Caminho do Guarda - A Floresta Sem Misericórdia (3)\nSeguir o Caminho do Senhor - O Lago da Discórdia (4)' , velocidade )
      dialogo_guarda_senhor= int(input())








#### DECIDIU SEGUIR O GUARDA - DEPOIS DE TER VISTO AS 2 OPÇÕES-COMEÇO DO PRIMEIRO QUE LEVA OA FIM
      if dialogo_guarda_senhor==3:
        print_pausado(f'Aparentemente o guarda parece ser o mais confiável.... Estranha decisão, mas {_nome} vai para a Floresta Sem Misericórdia, e ao adentrar no lugar entende porque se chama assim, parecia o lar de demônios, parece que o rei não quer ninguem indo até o seu castelo.\n Uns 10 minutos cavalgando você encontra uma placa: 7km Para a Cidade Amaldiçoada que leva ao Castelo Real\n Quem diria, o bêbado tarado falou a verdade....\n\n',velocidade )
       

       #IR PARA A CIDADE C
        print_pausado('{_nome} estava caminhando quando.....\n \n', velocidade)

        evento = 'acontecer coisas boas'
        if evento_sorte(8,evento):
            print_pausado("Seguindo o seu caminho você se depara com um cachorro te seguindo. \n \n -AU AU \n \n - SAI DAQUI SEU SARNENTO ESTUPIDO! \n \n - AUAUAUAU!!! \n \n Estranhamente o cachorro para. Ele quer que você o siga. \n \n Seguir o cachorro (1) Ignorar ele e continuar na sua trajetória (2)",velocidade)

            escolha = int(input("Digite a opção escolhida: "))

            if escolha == 1:
              print_pausado("Você acha aquilo bizarro, mas não custa nada seguir o animal....\n \n O Cachorro para de repente, e olha fixo para um arbusto... Curioso você desce do cavalo e vai ver o que é \n \n Você encontrou um baú!!! \n \n No mesmo instante quebra a fechadura e encontra lá dentro um pedaço de carne, um saco de maçãs e uma faca de pão (é pequena mas dá para se defender). \n \n Afinal o cachorro não era tão estúpido assim. Você o agradece dando um pedaço de carne e ele sai feliz abanando o rabo. \n \n Você sobe no cavalo, come uma maçã e segue sem olhar para trás.\n\n",velocidade)

            elif escolha == 2:
              print_pausado("Você ignora o cachorro e começa a andar mais rápido, e quando olha para trás ele já tinha desaparecido...\n\n",velocidade)
        else:
          print_pausado(" \n \n Você encontrou uma bebida no caminho e como estava com sede decidiu tomá-la... \n \n Ela estava infectada com bactérias e por isso você acaba de perder 12 pontos de vida.\n\n ", velocidade)

          barra_vida(64)
          print(barra_vida)
              
        #EVENTO 2
        print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

        evento = 'acontecer coisas boas'
        if evento_sorte(8,evento):
            print_pausado("Seguindo o seu caminho você se depara com um cachorro te seguindo. \n \n -AU AU \n \n - SAI DAQUI SEU SARNENTO ESTUPIDO! \n \n - AUAUAUAU!!! \n \n Estranhamente o cachorro para. Ele quer que você o siga. \n \n Seguir o cachorro (1) Ignorar ele e continuar na sua trajetória (2)",velocidade)

            escolha = int(input("Digite a opção escolhida: "))

            if escolha == 1:
              print_pausado("Você acha aquilo bizarro, mas não custa nada seguir o animal....\n \n O Cachorro para de repente, e olha fixo para um arbusto... Curioso você desce do cavalo e vai ver o que é \n \n Você encontrou um baú!!! \n \n No mesmo instante quebra a fechadura e encontra lá dentro um pedaço de carne, um saco de maçãs e uma faca de pão (é pequena mas dá para se defender). \n \n Afinal o cachorro não era tão estúpido assim. Você o agradece dando um pedaço de carne e ele sai feliz abanando o rabo. \n \n Você sobe no cavalo, come uma maçã e segue sem olhar para trás.\n\n",velocidade)

            elif escolha == 2:
              print_pausado("Você ignora o cachorro e começa a andar mais rápido, e quando olha para trás ele já tinha desaparecido...\n\n",velocidade)
        else:
          print_pausado(" \n \n Você encontrou uma bebida no caminho e como estava com sede decidiu tomá-la... \n \n Ela estava infectada com bactérias e por isso você acaba de perder 12 pontos de vida.\n\n ", velocidade)

          barra_vida(64)
          print(barra_vida)

        print_pausado ( f'...... {_nome} está exausto, porém a unica coisa que ele pensa é em sua vingança. \n Na frente ele vê uma placa:\n \n', velocidade)

        print_pausado_titulo('    CIDADE AMALDIÇOADA\n', velocidade)

        print_pausado_titulo('10 km para o Castelo Real\n\n',velocidade)

        print_pausado ( f'...... {_nome} acelera o cavalo, seu destino o espera daqui 10 quilomêtros....\n \n ', velocidade)



        print_pausado_titulo('    CAPÍTULO IV \n \n', velocidade)
        print_pausado_titulo(' A CIDADE AMALDIÇOADA\n', velocidade)

        print_pausado(f'Assim que {_nome} entra na cidade ele percebe algo estranho.\n Cadê as pessoas dali?\n\n {_nome} resolve caminhar pelo local, e finalmente encontrou as casas da vila.........\n \n Mas aquilo não eram casas, ERAM CINZAS...... \nImediatamente a imagem da sua casa vem a cabeça, {_nome} estava revivendo aquilo novamente. \n \n {_nome} avista fumaça no céu, e sai em disparado para o local\n \n Uma casa estava em chamas, o calor ardia seu rosto mesmo de longe. Ao mesmo tempo a imagem de sua filha e esposa dentro da casa fixou em sua mente\n \n ',velocidade)

        print_pausado(RED + f'- SOCORRO. ME AJUDEM!!!!!!!!!!!' + RESET, velocidade)
        print_pausado (RED + f'{_nome} avista uma mulher presa por uma guia de madeira perto da casa, pelo jeito ela estava fugindo. O fogo estava se espalhando rapidamente. Sua aparência era de muito doente, dava para ver os ossos no rosto, e os olhos eram tão fundos que parecia uma  caveira\n \n' + RESET, velocidade)
        print_pausado (RED + f' {_nome} ajuda a mulher (1)      {_nome} não a ajuda a mulher (2)\n \n' + RESET, velocidade)
        ajuda_mulher= int (input ())

        if ajuda_mulher == 1:
          print_pausado('{_nome} corre para  ajudar a mulher, o calor estava imenso, assim que levanta a viga algúem chega...',velocidade)
          print_pausado (AMARELO +'- PARE!!!!! ESTÁ MULHER ESTA INFECTADA COM A PESTE, VOCÊ IRÁ MORRER\n \n {_nome} se efasta com o susto e vê um homem encapuzado com uma máscara bizarra ' +RESET, velocidade)

          #imagem medico da peste
          print_pausado (AMARELO + '-Está cidade inteira está infectada com a peste negra, tentei ajudar a todos que viviam aqui, porém o rei acredita que a cidade é amaldiçoada, e sem piedade mandou queimar tudo e todos que estão aqui para purificar o reino. Esta mulher é Isadora, ela está com a peste e quase perto da morte, você chegou muito perto dela, deixei eu te examinar para ver se você esta infectado, os sintomas são muito rápidos, em menos de 3 minutos é possivel detectar o mal no corpo\n\n'+ RESET, velocidade)
          
          evento = 'sobreviver a doença'
          
          if evento_sorte(6, evento):
            print_pausado(' O médico depois de te analisar observou que você estava saudável, e felizmente não irá morrer.\n', velocidade)
            print_pausado ('- Você não está infectado e não pode fazer nada por ela. Assim, deixe ela e siga seu caminho, esta cidade está acabada. \n Com um enorme pesar no peito,  {_nome} segue para o castelo, determinado a acabar com isto uma vez por todas!!!\n \n', velocidade)
          else:
            print_pausado(' O médico depois de te analisar observou que você estava infectado, e infelizmente não irá sobreviver.', velocidade)
            print_pausado (f'-MEU DEUS!! VOCÊ ESTÁ INFECTADO!!! Não posso fazer nada por você, infelizmente em 1 dia você morrerá!!\n {_nome} se nega a acreditar e sai em disparada em seu cavalo. \n\n 5 horas depois {_nome} sente uma febre altíssima. \n\n 12 hrs depois {_nome} não consgeue mais andar\n\n 24 hrs depois {_nome} não consegue mais se manter no cavalo. {_nome} cai, bate a cabeça e desmaia.\n\n {_nome} nunca mais acordou!!\n\n ', velocidade)
            print_pausado_titulo ('VOCÊ MORREU!!', velocidade)
            time.sleep(5)
            sys.exit()
              
              ###CASTELO
              
            print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

            evento = 'acontecer coisas boas'
            if evento_sorte(8,evento):
              print_pausado("Você está andando em direção ao castelo e vê no chão uma espada. \n Parabéns, agora ela é sua!! ", velocidade)
            else:
              print_pausado('Você está cavalgando para o castelo com muita pressa, e não percebe o ganho que estáva na frente. Você é derubado do cavalo e vate a cabeça', velocidade)

              barra_vida (40)
            print_pausado("CAPÍTULO FINAL - O DESTINO \n\n", velocidade)
            print_pausado("Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

            print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

            #decidindo escolha

            if escolha == 1:
              print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
              print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
              print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
              print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
              print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
              print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
              print_pausado("Você lança a sua espada e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser inferior ao do rei. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
              print_pausado("\n FIM DE JOGO", velocidade)

            elif escolha == 2:
              print_pausado("Você escolheu matá-las", velocidade)
              print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
              print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
              print_pausado("\n FIM DE JOGO", velocidade)
                        #####FINAL DE TUDO



          




        if ajuda_mulher==2:
          print_pausado(f'{_nome} entra em choque, não consegue se movimentar, e vê naquela mulher sua esposa e filha, e quando se dá conta a mulher já estava carbonizada\n - Triste não é mesmo?\n {_nome} olha para o lado e se assusta com a pessoa que vê   \n -Está cidade inteira está infectada com a peste negra, tentei ajudar a todos que viviam aqui, porém o rei acredita que a cidade é amaldiçoada, e sem piedade mandou queimar tudo e todos que estão aqui para purificar o reino. Esta mulher é Isadora, ela está com a peste e quase perto da morte, ainda bem que você não chegou perto dela, se não poderia ter sido infectado e morrido. Infelizmente não podemos fazer nada por ela, siga seu caminho, esta cidade está acabada. \n Com um enorme pesar no peito, {_nome} segue para o castelo, determinado a acabar com isto uma vez por todas. \n \n!!! ', velocidade)
          
          #IR PARA O CASTELO
          #FINAL
          print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

          evento = 'acontecer coisas boas'
          if evento_sorte(8,evento):
            print_pausado("Você está andando em direção ao castelo e vê no chão uma espada. \n Parabéns, agora ela é sua!! ", velocidade)
          else:
            print_pausado('Você está cavalgando para o castelo com muita pressa, e não percebe o ganho que estáva na frente. Você é derubado do cavalo e vate a cabeça', velocidade)

            barra_vida (40)
          print_pausado("CAPÍTULO FINAL - O DESTINO \n\n", velocidade)
          print_pausado("Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

          print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

          #decidindo escolha

          if escolha == 1:
            print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
            print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
            print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
            print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
            print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
            print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
            print_pausado("Você lança a sua espada e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser inferior ao do rei. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)

          elif escolha == 2:
            print_pausado("Você escolheu matá-las", velocidade)
            print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
            print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)
                      #####FINAL DE TUDO







      elif dialogo_guarda_senhor==4:
        print_pausado(f'Aparentemente o idoso parece ser o mais confiável.... Aquele guarda não deve lembrar nem o seu nome.\n {_nome} pega a estrada para o Lago da Discórdia\n Uns 10 minutos cavalgando você encontra uma ponte e a sua única opção é atravessa-lá. \n CRASHHHHHHHHHHHHHHH {_nome} quase infarta, assim que terminou de atravessar, a ponte ela se quebra. Agora não tem mais volta, {_nome} segue em frente e avista uma placa: 1 km Cidade Santa que leva para o Castelo Real\n {_nome} não acredita no que lê. AQUELE VELHO SURDO, falou o caminho errado!! Agora só lhe resta ir para a Cidade Santa e lá achar o caminho correto.....\n\n',velocidade )
     
        #IR PARA A CIDADE B
        print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

        evento = 'acontecer coisas boas'
        if evento_sorte (9, evento):
          print_pausado('Você está andando pela estrada e vê uma senhora carregando uma sacola que aprece conter armas, você está curioso sobre a senhora e aprece que ela está tentando falar com você, você chega perto dela (1) ou a ignora (2)\n', velocidade)
          coisa = int(input())
          if coisa == 1:
            print_pausado('A senhora tira alguma coisa do saco e você não está certo do que é...\n', velocidade)
            print_pausado('Você chega mais perto\n', velocidade)
            print_pausado('E mais perto', velocidade)
            print_pausado('...', velocidade)
            print_pausado('A senhora dá uma machadada na sua mão por achar que está tentando rouba-la', velocidade)
            barra_vida(10)
            vida -= 10
          if coisa == 2:
            print_pausado('\nVida que segue.',velocidade)
        else:
          print_pausado(" - GRUUUUUUMMMMMM!! \n \n Opa, seu estômago está roncando alto, mas para sua sorte tem uma pomar logo a frente \n \n Ir até o pomar (1) Esperar para comer na cidade (2)  ",velocidade)

          escolha = int(input("Digite o número escolhido: "))

          if escolha == 1:
            print_pausado("As maçãs estão muito altas, você desce do cavalo e sobe em um galho para alcança-lás. \n \n - CRACCCCCCC! \n \n De repente o galho que você estava apoiado se rompe \n \n PUFT, você cai com tudo no chão e bate a cabeça, chega a ficar tonto. \n \n Não foi uma boa ideia ter ido ali.. Agora você está com fome e machucado!",velocidade)

            barra_vida(30)
            print(barra_vida)

          elif escolha == 2:
            print_pausado("Você vai para cidade e come em um bar próximo da estrada. \n \n Horas depois você começa a passar mal e 50 dinheiros seu cai no chão sem vc perceber.",velocidade)


              
        print_pausado('CAPITULO II - A Bruxa \n \n {_nome} chegou na cidade e por ser próxima ao castelo, o rei possui um carinho especial por ela. \n Você não sabe muito bem para onde ir, então resolve parar para descansar e quem sabe comprar algo no comércio local',velocidade)
        print_pausado('\nChegando no centro da cidade, você encontra um estranho aglomerado de pessoas.' ,velocidade)
        print_pausado('Se enfiando no meio das pessoas, você vê que alguém armou uma estrutura gigantesca, parece que vai acontecer algum evento ali...',velocidade)
        print_pausado('Chegando mais perto você vê uma mulher amarrada a uma estaca, aparentemente molhada e alguem segurando o que parece ser um braseiro próximo a ela.',velocidade)
        print_pausado('Claramente aquilo é uma execução pública, eles vão fazer com ela o mesmo que fizeram com sua mulher.',velocidade)
        print_pausado('A multidão grita "QUEIMEM A BRUXA"',velocidade)
        print_pausado('Você se encontra na frente da estrutura e se vê na oportunidade de interferir naquilo\n\n',velocidade)

        dec = int(input('Interferir (1)\n Ignorar (2)\n'))
        if dec == 2:
          print_pausado('Ignorando a senhora você segue seu caminho',velocidade)
          print_pausado('\nPassado algum tempo você se pergunta o porque daquilo tudo',velocidade)
          print_pausado('\nVocê busca o que acredita ser justo pra você mas não quer fazer justiça pelos outros',velocidade)
          print_pausado('\nPensando na dor e no sofrimento daqula senhora {_nome} retorna',velocidade)
          dec = 1
           
        if dec == 1:
          print_pausado('Você sobe na estrutura e desafia o carrasco',velocidade)
          print_pausado('-Quem você pensa que é forasteiro?',velocidade)
          print_pausado('-Essa execução é uma ordem direta de nossa majestade',velocidade)
          print_pausado('Você saca sua espada e o convida para um confronto direto\n',velocidade)

          evento = 'vencer o guarda'
          if evento_sorte(8 , evento):
            print_pausado('Em meio a batalha você percebe que o carrasco não era nada comparado aos desafios que você encontrou na sua carreira como guarda real\n', velocidade)
            print_pausado('Você acha uma brecha na técnica do guarda e vence a batalha.', velocidade)
            print_pausado('\n', velocidade)
            print_pausado('{_nome} liberta a senhora do tronco e a multidão se disperssa', velocidade)
            print_pausado('Conversando com a senhora, {_nome} descobre um novo caminho que o guiará para o castelo.', velocidade)
            print_pausado('\n{_nome} pega o cavalo do carrasco e segue sua vida.\n \n ', velocidade)
          else:
            print_pausado('O carrasco sorri ao ver que apesar de toda a habilidade de {_nome} com uma espada, ele está sofrendo muitos danos ', velocidade)
            print_pausado(' Por mais que atuou inúmeros anos como guarda real, seu cansaço o vence, fazendo com que você deixe uma abertura\n', velocidade)
            print_pausado('{_nome} morre', 0.4)
            time.sleep(5)
            sys.exit()

            ############SAINDO DA CIDADE#############################
            ########pocotopocotopocotopocotopocotopocoto#############
            #### CASTELO
            #FINAL
            ###aleatorio
          print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

          evento = 'acontecer coisas boas'
          if evento_sorte(8,evento):
              print_pausado("Você está andando em direção ao castelo e vê no chão uma espada. \n Parabéns, agora ela é sua!! ", velocidade)
          else:
            print_pausado('Você está cavalgando para o castelo com muita pressa, e não percebe o ganho que estáva na frente. Você é derubado do cavalo e vate a cabeça', velocidade)

          barra_vida (40)

          print_pausado("CAPÍTULO FINAL - O DESTINO \n\n", velocidade)
          print_pausado("\n\n Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

          print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

            #decidindo escolha

          escolha = int(input(" \n  \n Digite o número escolhido: "))

          if escolha == 1:
            print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
            print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
            print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
            print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
            print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
            print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
            print_pausado("Você lança a sua espada  e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser inferior ao do rei. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)

          elif escolha == 2:
            print_pausado("Você escolheu matá-las", velocidade)
            print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
            print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)


          else:
            print_pausado('O carrasco sorri ao ver que apesar de toda a habilidade de {nome} com uma espada ele está sofrendo mais danos. ', velocidade)
            print_pausado(' Por mais que teve inúmeros anos atuando na guarda real, seu cansaço o vence, fazendo com que {nome} deixe uma abertura\n', velocidade)
            print_pausado('{nome} morre', 0.4)
       



      
    elif dialogo_guarda==3:
      print_pausado(f'Aparentemente o guarda parece ser o mais confiável.... Estranha decisão, mas {_nome} vai para a Floresta Sem Misericórdia, e ao adentrar no lugar entende porque se chama assim, parecia o lar de demônios, parece que o rei não quer ninguem indo até o seu castelo.\n Uns 10 minutos cavalgando você encontra uma placa: 7km para o Castelo Real\n Quem diria, o bêbado falou a verdade....',velocidade )

      ####CIDADE C
      print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

      evento = 'acontecer coisas boas'
      if evento_sorte(8,evento):
          print_pausado("Seguindo o seu caminho você se depara com um cachorro te seguindo. \n \n -AU AU \n \n - SAI DAQUI SEU SARNENTO ESTUPIDO! \n \n - AUAUAUAU!!! \n \n Estranhamente o cachorro para. Ele quer que você o siga. \n \n Seguir o cachorro (1) Ignorar ele e continuar na sua trajetória (2)",velocidade)

          escolha = int(input("Digite a opção escolhida: "))

          if escolha == 1:
            print_pausado("Você acha aquilo bizarro, mas não custa nada seguir o animal....\n \n O Cachorro para de repente, e olha fixo para um arbusto... Curioso você desce do cavalo e vai ver o que é \n \n Você encontrou um baú!!! \n \n No mesmo instante quebra a fechadura e encontra lá dentro um pedaço de carne, um saco de maçãs e uma faca de pão (é pequena mas dá para se defender). \n \n Afinal o cachorro não era tão estúpido assim. Você o agradece dando um pedaço de carne e ele sai feliz abanando o rabo. \n \n Você sobe no cavalo, come uma maçã e segue sem olhar para trás.",velocidade)

          elif escolha == 2:
            print_pausado("Você ignora o cachorro e começa a andar mais rápido, e quando olha para trás ele já tinha desaparecido...",velocidade)
      else:
        print_pausado(" \n \n Você encontrou uma bebida no caminho e como estava com sede decidiu tomá-la... \n \n Ela estava infectada com bactérias e por isso você acaba de perder 12 pontos de vida. ", velocidade)

        barra_vida(64)
        print(barra_vida)
      
      print_pausado ( f'...... {_nome} está exausto, porém a única coisa que ele pensa é em sua vingança......\n Ele vê uma placa:\n \n', velocidade)

      print_pausado_titulo('    CIDADE AMALDIÇOADA\n', velocidade)

      print_pausado_titulo('10 km para o Castelo Real\n\n',velocidade)

      print_pausado ( f'...... {_nome} acelera o cavalo, seu destino o espera daqui 10 quilomêtros....\n \n ', velocidade)



      print_pausado_titulo('    CAPÍTULO IV \n \n', velocidade)
      print_pausado_titulo(' A CIDADE AMALDIÇOADA\n', velocidade)

      print_pausado(f'Assim que {_nome} entra na cidade ele percebe algo estranho.\n Cadê as pessoas dali?\n\n {_nome} resolve caminhar pelo local, e finalmente encontrou as casas da vila.........\n \n Mas aquilo não eram casas, ERAM CINZAS...... \nImediatamente a imagem da sua casa vem a cabeça, {_nome} estava revivendo aquilo novamente. \n \n {_nome} avista fumaça no céu, e sai disparado para o local\n \n Uma casa estava em chamas, o calor ardia seu rosto mesmo de longe. Ao mesmo tempo a imagem de sua filha e esposa dentro da casa fixou em sua mente\n \n ',velocidade)

      print_pausado(RED + f'- SOCO1RRO. ME AJUDEM!!!!!!!!!!!' + RESET,velocidade)
      print_pausado ('{_nome} avista uma mulher presa por uma guia de madeira perto da casa, pelo jeito ela estava fugindo. O fogo estava se espalhando rapidamente. Sua aparência era de muito doente, dava para ver os ossos no rosto, e os olhos eram tão fundos que parecia uma  caveira\n \n' + RESET, velocidade)
      print_pausado (RED + f'{_nome} ajuda a mulher (1)  {_nome} não a ajuda a mulher (2)\n \n' + RESET, velocidade)
      ajuda_mulher= int (input ())

      if ajuda_mulher == 1:
        print_pausado('{_nome} corre para  ajudar a mulher, o calor estava imenso....',velocidade)
        print_pausado ('- PARE!!!!! ESTÁ MULHER ESTA INFECTADA COM A PESTE, VOCÊ IRÁ MORRER\n \n {_nome} se efasta com o susto e vê um homem encapuzado com uma máscara bizarra ', velocidade)

          #imagem medico da peste
        print_pausado ('-Está cidade inteira está infectada com a peste negra, tentei ajudar a todos que viviam aqui, porém o rei acredita que a cidade é amaldiçoada, e sem piedade mandou queimar tudo e todos que estão aqui para purificar o reino. Esta mulher é Isadora, ela está com a peste e quase perto da morte, você chegou muito perto dela, deixe eu te examinar para ver se você esta infectado. Os sintomas são muito rapidos, em menos de 3 minutos é possivel detectar o mal no corpo\n\n', velocidade)
          
        evento = 'sobreviver a doença'
        if evento_sorte(6, evento):
          print_pausado(' O médico depois de te analisar observou que você está saudável, e felizmente não irá morrer.\n', velocidade)
          print_pausado ('- Você não está infectado e não pode fazer nada por ela, deixe ela e siga seu caminho, esta cidade está acabada. \n Com um enorme pesar no peito, {_nome} segue para o castelo, determinado a acabar com isto uma vez por todas \n \n!!!', velocidade)
        else:
          print_pausado(' O médico depois de te analisar observou que você estava infectado, e infelizmente não irá sobreviver.', velocidade)
          print_pausado (f'-MEU DEUS!! VOCÊ ESTÁ INFECTADO!!! Não posso fazer nada por você, infelizmente em 1 dia você morrerá!!\n {_nome} se nega a acreditar e sai em disparada em seu cavalo. \n\n 5 horas depois {_nome} sente uma febre altíssima. \n\n 12 hrs depois {_nome} não consegue mais andar\n\n 24 hrs depois {_nome} não consegue mais se manter no cavalo. {_nome} cai, bate a cabeça e desmaia.\n\n {_nome} nunca mais acordou!!\n\n ', velocidade)
          print_pausado_titulo ('VOCÊ MORREU!!', velocidade)
          time.sleep(5)
          sys.exit()
        ####evento aleatorio
        print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

        evento = 'acontecer coisas boas'
        if evento_sorte(8,evento):
          print_pausado("Você está andando em direção ao castelo e vê no chão uma espada. \n Parabéns, agora ela é sua!! ", velocidade)
        else:
          print_pausado('Você está cavalgando para o castelo com muita pressa, e não percebe o ganho que estáva na frente. Você é derubado do cavalo e vate a cabeça', velocidade)

          barra_vida (40)
          ###CASTELO
          #FINAL
        
          print_pausado("CAPÍTULO FINAL - O DESTINO \n\n", velocidade)

          print_pausado("Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

          print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

            #decidindo escolha

          escolha = int(input(" \n  \n Digite o número escolhido: "))

          if escolha == 1:
            print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
            print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
            print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
            print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
            print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
            print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
            print_pausado("Você lança a sua espada e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser claramente inferior. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)

          elif escolha == 2:
            print_pausado("Você escolheu matá-las", velocidade)
            print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
            print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)
              #####FINAL DE TUDO



  

    


            
    if ajuda_mulher==2:
      print_pausado(f'{_nome} entra em choque, não consegue se movimentar, e vê naquela mulher sua esposa e filha, e quando se dá conta a mulher já estava carbonizada\n - Triste não é mesmo?\n {_nome} olha para o lado e se assusta com a figura que vê \n -Está cidade inteira está infectada com a peste negra, tentei ajudar todos que viviam aqui, porém o rei acredita que a cidade é amaldiçoada, e sem piedade mandou queimar tudo e todos que estão aqui para purificar o reino. Esta mulher é Isadora, ela está com a peste e quase perto da morte, ainda bem que você não chegou perto dela, se não poderia ter sido infectado e morrido. Infelizmente  não podemos fazer nada por ela, siga seu caminho, esta cidade está acabada. \n Com um enorme pesar no peito, {_nome} segue para o castelo, determinado a acabar com isto uma vez por todas \n \n!!! ', velocidade)
          #IR PARA O CASTELO
          #FINAL
      
      print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

      evento = 'acontecer coisas boas'
      if evento_sorte(8,evento):
        print_pausado("Você está andando em direção ao castelo e vê no chão uma espada. \n Parabéns, agora ela é sua!! ", velocidade)
      else:
        print_pausado('Você está cavalgando para o castelo com muita pressa, e não percebe o ganho que estáva na frente. Você é derubado do cavalo e vate a cabeça', velocidade)

        barra_vida (40)

      print_pausado("CAPÍTULO FINAL - O DESTINO \n\n", velocidade)
      print_pausado("Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

      print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

        #decidindo escolha

      escolha = int(input(" \n  \n Digite o número escolhido: "))

      if escolha == 1:
        print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
        print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
        print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
        print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
        print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
        print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
        print_pausado("Você lança a sua espada e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser inferior ao do rei. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
        print_pausado("\n FIM DE JOGO", velocidade)

      elif escolha == 2:
        print_pausado("Você escolheu matá-las", velocidade)
        print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
        print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
        print_pausado("\n FIM DE JOGO", velocidade)
          #####FINAL DE TUDO







  #diálogo com o senhor
  if _cidadeA==4:
    print_pausado(f"-Desculpe incomodar meu senhor, não sou da região e estou procurando a estrada correta para ir ao Castelo Real, o senhor saberia para onde devo ir?\n -OI??? FALOU ALGO? EU TO MEIO SURDO, PODERIA REPETIR?\n {_nome} se assusta com o grito.. \n -Queria saber o caminho para o castelo\n - AHH SIM, O CASTELO!!! ELE NÃO ESTÁ TÃO LONGE, SE VOCÊ PEGAR A ESTRADA PARA O LAGO DA DISCÓRDIA VOCÊ CHEGARÁ COM CERTEZA!!!\n Apesar de quase ficar surdo, {_nome} agradece o senhor e se afasta.\n E agora {_nome} ?\n\nPedir Informações Para o Guarda (3)\nSeguir o Caminho do Senhor - O Lago da Discórdia (4)",velocidade)

    dialogo_senhor= int(input())
    if dialogo_senhor==4:
      print_pausado(f'Aparentemente o idoso parece ser o mais confiável.... Aquele guarda não deve lembrar nem seu nome.\n {_nome} pega a estrada para o Lago da Discórdia\n Uns 10 minutos cavalgando você encontra uma ponte e a sua unica opção é atravessa-lá. \n CRASHHHHHHHHHHHHHHH {_nome} quase infarta, assim que terminou de atravesar a ponte quebrou, agora não tem mais volta. {_nome} segue em frente e avista uma placa: 1 km Cidade Santa que leva para o Castelo Real\n {_nome} não acredita no que lê. AQUELE VELHO SURDO, falou o caminho errado!! Agora só lhe resta ir para a Cidade Santa e lá achar o caminho correto.....\n\n', velocidade)
      ###CIDADE B
      print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

      evento = 'acontecer coisas boas'
      if evento_sorte (9, evento):
        print_pausado('Você está andando pela estrada e vê uma senhora carregando uma sacola que aprece conter armas, você está curioso sobre a senhora e aprece que ela está tentando falar com você, você chega perto dela (1) ou a ignora (2)\n', velocidade)
        coisa = int(input())
        if coisa == 1:
          print_pausado('A senhora tira alguma coisa do saco e você não está certo do que é...\n', velocidade)
          print_pausado('Você chega mais perto\n', velocidade)
          print_pausado('E mais perto', velocidade)
          print_pausado('...', velocidade)
          print_pausado('A senhora dá uma machadada na sua mão por achar que está tentando rouba-la', velocidade)
          barra_vida(10)
          vida -= 10
        if coisa == 2:
          print_pausado('\nVida que segue.',velocidade)
      else:
        print_pausado(" - GRUUUUUUMMMMMM!! \n \n Opa, seu estômago está roncando alto, mas para sua sorte tem uma pomar logo a frente \n \n Ir até o pomar (1) Esperar para comer na cidade (2)  ",velocidade)

        escolha = int(input("Digite o número escolhido: "))

        if escolha == 1:
          print_pausado("As maçãs estão muito altas, você desce do cavalo e sobe em um galho para alcança-lás. \n \n - CRACCCCCCC! \n \n De repente o galho que você estava apoiado se rompe \n \n PUFT, você cai com tudo no chão e bate a cabeça, chega a ficar tonto. \n \n Não foi uma boa ideia ter ido ali.. Agora você está com fome e machucado!",velocidade)

          barra_vida(30)
          print(barra_vida)

        elif escolha == 2:
          print_pausado("Você vai para cidade e come em um bar próximo da estrada. \n \n Horas depois você começa a passar mal e 50 dinheiros seu cai no chão sem vc perceber.",velocidade)


              
        print_pausado(' CAPITULO II - A Bruxa\n\n {_nome}  chegou na cidade sagrada e por ser próxima ao castelo, o rei possui um carinho especial pela mesma. Você não sabe muito bem para onde ir, então resolve parar para descansar e quem sabe comprar algo no comércio local',velocidade)
        print_pausado('\nChegando no centro da cidade, você encontra um estranho aglomerado de pessoas',velocidade)

        print_pausado('Se enfiando no meio das pessoas, você vê que alguém armou uma estrutura  gigantesca, parece que vai acontecer algum evento ali...',velocidade)
        print_pausado('Chegando mais perto você vê uma mulher amarrada a uma estaca, aparentemente molhada e alguem segurando o que parece ser um braseiro próximo a ela.',velocidade)
        print_pausado('Claramente aquilo é uma execução pública, eles vão fazer com ela o mesmo que fizeram com sua mulher.',velocidade)
        print_pausado('A multidão grita "QUEIMEM A BRUXA"',velocidade)
        print_pausado('Você se encontra na frente da estrutura e se vê na oportunidade de interferir naquilo\n\n',velocidade)
        dec = int(input('Interferir (1)\n Ignorar (2)\n'))
        if dec == 2:
          print_pausado('Ignorando a senhora você segue seu caminho',velocidade)
          print_pausado('\nPassado algum tempo você se pergunta o porque daquilo tudo',velocidade)
          print_pausado('\nVocê busca o que acredita ser justo pra você mas não quer fazer justiça pelos outros',velocidade)
          print_pausado('\nPensando na dor e no sofrimento daqula senhora {_nome} retorna',velocidade)
          dec = 1
        
        if dec == 1:
          print_pausado('Você sobe na estrutura e desafia o carrasco',velocidade)
          print_pausado('-Quem você pensa que é forasteiro?',velocidade)
          print_pausado('-Essa execução é uma ordem direta de nossa majestade',velocidade)
          print_pausado('Você saca sua espada e o convida para um confronto direto\n',velocidade)

          evento = 'vencer o guarda'
          if evento_sorte(8 , evento):
            print_pausado('Em meio a batalha você percebe que o carrasco não era nada comparado aos desafios que você encontrou na sua carreira como guarda real\n', velocidade)
            print_pausado('Você acha uma brecha na técnica do guarda e vence a batalha.', velocidade)
            print_pausado('\n', velocidade)
            print_pausado('{_nome} liberta a senhora do tronco e a multidão se disperssa', velocidade)
            print_pausado('Conversando com a senhora, {_nome} descobre um novo caminho que o guiará para o castelo.', velocidade)
            print_pausado('\n{_nome} pega o cavalo do carrasco e segue sua vida.\n \n ', velocidade)
          else:
            print_pausado('O carrasco sorri ao ver que apesar de toda a habilidade de {_nome} com uma espada, ele está sofrendo muitos danos ', velocidade)
            print_pausado(' Por mais que atuou inúmeros anos como guarda real, seu cansaço o vence, fazendo com que você deixe uma abertura\n', velocidade)
            print_pausado('{_nome} morre', 0.4)
            sys
            time.sleep(5)
            sys.exit()


            
        #FINAL CASTELO
          print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

          evento = 'acontecer coisas boas'
          if evento_sorte(8,evento):
            print_pausado("Você está andando em direção ao castelo e vê no chão uma espada. \n Parabéns, agora ela é sua!! ", velocidade)
          else:
            print_pausado('Você está cavalgando para o castelo com muita pressa, e não percebe o ganho que estáva na frente. Você é derubado do cavalo e vate a cabeça', velocidade)

            barra_vida (40)
            
          print_pausado("CAPÍTULO FINAL - O DESTINO \n\n", velocidade)
          print_pausado("\n\n Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

          print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

            #decidindo escolha

          escolha = int(input(" \n  \n Digite o número escolhido: "))

          if escolha == 1:
            print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
            print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
            print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
            print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
            print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
            print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
            print_pausado("Você lança a sua espada e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser inferior ao do rei. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)

          elif escolha == 2:
            print_pausado("Você escolheu matá-las", velocidade)
            print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
            print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)


          else:
            print_pausado('O carrasco sorri ao ver que apesar de toda a habilidade de {nome} com uma espada, ele está levando vários danos ', velocidade)
            print_pausado(' Por mais que você atuou vários anos como guarda real, seu cansaço o vence, fazendo com que você deixe uma abertura\n', velocidade)
            print_pausado('{nome} morre', 0.4)



    elif dialogo_senhor==3:
      print_pausado(f"Mesmo com ódio de todos que trabalham para o rei, {_nome} segue em direção ao Guarda Real. \n -Olá, gostaria de saber se poderia me ajudar dizendo o caminho correto para o castelo. \n\n ",velocidade)
      
      print_pausado(f'- Zzzzzzzzzzzzzz. Opa, desculpe, a dama disse alguma coisa????  Adorei o seu vestido, combinou com seu tom de pele!!\n {_nome} Quase desmaiou com o hálito do guarda, ele está visivelmente bêbado, lhe impressiona ainda estar de pé. {_nome} insiste\n - Eu quero saber o caminho para o castelo, você sabe?\n - Você quer um martelo???? Eu sou guarda não ferreiro!!\n -CASTELOOOO, CASTELO DO REI, ONDE FICA??\n -Ah sim, castelo, por que não disse antes? Fica na direção da Floresta Sem Misericórdia, só seguir por ela, uma moça não deveria ir lá sozinha, posso lhe acompanhar!\n {_nome} se afasta do guarda que aparentemente iria lhe beijar, mas caiu de cara no chão antes que conseguisse.....\n', velocidade )
      print_pausado ('O que {_nome} fará agora?\n\nSeguir o Caminho do Guarda - A Floresta Sem Misericórdia (3)\nSeguir o Caminho do Senhor - O Lago da Discórdia (4)',velocidade )

      dialogo_guarda_senhor= int(input())
      

      if dialogo_guarda_senhor==3:
        print_pausado(f'Aparentemente o guarda parece ser o mais confiável.... Estranha decisão, mas {_nome} vai para a Floresta Sem Misericórdia, e ao adentrar no lugar entende porque se chama assim, parecia o lar de demônios, parece que o rei não quer ninguém indo até o seu castelo.\n Uns 10 minutos cavalgando você encontra uma placa: 7km Para o Castelo Real\n Quem diria, o bêbado falou a verdade....', velocidade )
        #EVENTO 2
        print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

        evento = 'acontecer coisas boas'
        if evento_sorte(8,evento):
            print_pausado("Seguindo o seu caminho você se depara com um cachorro te seguindo. \n \n -AU AU \n \n - SAI DAQUI SEU SARNENTO ESTUPIDO! \n \n - AUAUAUAU!!! \n \n Estranhamente o cachorro para. Ele quer que você o siga. \n \n Seguir o cachorro (1) Ignorar ele e continuar na sua trajetória (2)",velocidade)

            escolha = int(input("Digite a opção escolhida: "))

            if escolha == 1:
              print_pausado("Você acha aquilo bizarro, mas não custa nada seguir o animal....\n \n O Cachorro para de repente, e olha fixo para um arbusto... Curioso você desce do cavalo e vai ver o que é \n \n Você encontrou um baú!!! \n \n No mesmo instante quebra a fechadura e encontra lá dentro um pedaço de carne, um saco de maçãs e uma faca de pão (é pequena mas dá para se defender). \n \n Afinal o cachorro não era tão estúpido assim. Você o agradece dando um pedaço de carne e ele sai feliz abanando o rabo. \n \n Você sobe no cavalo, come uma maçã e segue sem olhar para trás.",velocidade)

            elif escolha == 2:
              print_pausado("Você ignora o cachorro e começa a andar mais rápido, e quando olha para trás ele já tinha desaparecido...",velocidade)
        else:
          print_pausado(" \n \n Você encontrou uma bebida no caminho e como estava com sede decidiu tomá-la... \n \n Ela estava infectada com bactérias e por isso você acaba de perder 12 pontos de vida. ", velocidade)

          barra_vida(64)
          print(barra_vida)

      #IR PARA A CIDADE C
          print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

          evento = 'acontecer coisas boas'
          if evento_sorte(8,evento):
              print_pausado("Seguindo o seu caminho você se depara com um cachorro te seguindo. \n \n -AU AU \n \n - SAI DAQUI SEU SARNENTO ESTUPIDO! \n \n - AUAUAUAU!!! \n \n Estranhamente o cachorro para. Ele quer que você o siga. \n \n Seguir o cachorro (1) Ignorar ele e continuar na sua trajetória (2)",velocidade)

              escolha = int(input("Digite a opção escolhida: "))

              if escolha == 1:
                print_pausado("Você acha aquilo bizarro, mas não custa nada seguir o animal....\n \n O Cachorro para de repente, e olha fixo para um arbusto... Curioso você desce do cavalo e vai ver o que é \n \n Você encontrou um baú!!! \n \n No mesmo instante quebra a fechadura e encontra lá dentro um pedaço de carne, um saco de maçãs e uma faca de pão (é pequena mas dá para se defender). \n \n Afinal o cachorro não era tão estúpido assim. Você o agradece dando um pedaço de carne e ele sai feliz abanando o rabo. \n \n Você sobe no cavalo, come uma maçã e segue sem olhar para trás.",velocidade)

              elif escolha == 2:
                print_pausado("Você ignora o cachorro e começa a andar mais rápido, e quando olha para trás ele já tinha desaparecido...",velocidade)
          else:
            print_pausado(" \n \n Você encontrou uma bebida no caminho e como estava com sede decidiu tomá-la... \n \n Ela estava infectada com bactérias e por isso você acaba de perder 12 pontos de vida. ", velocidade)

            barra_vida(64)
            print(barra_vida)
      
        print_pausado ( f'...... {_nome} está exausto, porém a única coisa que ele pensa é em sua vingança. \n Na frente ele vê uma placa:\n \n', velocidade)

        print_pausado_titulo('    CIDADE AMALDIÇOADA\n', velocidade)

        print_pausado_titulo('10 km para o Castelo Real\n\n',velocidade)

        print_pausado ( f'...... {_nome} acelera o cavalo, seu destino o espera daqui 10 quilomêtros....\n \n ', velocidade)



        print_pausado_titulo('    CAPÍTULO IV \n \n', velocidade)
        print_pausado_titulo(' A CIDADE AMALDIÇOADA\n', velocidade)

        print_pausado(f'Assim que {_nome} entra na cidade, ele percebe algo estranho.\n Cadê as pessoas dali?\n\n {_nome} Resolve caminhar pelo local, e finalmente encontrou as casas da vila.........\n \n Mas aquilo não eram casas, ERAM CINZAS...... \nImediatamente a imagem da sua casa vem a cabeça, {_nome} estava revivendo aquilo novamente. \n \n {_nome} avista fumaça no céu, e sai disparado para o local\n \n Uma casa estava em chamas, o calor ardia seu rosto mesmo de longe. Ao mesmo tempo a imagem de sua filha e esposa dentro da casa fixou em sua mente\n \n ',velocidade)

        print_pausado(RED + f'- SOCORRO. ME AJUDEM!!!!!!!!!!!' + RESET, velocidade)
        print_pausado ('{_nome} avista uma mulher presa por uma guia de madeira perto da casa, pelo jeito ela estava fugindo. O fogo estava se espalhando rapidamente. Sua aparência era de muito doente, dava para ver os ossos no rosto, e os olhos eram tão fundos que parecia uma  caveira\n \n' + RESET, velocidade)
        print_pausado (RED + f'{_nome} ajuda a mulher (1)   {_nome} não a ajuda a mulher (2)\n \n' + RESET, velocidade)

        ajuda_mulher= int (input ())

        if ajuda_mulher == 1:
          print_pausado('{_nome} corre para  ajudar a mulher, o calor estava imenso...',velocidade)
          print_pausado ('- PARE!!!!! ESTÁ MULHER ESTA INFECTADA COM A PESTE, VOCÊ IRÁ MORRER\n \n {_nome} se afasta com o susto e vê um homem encapuzado com uma máscara bizarra', velocidade)

          #imagem medico da peste
          print_pausado ('-Está cidade inteira está infectada com a peste negra, tentei ajudar a todos que viviam aqui, porém o rei acredita que a cidade é amaldiçoada, e sem piedade mandou queimar tudo e todos que estão aqui para purificar o reino. Esta mulher é Isadora, ela está com a peste e quase perto da morte, você chegou muito perto dela, deixei eu te examinar para ver se você esta infectado, os sintomas são muito rápidos, em menos de 3 minutos é possivel detectar o mal no corpo\n\n', velocidade)
          
          evento = 'sobreviver a doença'
          if evento_sorte(6, evento):
            print_pausado(' O médico depois de te analisar observou que você está saudável, e felizmente não irá morrer.\n', velocidade)
            print_pausado ('-Você não está infectado, deixe ela e siga seu caminho, esta cidade está acabada. \n Com um enorme pesar no peito, {_nome} segue para o castelo, determinado a acabar com isto uma vez por todas \n \n!!!', velocidade)
          else:
            print_pausado(' O médico depois de te analisar observou que você estava infectado, e infelizmente não irá sobreviver.', velocidade)
            print_pausado (f'-MEU DEUS!! VOCÊ ESTÁ INFECTADO!!! Não posso fazer nada por você, infelizmente em 1 dia você morrerá!!\n {_nome} se nega a acreditar e sai em disparada em seu cavalo. \n\n 5 horas depois {_nome} sente uma febre altíssima. \n\n 12 hrs depois {_nome} não consgeue mais andar\n\n 24 hrs depois {_nome} não consegue mais se manter no cavalo. {_nome} cai, bate a cabeça e desmaia.\n\n {_nome} nunca mais acordou!!\n\n ', velocidade)
            print_pausado_titulo ('VOCÊ MORREU!!', velocidade)
            time.sleep(5)
            sys.exit()
              
              ####CASTELO
            print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

            evento = 'acontecer coisas boas'
            if evento_sorte(8,evento):
              print_pausado("Você está andando em direção ao castelo e vê no chão uma espada. \n Parabéns, agora ela é sua!! ", velocidade)
            else:
              print_pausado('Você está cavalgando para o castelo com muita pressa, e não percebe o ganho que estáva na frente. Você é derubado do cavalo e vate a cabeça', velocidade)

              barra_vida (40)

              print_pausado("CAPÍTULO FINAL - O DESTINO \n\n", velocidade)
              print_pausado("Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

              print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

            #decidindo escolha

            if escolha == 1:
              print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
              print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
              print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
              print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
              print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
              print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
              print_pausado("Você lança a sua espada e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser inferior ao do rei. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
              print_pausado("\n FIM DE JOGO", velocidade)

            elif escolha == 2:
              print_pausado("Você escolheu matá-las", velocidade)
              print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
              print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
              print_pausado("\n FIM DE JOGO", velocidade)
                        #####FINAL DE TUDO



          
         
            

        if ajuda_mulher==2:
          print_pausado(f'{_nome} entra em choque, não consegue se movimentar, e vê naquela mulher sua esposa e filha, e quando se dá conta a mulher já estava carbonizada\n - Triste não é mesmo?\n {_nome} olha para o lado e se assusta com a pessoa que vê \n -Está cidade inteira está infectada com a peste negra, tentei ajudar a todos que viviam aqui, porém o rei acredita que a cidade é amaldiçoada, e sem piedade mandou queimar tudo e todos que estão aqui para purificar o reino. Esta mulher é Isadora, ela está com a peste e quase perto da morte, ainda bem que você não chegou perto dela,s e não poderia ter sido infectado e morrido. Infelizmente não podemos fazer nada por ela, siga seu caminho, esta cidade está acabada. \n Com um enorme pesar no peito, {_nome} segue para o castelo, determinado a acabar com isto uma vez por todas \n \n!!! ', velocidade)
          #IR PARA O CASTELO
          #FINAL
          print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

          evento = 'acontecer coisas boas'
          if evento_sorte(8,evento):
            print_pausado("Você está andando em direção ao castelo e vê no chão uma espada. \n Parabéns, agora ela é sua!! ", velocidade)
          else:
            print_pausado('Você está cavalgando para o castelo com muita pressa, e não percebe o ganho que estáva na frente. Você é derubado do cavalo e vate a cabeça', velocidade)

            barra_vida (40)

          print_pausado("CAPÍTULO FINAL - O DESTINO \n\n", velocidade)
          print_pausado("Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

          print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

          #decidindo escolha

          if escolha == 1:
            print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
            print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
            print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
            print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
            print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
            print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
            print_pausado("Você lança a sua espada e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser inferior ao do rei. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)

          elif escolha == 2:
            print_pausado("Você escolheu matá-las", velocidade)
            print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
            print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
            print_pausado("\n FIM DE JOGO", velocidade)
                      #####FINAL DE TUDO





      elif dialogo_guarda_senhor==4:
          print_pausado(f'Aparentemente o idoso parece ser o mais confiável.... Aquele guarda não deve lembrar nem o seu nome.\n {_nome} pega a estrada para o Lago da Discórdia\n Uns 10 minutos cavalgando você encontra uma ponte e a sua única opção é atravessa-lá. \n CRASHHHHHHHHHHHHHHH {_nome} quase infarta, assim que terminou de atravesar a ponte quebrou, agora não tem mais volta. {_nome} segue na frente e avista uma placa: 1 km Cidade Santa que leva para o Castelo Real\n {_nome} não acredita no que lê. AQUELE VELHO SURDO, falou o caminho errado!! Agora só lhe resta ir para a Cidade Santa e lá achar o caminho correto.....\n\n', velocidade)
          ##CIDADE B
      print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

      evento = 'acontecer coisas boas'
      if evento_sorte (9, evento):
        print_pausado('Você está andando pela estrada e vê uma senhora carregando uma sacola que aprece conter armas, você está curioso sobre a senhora e aprece que ela está tentando falar com você, você chega perto dela (1) ou a ignora (2)\n', velocidade)
        coisa = int(input())
        if coisa == 1:
          print_pausado('A senhora tira alguma coisa do saco e você não está certo do que é...\n', velocidade)
          print_pausado('Você chega mais perto\n', velocidade)
          print_pausado('E mais perto', velocidade)
          print_pausado('...', velocidade)
          print_pausado('A senhora dá uma machadada na sua mão por achar que está tentando rouba-la', velocidade)
          barra_vida(10)
          vida -= 10
        if coisa == 2:
          print_pausado('\nVida que segue.',velocidade)
      else:
        print_pausado(" - GRUUUUUUMMMMMM!! \n \n Opa, seu estômago está roncando alto, mas para sua sorte tem uma pomar logo a frente \n \n Ir até o pomar (1) Esperar para comer na cidade (2)  ",velocidade)

        escolha = int(input("Digite o número escolhido: "))

        if escolha == 1:
          print_pausado("As maçãs estão muito altas, você desce do cavalo e sobe em um galho para alcança-lás. \n \n - CRACCCCCCC! \n \n De repente o galho que você estava apoiado se rompe \n \n PUFT, você cai com tudo no chão e bate a cabeça, chega a ficar tonto. \n \n Não foi uma boa ideia ter ido ali.. Agora você está com fome e machucado! \n \n",velocidade)

          barra_vida(30)
          print(barra_vida)

        elif escolha == 2:
          print_pausado("Você vai para cidade e come em um bar próximo da estrada. \n \n Horas depois você começa a passar mal e 50 dinheiros seu cai no chão sem vc perceber.",velocidade)


                    
          print_pausado('CAPITULO II - A Bruxa \n \n {_nome} chegou na cidade de sagrada e por ser uma cidade próxima ao casetelo, o rei possui um carinho especial pela mesma. Você não sabe muito bem para onde ir, então resolve parar para descansar e quem sabe comprar algo no comércio local',velocidade)
          print_pausado('\nChegando ao centro da cidade você encontra um estranho aglomerado de pessoas\n',velocidade)
          
          print_pausado('Se enfiando no meio das pessoas você vê que alguem armou uma estrutura gigantesca, parece que vai acontecer algum evento alí...',velocidade)
          print_pausado('Chagando mais perto você vê uma mulher amarrada a uma estaca, aparentemente molhada e alguém segurando o que parece ser um braseiro próximo a ela.',velocidade)
          print_pausado('Claramente aquilo é uma execução pública, eles vão fazer com ela o mesmo que fizeram com sua mulher, só quen dessa vez em um evento público, vão mostrar a todos aquela barbaridade.',velocidade)
          print_pausado('A multidão grita "QUEIMEM A BRUXA"',velocidade)
          print_pausado('Você se encontra na frente da estrutura e se vê na oportunidade de interferir naquilo\n\n',velocidade)

          dec = int(input('Interferir (1)\n Ignorar (2)\n'))
          if dec == 2:
            print_pausado('Ignorando a senhora você segue seu caminho',velocidade)
            print_pausado('\nPassado algum tempo você se pergunta o porque daquilo tudo',velocidade)
            print_pausado('\nVocê busca o que acredita ser justo pra você mas não quer fazer justiça pelos outros',velocidade)
            print_pausado('\nPensando na dor e no sofrimento daqula senhora {_nome} retorna',velocidade)
            dec = 1
          if dec == 1:
            print_pausado('Você sobe na estrutura e desafia o carrasco',velocidade)
            print_pausado('-Quem você pensa que é forasteiro?',velocidade)
            print_pausado('-Essa execução é uma ordem direta de nossa majestade',velocidade)
            print_pausado('Você saca sua espada e o convida para um confronto direto\n',velocidade)

            evento = 'vencer o guarda'
            if evento_sorte(8 , evento):
              print_pausado('Em meio a batalha você percebe que o carrasco não era nada comparado aos desafios que você encontrou na sua carreira como guarda real\n', velocidade)
              print_pausado('Você acha uma brecha na técnica do guarda e vence a batalha.', velocidade)
              print_pausado('\n', velocidade)
              print_pausado('{_nome} liberta a senhora do tronco e a multidão se disperssa', velocidade)
              print_pausado('Conversando com a senhora, {_nome} descobre um novo caminho que o guiará para o castelo.', velocidade)
              print_pausado('\n{_nome} pega o cavalo do carrasco e segue sua vida.\n \n ', velocidade)
            else:
              print_pausado('O carrasco sorri ao ver que apesar de toda a habilidade de {_nome} com uma espada, ele está sofrendo muitos danos ', velocidade)
              print_pausado(' Por mais que atuou inúmeros anos como guarda real, seu cansaço o vence, fazendo com que você deixe uma abertura\n', velocidade)
              print_pausado('{_nome} morre', 0.4)
              time.sleep(5)
              sys.exit()

              ############SAINDO DA CIDADE#############################
              ########pocotopocotopocotopocotopocotopocoto#############
              #FINAL
            print_pausado('{_nome} estava caminahndo quando.....\n \n', velocidade)

            evento = 'acontecer coisas boas'
            if evento_sorte(8,evento):
              print_pausado("Você está andando em direção ao castelo e vê no chão uma espada. \n Parabéns, agora ela é sua!! ", velocidade)
            else:
              print_pausado('Você está cavalgando para o castelo com muita pressa, e não percebe o ganho que estáva na frente. Você é derubado do cavalo e vate a cabeça', velocidade)

              barra_vida (40)
            print_pausado("CAPÍTULO FINAL - O DESTINO \n\n", velocidade)
            print_pausado("\n\n Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

            print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

            #decidindo escolha

            escolha = int(input(" \n  \n Digite o número escolhido: "))

            if escolha == 1:
              print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
              print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
              print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
              print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
              print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
              print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
              print_pausado("Você lança a sua espada e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser inferior ao do rei. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
              print_pausado("\n FIM DE JOGO", velocidade)

            elif escolha == 2:
              print_pausado("Você escolheu matá-las", velocidade)
              print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
              print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
              print_pausado("\n FIM DE JOGO", velocidade)

              

if decisao_caminho1==2:
  ### ir para cidade B primeira decisão
  print_pausado('CAPITULO I - A Bruxa \n \n {_nome} chegou na cidade de sagrada e por ser uma cidade próxima ao casetelo, o rei possui um carinho especial pela mesma. Você não sabe muito bem para onde ir, então resolve parar para descansar e quem sabe comprar algo no comércio local',velocidade)
  print_pausado('\nChegando ao centro da cidade você encontra um estranho aglomerado de pessoas\n',velocidade)
          
  print_pausado('Se enfiando no meio das pessoas você vê que alguem armou uma estrutura gigantesca, parece que vai acontecer algum evento alí...',velocidade)
  print_pausado('Chagando mais perto você vê uma mulher amarrada a uma estaca, aparentemente molhada e alguém segurando o que parece ser um braseiro próximo a ela.',velocidade)
  print_pausado('Claramente aquilo é uma execução pública, eles vão fazer com ela o mesmo que fizeram com sua mulher, só quen dessa vez em um evento público, vão mostrar a todos aquela barbaridade.',velocidade)
  print_pausado('A multidão grita "QUEIMEM A BRUXA"',velocidade)
  print_pausado('Você se encontra na frente da estrutura e se vê na oportunidade de interferir naquilo\n\n',velocidade)

  dec = int(input('Interferir (1)\n Ignorar (2)\n'))
  if dec == 2:
    print_pausado('Ignorando a senhora você segue seu caminho',velocidade)
    print_pausado('\nPassado algum tempo você se pergunta o porque daquilo tudo',velocidade)
    print_pausado('\nVocê busca o que acredita ser justo pra você mas não quer fazer justiça pelos outros',velocidade)
    print_pausado('\nPensando na dor e no sofrimento daqula senhora {_nome} retorna',velocidade)
    dec = 1
  if dec == 1:
    print_pausado('Você sobe na estrutura e desafia o carrasco',velocidade)
    print_pausado('-Quem você pensa que é forasteiro?',velocidade)
    print_pausado('-Essa execução é uma ordem direta de nossa majestade',velocidade)
    print_pausado('Você saca sua espada e o convida para um confronto direto\n',velocidade)

    evento = 'vencer o guarda'
    if evento_sorte(8 , evento):
      print_pausado('Em meio a batalha você percebe que o carrasco não era nada comparado aos desafios que você encontrou na sua carreira como guarda real\n', velocidade)
      print_pausado('Você acha uma brecha na técnica do guarda e vence a batalha.', velocidade)
      print_pausado('\n', velocidade)
      print_pausado('{_nome} liberta a senhora do tronco e a multidão se disperssa', velocidade)
      print_pausado('Conversando com a senhora, {_nome} descobre um novo caminho que o guiará para o castelo.', velocidade)
      print_pausado('\n{_nome} pega o cavalo do carrasco e segue sua vida.\n \n ', velocidade)
    else:
      print_pausado('O carrasco sorri ao ver que apesar de toda a habilidade de {_nome} com uma espada, ele está sofrendo muitos danos ', velocidade)
      print_pausado(' Por mais que atuou inúmeros anos como guarda real, seu cansaço o vence, fazendo com que você deixe uma abertura\n', velocidade)
      print_pausado('{_nome} morre', 0.4)
      time.sleep(5)
      sys.exit()

              ############SAINDO DA CIDADE#############################
              ########pocotopocotopocotopocotopocotopocoto#############
              #FINAL
  print_pausado("CAPÍTULO III - O DESTINO \n\n", velocidade)
  print_pausado("\n\n Você chegou no castelo e se deparou com um antigo amigo seu. \n Ele permite a sua entrada.", velocidade)

  print_pausado(" \n  Você entra nos aposentos do rei e lá encontra a mulher e filha do seu odiável rei. \n \n Você tem duas opções: Seguir procurando o rei (1) ou matá-las (2)", velocidade)

        #decidindo escolha

  escolha = int(input(" \n  \n Digite o número escolhido: "))

  if escolha == 1:
    print_pausado(" \n Você escolheu seguir procurando o rei \n ", velocidade)
    print_pausado("No seu caminho de busca pelo rei, ele aparece na sua frente inesperadamente. \n", velocidade)
    print_pausado("Você diz: 'Eu vim aqui para vingar a morte da minha mulher e filha. Seu mandato no poder acaba aqui, ordinário", velocidade)
    print_pausado("\n Rei: Eu faço isso pelo bem do povo", velocidade)
    print_pausado("\n {_nome} : Você faz isso pelo seu próprio bem, ganancioso. \n EU VOU TE MATAR", velocidade)
    print_pausado("A luta acontece entre {_nome} e o rei. \n ", velocidade)
    print_pausado("Você lança a sua espada e ataca o rei. \n O rei contra-ataca você. Você consegue ter vantagem na luta apesar de sua espada ser inferior ao do rei. \n \n VOCÊ ARRANCA A CABEÇA DO REI!", velocidade)
    print_pausado("\n FIM DE JOGO", velocidade)

  elif escolha == 2:
    print_pausado("Você escolheu matá-las", velocidade)
    print_pausado("\n Logo após você esfaquear a mulher filha do rei, guardas reais chegam e te levam para uma prisão solitária", velocidade)
    print_pausado("\n Você é preso e apodrece na prisão por ter feito a mesma coisa que fizeram com sua família.", velocidade)
    print_pausado("\n FIM DE JOGO", velocidade)

   