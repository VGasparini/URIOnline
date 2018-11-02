// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Animal
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

#include <stdio.h>
#include <string.h>
int main()
{
    char a1[]="aguia", a2[]="pomba", a3[]="homem", a4[]="vaca", a5[]="pulga", a6[]="lagarta", a7[]="sanguessuga", a8[]="minhoca";
    char c1[]="vertebrado", c11[]="ave", c12[]="mamifero";
    char c111[]="carnivoro", c112[]="onivoro", c122[]="herbivoro";
    char c2[]="invertebrado", c21[]="inseto", c22[]="anelideo";
    char c211[]="hematofago";
    char a[10], b[10], c[10];
    scanf("%s", a);
    if(0==strcmp(a,c1))
    {
        scanf("%s",b);
        if(0==strcmp(b,c11))
        {
            scanf("%s",c);
            if(0==strcmp(c,c111))
                printf("%s\n",a1);
            else if(0==strcmp(c,c112))
                printf("%s\n",a2);
        }
        if(0==strcmp(b,c12))
        {
            scanf("%s",&c);
            if(0==strcmp(c,c112))
                printf("%s\n",a3);
            else if(0==strcmp(c,c122))
                printf("%s\n",a4);
        }
    }
    else if(0==strcmp(a,c2))
    {
        scanf("%s",b);
        if(0==strcmp(b,c21))
        {
            scanf("%s",&c);
            if(0==strcmp(c,c211))
                printf("%s\n",a5);
            else if(0==strcmp(c,c122))
                printf("%s\n",a6);
        }
        if(0==strcmp(b,c22))
        {
            scanf("%s",&c);
            if(0==strcmp(c,c211))
                printf("%s\n",a7);
            else if(0==strcmp(c,c112))
                printf("%s\n",a8);
        }
    }
    return 0;
}

