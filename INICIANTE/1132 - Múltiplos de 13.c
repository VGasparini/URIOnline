// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Múltiplos de 13
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1132

int main()
{
    int a,b,c=0,i;
    scanf("%d%d", &a, &b);
    if(a<b)
    {
        for(i=a; i<=b; i++)
        {
            if(i%13==0) continue;
            c+=i;
        }
    }
    else if(a>b)
    {
        for(i=b; i<=a; i++)
        {
            if(i%13==0) continue;
            c+=i;
        }
    }
    printf("%d\n",c);
    return 0;
}

