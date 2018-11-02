// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Idade em Dias
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

#include <stdio.h>
 
int main (void){

    int i, a,m,d;
    scanf ("%d", &i);
    a=i/365;
    m=(i-a*365)/30;
    d=i-(a*365+m*30);
    printf ("%d ano(s)\n%d mes(es)\n%d dia(s)\n",a,m,d);
    return 0;
}
