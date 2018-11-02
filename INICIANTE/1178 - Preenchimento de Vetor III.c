// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Preenchimento de Vetor III
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1178

#include <stdio.h>
int main(){
  int i=0,j=0;
  double n,vetor[100];
  scanf("%lf",&n);
  while (i<100){
    vetor[i]=n/pow(2,i);
    printf("N[%d] = %.4lf\n",i,vetor[i]);
    i++;
  }
}
