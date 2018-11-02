// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Sequencia IJ 1
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1095

#include <stdio.h>

void main(void)
{
 int j,i=1;
 for(j=60;j>=0;j-=5){
    printf("I=%d J=%d\n",i,j);
    i+=3;
 }
}

