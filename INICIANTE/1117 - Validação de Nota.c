// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Validação de Nota
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1117

#include <stdio.h>
int main()
{
    double a,b,c=0,d=0;
    while(1)
    {
        if(d==2)
            break;
        scanf("%lf", &a);
        if(a>=0 && a<=10)
        {
            d++;
            c+=a;
        }
        else
            printf("nota invalida\n");
    }
    printf("media = %.2lf\n", c/2.00);
    return 0;
}
