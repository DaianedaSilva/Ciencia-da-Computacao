def buscar(arquivo, item):
  lista = [] #Definindo uma lista vazia para pegar as linhas do arquivo
  first = 0 #inicio do vetor
   #fim do vetor
  found = False
   
  for linha in arquivo:#Para cada linha no arquivo, add na lista vazia
    linha = linha.strip()
    lista.append(linha) 
  
  lista.sort()
  
  last = len(lista)-1
  while first<=last and (found == False):
    #Aplicando a busca binária
    midpoint = (first + last)//2
    if item in lista[midpoint]:
        found = True
    else:
        if item < lista[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
  return found

arquivo = open('produtos.txt', 'r')#Acessando o arquivo como leitura

busca = buscar(arquivo, "mamão")
print(busca)
arquivo.close()