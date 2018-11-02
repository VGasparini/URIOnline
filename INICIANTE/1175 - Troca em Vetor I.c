// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Troca em Vetor I
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1175

#include <stdio.h>
int main()
{
    int n[20],ni[20];
    int i,c;
    for(i=0;i<20;i++)
    {
        scanf("%d",&n[19-i]);
    }
    for(i=0;i<20;i++)
    {
        printf("N[%d] = %d\n",i,n[i]);
    }
}

