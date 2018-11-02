// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Par ou Ímpar
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1074

#include <stdio.h>

int main(){
    int i,n,x;
    scanf("%d",&x);
    for(i=1;i<=x;i++){
        scanf("%d",&n);
        if(n==0){printf("NULL\n");}
        else{
        if(n%2==0){printf("EVEN ");}
        else{printf("ODD ");}
        if(n>0){printf("POSITIVE\n");}
        else{printf("NEGATIVE\n");}
        }
    }
}

