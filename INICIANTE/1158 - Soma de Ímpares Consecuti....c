// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Soma de Ímpares Consecuti...
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1158

#include <stdio.h>
int main()
{
    int n,x,y,a,b,c,d,e;
    scanf("%d", &n);
    for(a=1; a<=n; a++)
    {
        scanf("%d %d", &x, &y);
        if(x%2==1)
        {
            c=0;
            for(b=1; b<=y; b++)
            {
                c+=x;
                x+=2;
            }
            printf("%d\n", c);
        }
        else
        {
            x++;
            c=0;
            for(b=1; b<=y; b++)
            {
                c+=x;
                x+=2;
            }
            printf("%d\n", c);
        }
    }
}

