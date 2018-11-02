// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Leitura Ótica
// Nível: 2
// Categoria: AD-HOC
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1129

#include <stdio.h>
int main ()
{
    int n, i, A, B, C, D, E;
    scanf ("%d",&n);    
    do{
    	for (i=n;i!=0;i--){
        scanf ("%d %d %d %d %d", &A, &B, &C, &D, &E);
        if (A<=127 && B>127 && C>127 && D>127 && E>127) printf ("A\n");
        else if (A>127 && B<=127 && C>127 && D>127 && E>127) printf ("B\n");
        else if (A>127 && B>127 && C<=127 && D>127 && E>127) printf ("C\n");
        else if (A>127 && B>127 && C>127 && D<=127 && E>127) printf ("D\n");
        else if (A>127 && B>127 && C>127 && D>127 && E<=127) printf ("E\n");
        else printf ("*\n");   
    	}
    scanf ("%d",&n);
    } while (n!=0); 
}
