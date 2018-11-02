// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Consumo
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

#include <stdio.h>

int main() {
	int dist;
	float gas;
	scanf("%d %f",&dist,&gas);
	printf("%.3f km/l\n",dist/gas);
	return 0;
}
