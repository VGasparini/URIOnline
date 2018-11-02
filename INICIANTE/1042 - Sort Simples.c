// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Sort Simples
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

#include <stdio.h>

int main() {

    int a,b,c,x,y,z,temp;

    scanf("%d %d %d",&a,&b,&c);

    x=a;
    y=b;
    z=c;
    if (x<y)
    {
        temp=x;
        x=y;
        y=temp;
    }
    if (y<z)
    {
        temp=y;
        y=z;
        z=temp;
    }
    if (x<y)
    {
        temp=x;
        x=y;
        y=temp;
    }
    printf("%d\n%d\n%d\n\n%d\n%d\n%d\n",z,y,x,a,b,c);
}
