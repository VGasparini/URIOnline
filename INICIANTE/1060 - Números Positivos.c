// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Números Positivos
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1060

#include <stdio.h>

void main(void)
{
float n,p,i;
for(i=1;i<=6;i++){
    scanf("%f",&n);
    if(n>0){p++;}
}
printf("%.0f valores positivos\n",p);
}

