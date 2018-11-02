// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Salário com Bônus
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

#include <stdio.h>

int main() {
    char nome;
	double sal,vend;
	scanf("%s %lf %lf",&nome,&sal,&vend);
	printf("TOTAL = R$ %.2lf\n",sal+.15*vend);
	return 0;
}
