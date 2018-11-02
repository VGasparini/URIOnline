// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Dividindo X por Y
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1116

#include <stdio.h>

int main(){
    int n,a,b,i;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        scanf("%d %d",&a,&b);
        if(b==0){printf("divisao impossivel\n");}
        else{printf("%.1f\n",(float)((float)a/(float)b));}
    }
}
