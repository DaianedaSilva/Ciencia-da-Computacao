#include <iostream>
using namespace std;

/*
LISTA SIMPLESMENTE ENCADEADA

ESTRUTURA:
   ________           ________         ________         ____________
  |__HEAD__| --->    |_ X | __|  ---> |_ Y | __| ----> |_ Y_ |_NULL_|

  Primeiro temos um nó que não tem dado (HEAD), serve apenas para apontar onde começa a lista, ou seja tem o endereço do primeiro nó da lista, 
  O primeiro nó tem um dado (x), e um ponteiro que aponta para o próximo nó, e assim são todos os outros nós, COM EXESSÃO DO ULTIMO nó

  ULTIMO NÓ: o ponteiro dele que apontaria para o próximo tem o valor NULL, pois não temos um próximo.

O QUE A ESTRUTURA TERÁ:
  variável (int ou char) contendo o dado do nó
  um ponteiro do tipo da estrutura do nó, onde terá o valor do endereço do próximo nó

MÉTODOS:  

  INICIALIZA_LISTA:
    Método que irá criar o head, ou seja um nó sem nenhum dado

  INSERIR_DADO_NO_INÍCIO:
    método que irá criar um nó com um novo dado.
    
  
  REMOVER_ELEMENTO:
    Método que irá remver um dado da lista
*/


/*ESTRUTURA DA LISTA*/
struct Node{
  int dado;     //dado que o nó guardará
  Node *prox;  //ponteiro que sinalizará onde está o proximo No
  int quantidade; // para auxiliar a sabe quantos itens tem dentro da lista
};

/*Criando o Head, retornaremos NULL para todos os dados que tem em um Nó, No MAIN guardaremos este retorno em um No*/
Node * Inicializa(){
  return NULL;
}

/* inserindo um novo nó com um dado
* para inserir precisamos:
    de uma lista que é onde iremos colocar o nó
    do valor que será inserido

  *criaremos um novo nó dentro da função onde:
    seu dado será o valor passado
    o ponteiro apontará para a lista passada, que conté é um nó, 
    (lembre-se que na hr de criar uma lista criamos ela ao contrário, apontamos para quem já está na lista, não tem como apontar para algo que não existe então o formato na hr de criar seria:
    head <- nó1 <- nó2 <- nó3
    
    Pois quando fomos acessar acessaremos do Nó3 para o restante, então o próximo do nó 3 é no nó2:
    nó3 -> nó2 -> nó1 -> head)


*/
Node * Inserindo_Node_Inicio(Node * node_anterior, int valor){
  Node * novo_no =  new Node;  // criando um novo nó

  //inserindo o valor passado no dado do novo nó da lista
  novo_no->dado = valor;
  novo_no->prox = node_anterior; 
  return novo_no; 
};

/*Inserindo um nó no meio da lista
Precisamos da lista que será colocado o valor, e o valor que será colocado e a posição que quer coloccar

iremos percorrer a lista ate encontrar a posição, quando encontrar:
     ________         _____________         ________
    |_ W_| __|  ---> |_ NOVO __| __|  ---> |_ Y | __|
  
  novo.prox = no_anterior.prox (y)
  no_anterior.prox = novo
 

*/
Node * Inserindo_No_Posicao( Node * lista, int valor, int posicao ){

    Node * novo_node = new Node;

    novo_node->dado = valor;

    Node * aux = lista;

    Node * node_anterior = new Node;

    if ( posicao == 0){
     
      lista = Inserindo_Node_Inicio(lista, valor);
    
    }else{
        for (int i = 0; i != posicao+1; i++){
          if (i == posicao){
          novo_node->prox = node_anterior->prox;
          node_anterior ->prox = novo_node;

          }
          node_anterior = aux;
          aux = aux->prox;
        }

      }
  return lista;
}

/*removendo um dado do lista
  Precisamos:
    da lista com os nós, e o dado que queremos retirar
  
  OQ FAZER:
    Queremos tirar o X da lista; para isso:
    * o prox do W apontará para o Y (que é o prox do x)
    * Deletar o nó
    __________        ________         ________
    |_ W | __|  ---> |_ X | __|  ---> |_ Y | __|
  
  Como fazer:
    percorra toda a lista ate encontrar o dado
  
*/

Node * Retirar_Node(Node * lista, int valor){
  
  Node * node = lista;

  Node * prox_node = node->prox;

  /*criaremos um nó auxiliar que irá rodar todos os nós da lista (node)
  
  criaremos um outro que receberá o próximo deste nó, onde verificaremos se o valor é igual ao que queremos tirar
    se for igual:
      pegamos o proximo do prox_node e guardamos no nó atual, excluir este nó*/

  /*precisamos verificar se ele esta na primeira posição da lista, se tiver o proximo é NULL, então para excluir ele é so falar que a lista é igual a NULL, ou seja igual o primeiro*/
  if (node->dado == valor && node->prox == NULL){
        lista = prox_node;
    

  }else{
    for(node = lista; node != NULL; node = node->prox ){
  
    if (prox_node != NULL && prox_node->dado == valor){
        node->prox = prox_node->prox;
        
    }
     prox_node = node->prox;
    }
  } 

  return lista;
}

/*verificando se o a lista está vazia
  se a lista esta vazia nela so temos um nó: o HEAD, que contém o valor null, então é so verificar se a lista é igual a NULL;
  PRECISAMOS:
    Da lista que queremos verificar se esta vazia
*/
bool IsEmpty(Node * lista){
  if (lista == NULL){
    cout<<endl<<"Sua lista está vazia"<<endl;
    return true;
  }else{
    return false;
  }
};

/*buscando um elemento na lista

oq precisamos:
  da lista que irá procurar, do elemento que será procurado

Como fazer:
  Rodar todos os nós e verificar o valor, se for igual ao dado daquele nó mostrar a posição que ele se encontra

*/
bool Busca_Dado(Node * lista, int valor){
  Node * aux = lista;
  int cont = 0;
  while(!IsEmpty(aux)){
    
    if (aux->dado == valor){
        cout<<"Valor " <<aux->dado<< ", encontrado na posição: " <<cont;
        return true;
    }
    aux = aux->prox;
    cont++;
  }
  return false;
}

/*mostrando a lista na tela */
void Imprimindo_Lista(Node * lista){
  cout<<"\n\nIMPRIMINDO A LISTA: \n\n";
  while (lista != NULL){
    cout<< lista->dado << " - " ;
    lista = lista->prox;
  }
  cout<<endl;

}

/*mostrando a lista na tela */
void Tamanho_Lista(Node * lista){
  cout<<"\nIMPRIMINDO A LISTA: \n\n";
  int c = 0;
  while (lista != NULL){
    
    lista = lista->prox;
    c++;
  }
   cout<<"\nA lista tem: "<<c<<" dados \n\n";

}

int main() {
  cout << "Estrutura de Lista Simplesmente Encadeada\n";

  /* criando a lista, ou seja uma estrutura que terá nós, não esqueça que essa estrutura tem um ponteiro então é necessário criar como um ponteiro */
  Node * lista = new Node;

  lista = Inicializa(); //aqui estamos criando uma lista com um nó com valores nulos ( NOSSO HEAD), 
  
  IsEmpty(lista);
  int pos = 0;
  int opc;
  int valor;

  while (true){
    cout<<"\n-------------------------------------------------------";
    cout<<"\n\n0 - Sair";
    cout<<"\n\n1 - Entrar na fila";
    cout<<"\n\n2 - Sair da fila ";
    cout<<"\n\n3- Verifica se o item, está na fila (retorna a posição na fila, se nao estiver, retorna 0 ";
    cout<<"\n\n4 - Tamanho da fila\n\nOpção: ";
 
    cin >>opc;
    cout<<"\n-------------------------------------------------------";
    if (opc == 0){
        cout<<"Finalizado";
        break;
    }
      if (opc == 1){
          cout<<"\nEntrou na opção 1";
          cout<<"\nInsira o valor que quer colocar na lista: ";
          cin>>valor;
          lista = Inserindo_Node_Inicio(lista,valor);
          //lista = Inserindo_No_Posicao(lista,valor, pos);

          cout<<"\nEntrou na opção 1";
          pos++;
          Imprimindo_Lista(lista);
    }
      if (opc == 2){
          cout<<"\nEntrou na opção 2";
          cout<<"\nInsira o valor que quer retirar da lista: ";
          cin>>valor;
          lista = Retirar_Node(lista, valor);
          Imprimindo_Lista(lista);
    }                 
      if (opc == 3){
          cout<<"\nEntrou na opção 3";
          cout<<"\nInsira o valor que quer buscar na lista: ";
          cin>>valor;
          Busca_Dado(lista, valor);
    }
      if (opc == 4){
          cout<<"\nEntrou na opção 4";
          cout<<"\nTamanho da fila";
          Tamanho_Lista(lista);

    }
      


  }
    
return 0;
}