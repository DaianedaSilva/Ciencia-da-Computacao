#include <iostream>
using namespace std;
#define tamanho 4
/*
Caracteristicas de uma fila:
  tem 2 ponteiros, um mostrando onde é o inicio e outra onde é o fim

  Sempre o primeiro a entrar é o primeiro a sair (FIFO - first in, first out)

  Os elementos são inseridos no final da fila e removidos do começo

  sempre colocamos no final, e tiramos do inicio

Criar uma fila:
  usamos um vetor, para armazenar os elementos
  2 modos de implementar:
    Sempre retirar do indice 0, e dps deslocar todos os outros elementos 1 indice para a esquerda

    Sempre ao retirarmos um elemento, ao invés de mexer todo mundo, mudamos para onde o ponteiro do inicio aponta 
*/

typedef struct {
  int inicio;
  int fim;
  int qtd;
  int fila[tamanho];
}FILA;


void iniciar(FILA &f){
  f.inicio=-1;
  f.fim=-1;
  f.qtd=0;
}

void Verifilacheia(FILA &f){
    if (f.qtd < tamanho){
        cout<<f.qtd<<"\nPode inserir .\n";
    }
    else{
        cout<<f.qtd<<", Já passamos do tamanho , favor esperar o proximo sair da fila \n";
    }
}

void inserir(FILA &f,int x){
    if(f.qtd==0){
        f.inicio=0;
        f.fim=0;

    }
    else{
        f.fim+=1;  
    }

    f.fila[f.fim]=x;
    f.qtd+=1;
}

int remover(FILA &f){
  cout<<f.fila[f.inicio]<<", esse sujeito será removido da fila"<<endl;
  f.qtd-=1;

  return f.fila[f.inicio++];
  
}

void imprimir(FILA f){
  for(int i=f.inicio;i<f.fim+1;i++){
    cout<<f.fila[i] <<endl;
  }
}

bool vazia (FILA &f){
  cout << "valor do qde"<<f.qtd<<endl;
  
  if (f.qtd == 0){
    cout<<"lista vazia pode inserir ";
    return true;
  }else{
    cout << " \n\nNão esta vazia";
    return false;
  }
}


int main() {
    cout << "Essa é minha fila BEM VINDO \n";

    FILA fila;


    iniciar(fila);

    inserir(fila,12);
    inserir(fila,5);
    inserir(fila,46);
    inserir(fila,85);

    imprimir(fila);
    cout<<"\n O tamanho da fila é: "<<fila.qtd <<endl;    remover(fila);



    remover(fila); 
    cout<< endl << endl ;
    imprimir(fila);


    vazia (fila);

    Verifilacheia(fila);
    inserir(fila,55);
    imprimir(fila);


    cout<< endl << endl ;
    inserir(fila,55);
    remover(fila);
    imprimir(fila);

    cout<< fila.inicio;

  return 0;
}