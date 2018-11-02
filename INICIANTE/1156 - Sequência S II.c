// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Sequência S II
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1156

#include <stdio.h>
int main()
{
    float s=0,i,j=1;
    for(i=1; i<=39; i=i+2){
        s+=i/j;
        j+=j;
    }
    printf("%.2f\n",s);
}

