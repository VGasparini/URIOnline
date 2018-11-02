// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Idades
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1154

#include <stdio.h>
int main()
{
    int i,m=0,j=0;

    while(1)
    {
        scanf("%d",&i);
        if(i>0){
            m+=i;
            j++;
        }
        else{
            break;
        }
    }
    printf("%.2f\n",(float)m/(float)j);
}

