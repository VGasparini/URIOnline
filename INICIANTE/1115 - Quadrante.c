// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Quadrante
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1115

#include <stdio.h>

int main(){
    int a=1,b=1;
    do{
        scanf("%d %d",&a,&b);
        if(a>0 && b>0){printf("primeiro\n");}
        else if(a<0 && b>0){printf("segundo\n");}
        else if(a<0 && b<0){printf("terceiro\n");}
        else if(a>0 && b<0){printf("quarto\n");}
        else{break;}
    }while(a!=0 || b!=0);
}
