// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Substituição em Vetor I
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1172

#include <stdio.h>
int main()
{
    int n[10], temp,i,j;
    for(i=0; i<10; i++)
        scanf("%d",&n[i]);
    for(i=0; i<10; i++)
    {
        if(n[i]<=0)
            n[i]=1;
    }
    for(i=0; i<10; i++)
        printf("X[%d] = %d\n",i,n[i]);
    return 0;
}

