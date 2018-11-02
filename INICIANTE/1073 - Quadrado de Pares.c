// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Quadrado de Pares
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1073

#include <stdio.h>
#include <math.h>

void main(void)
{
int n,i=2;
scanf("%d",&n);
do{
        printf("%d^2 = %d\n",i,(int)pow(i,2));
        i+=2;
 }while(i<=n);
}

