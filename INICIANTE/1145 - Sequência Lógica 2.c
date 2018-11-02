// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Sequência Lógica 2
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1145

#include <stdio.h>
int main()
{
    int x,y,j=0,i;
    scanf("%d %d",&x,&y);
    for(i=1;i<=y;i++){
        printf("%d",i);
        j++;
        if(j==x){
            printf("\n");
            j=0;
        }
        else{printf(" ");}
    }
}

