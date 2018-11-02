// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Crescimento Populacional
// Nível: 2
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1160

#include <stdio.h>

int main(){

int t,i,c=0,pa,pb;
double g1,g2;

scanf("%d",&t);
for(i=1;i<=t;i++){
    scanf("%d %d %lf %lf",&pa,&pb,&g1,&g2);
    while(pa<=pb){
        pa+= pa*(g1*.01);
        pb+= pb*(g2*.01);
        c++;
        if(c>100){
            break;
        }
    }
    if(c>100) printf("Mais de 1 seculo.\n");
    else{printf("%d anos.\n",c);}
    c=0;
}
}

