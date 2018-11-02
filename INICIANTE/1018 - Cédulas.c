// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Cédulas
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

#include <stdio.h>
 
int main (void){
 
    int q = 0, c;
    scanf ("%d", &q);
    printf ("%d\n",q);
 
    c=(q-(q%100))/100;
    printf ("%d nota(s) de R$ 100,00\n", c);
    q=q%100 ;
 
    c=(q-(q%50))/50;
    printf ("%d nota(s) de R$ 50,00\n", c);
    q=q%50 ;
 
    c=(q-(q%20))/20;
    printf ("%d nota(s) de R$ 20,00\n", c);
    q=q%20 ;
 
    c=(q-(q%10))/10;
    printf ("%d nota(s) de R$ 10,00\n", c);
    q=q%10 ;
 
    c=(q-(q%5))/5;
    printf ("%d nota(s) de R$ 5,00\n", c);
    q=q%5 ;
 
    c=(q-(q%2))/2;
    printf ("%d nota(s) de R$ 2,00\n", c);
    q=q%2 ;
 
 
    printf ("%d nota(s) de R$ 1,00\n", q);
    return 0;
}
