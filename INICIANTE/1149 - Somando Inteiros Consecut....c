// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Somando Inteiros Consecut...
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1149

#include <stdio.h>
int main()
{
    int X, N, a,b=0;
    scanf("%d %d", &X, &N);
    while(N<=0)
        scanf("%d", &N);
    for(a=1; a<=N; a++)
    {
        b+=X;
        X++;
    }
    printf("%d\n",b);
    return 0;
}
