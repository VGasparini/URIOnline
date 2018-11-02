// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Tempo de Jogo
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

#include <stdio.h>

int main(void) {

	int h_inicial, h_final, duracao;
	scanf("%d %d",&h_inicial, &h_final);
	if (h_inicial >= h_final){
        duracao = 24 - h_inicial + h_final;
	}else{
        duracao = h_final - h_inicial;
	}
    printf("O JOGO DUROU %d HORA(S)\n", duracao);
	return 0;
}
