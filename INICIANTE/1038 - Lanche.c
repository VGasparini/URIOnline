// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Lanche
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

#include <stdio.h>
#include <stdlib.h>

int main(){
	
	float a, b, val;
	scanf("%f %f", &a, &b);
	if(a<=5){
		if(a==1){
			val=b*4.00;
		}else if(a==2){
			val=b*4.50;
		}else if(a==3){
			val=b*5.00;
		}else if(a==4){
			val=b*2.00;
		}else if(a==5){
			val=b*1.50;
		}
	}printf("Total: R$ %.2f\n", val);
	return 0;
}
