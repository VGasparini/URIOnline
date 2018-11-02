// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Seleçao em Vetor I
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1174

#include <stdio.h>
int main()
{
    double n[100];
    int i,c;
    for(i=0;i<100;i++)
    {
        scanf("%lf",&n[i]);
        if(n[i]<=10) printf("A[%d] = %.1lf\n",i,n[i]);
    }
}

