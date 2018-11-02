// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Várias Notas Com Validação
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1118

#include <stdio.h>
#include <stdlib.h>

int verifica(float nota){
	if (nota<0 || nota>10){
		return 0;
	}
	else{
		return 1;
	}
}

int main(){
	int op,cont;
	float nota,soma;
	
	do{
		scan:
		scanf("%f",&nota);
		if(verifica(nota) == 0){
			printf("nota invalida\n");
			goto scan;
		}
		else if(verifica(nota) == 1){
			soma += nota;
			cont++;
		}
		if(cont == 2){
			printf("media = %.2f\n",soma/2);
			cont = 0;
			soma = 0;
			opcao:
			printf("novo calculo (1-sim 2-nao)\n");
			scanf("%d",&op);
			if(op == 1) goto scan;
			else if (op == 2) soma=0;
			else goto opcao;
		}
}while(op != 2);
}
