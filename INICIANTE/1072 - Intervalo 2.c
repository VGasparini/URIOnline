// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Intervalo 2
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1072

#include <stdio.h>

void main(void)
{
int a,n,in=0,out=0;
scanf("%d",&n);
do{
    scanf("%d",&a);
    if(a>=10 && a<=20){in++;}
    else{out++;}
    n--;
 }while(n>0);
 printf("%d in\n%d out\n",in,out);
}

