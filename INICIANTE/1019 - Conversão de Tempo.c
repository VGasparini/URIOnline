// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Conversão de Tempo
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

#include <stdio.h>
 
int main (void){
 
    //int n;
    int n, h,m,s;
    scanf ("%d", &n);
    h=n/3600;
    m=((n%3600)/60-60)+60;
    s=n-(n/60)*60;
    printf ("%d:%d:%d\n",h,m,s);
    return 0;
}
