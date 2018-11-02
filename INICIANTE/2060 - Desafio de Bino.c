// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Desafio de Bino
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2060

#include <stdio.h>
 
int main() {
 
    int n,num,i,cont2=0,cont3=0,cont4=0,cont5=0;
    
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&num);
        if (num%2 == 0) cont2++;
        if (num%3 == 0) cont3++;
        if (num%4 == 0) cont4++;
        if (num%5 == 0) cont5++;
    }
    printf("%d Multiplo(s) de 2\n%d Multiplo(s) de 3\n%d Multiplo(s) de 4\n%d Multiplo(s) de 5\n",cont2,cont3,cont4,cont5);
    return 0;
}
