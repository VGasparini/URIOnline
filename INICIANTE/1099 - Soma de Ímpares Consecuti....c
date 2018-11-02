// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Soma de Ímpares Consecuti...
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1099

#include <stdio.h>
int main()
{
    int a,b,c=0,i,n;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
    scanf("%d %d", &a, &b);
    if(a==b)
        printf("%d\n",c);
    else if(a<b)
    {
        for(a=a+1;a<b;a++)
        {
            if(a%2==1||a%2==-1)
                c+=a;
        }
        printf("%d\n",c);
    }
    else if(a>b)
    {
        for(b=b+1;b<a;b++)
        {
            if(b%2==1||b%2==-1)
                c+=b;
        }
        printf("%d\n",c);
    }
    c=0;
    }
    return 0;
}

