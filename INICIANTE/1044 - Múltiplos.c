// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Múltiplos
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

#include <stdio.h>
#include <math.h>

int main() {
    int a,b,s;
    scanf("%d %d",&a,&b);

    s=(a+b+(abs(a-b)))/2;
    if (s%a==0 && s%b==0){
        printf("Sao Multiplos\n");
    }
    else{
        printf("Nao sao Multiplos\n");
    }
return 0;
}
