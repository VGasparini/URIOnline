// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Cálculo Simples
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

#include <stdio.h>

int main() {
    int cd1,cd2,qt1,qt2;
	double pr1,pr2;
	scanf("%d %d %lf",&cd1,&qt1,&pr1);
	scanf("%d %d %lf",&cd2,&qt2,&pr2);
	printf("VALOR A PAGAR: R$ %.2lf\n",qt1*pr1+qt2*pr2);
	return 0;
}
