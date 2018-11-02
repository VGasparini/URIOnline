// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Senha Fixa
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1114

#include <stdio.h>

int main(){
    int p,ps;
    do{
        ps=2002;
        scanf("%d",&p);
        if(p!=ps){
            printf("Senha Invalida\n");
        }
        else{break;}
    }while(p!=ps);
    printf("Acesso Permitido\n");
}
