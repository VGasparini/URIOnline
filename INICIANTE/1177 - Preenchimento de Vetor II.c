// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Preenchimento de Vetor II
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1177

#include <stdio.h>
int main(){
  int n,i,j=0,vetor[1000];
  scanf("%d",&n);
  while (i<1000){
    if(j==n){
      j=0;
      vetor[i]=j;
      printf("N[%d] = %d\n",i,vetor[i]);
      j++;
    }
    else{
      vetor[i]=j;
      printf("N[%d] = %d\n",i,vetor[i]);
      j++;
    }
    i++;
  }
}
