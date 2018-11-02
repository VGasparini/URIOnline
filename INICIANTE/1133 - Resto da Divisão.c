// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Resto da Divisão
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1133

#include <stdio.h>
int main()
{
    int x,y,i,t;

    scanf("%d %d",&x,&y);
    if(x>y){
        for(i=1;i<(x-y);i++){
            t=y+i;
            if(t%5==2 || t%5==3){printf("%d\n",t);}
        }
    }
    else if(x<y){
        for(i=1;i<(y-x);i++){
            t=x+i;
            if(t%5==2 || t%5==3){printf("%d\n",t);}
        }
    }
}

