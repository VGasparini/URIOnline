// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Triangulação de Delaunay
// Nível: 1
// Categoria: MATEMÁTICA
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1620

#include <cstdio>
using namespace std;

int main()
{
	long double l, i, x;

	while(scanf("%Lf", &l) && l != 0)
	{
		i = ((l - 3) * 2) + 3;
		x = (i - l) / l;
		printf("%.6Lf\n", x);
	}

	return 0;
}
