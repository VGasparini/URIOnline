// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Números Ímpares
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1067

#include <stdio.h>

int main(){
int i,n;

scanf("%d",&n);
for(i=0;i<=n;i++){
	if(i%2!=0) printf("%d\n",i);
}
}
