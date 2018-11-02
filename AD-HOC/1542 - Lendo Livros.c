// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Lendo Livros
// Nível: 1
// Categoria: AD-HOC
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1542

#include<stdio.h>
#include<math.h>
#include<stdlib.h>
  
int main () {
  
    int Q, D, P;
    int x, res;
  
    while ( 1 ) {
        scanf ( "%d", &Q );
        if ( Q==0 ) return 0;
        scanf ( "%d %d", &D, &P );
 
        x = (double) (Q*D)/(P-Q)*P;
        res = floor(x);
 
        if ( res == 1 ) printf ( "%d pagina\n", res );
        else printf ( "%d paginas\n", res );
    }
}
