// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Média 3
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1040

#include <stdio.h>

int main(void) {
	
	float n1,n2,n3,n4,media;
	
	scanf("%f %f %f %f",&n1,&n2,&n3,&n4);
	media=n1*.2+n2*.3+n3*.4+n4*.1;
	printf("Media: %.1f\n",media);
	if(media>=7){
	    printf("Aluno aprovado.\n");
	}else{
	    if(media<5){
	        printf("Aluno reprovado.\n");
	    }else{
	        printf("Aluno em exame.\n");
	        scanf("%f",&n1);
	        printf("Nota do exame: %.1f\n",n1);
	        media=(media+n1)/2;
	        if(media>=5){
	            printf("Aluno aprovado.\nMedia final: %.1f\n",media);
	        }else{
	            printf("Aluno reprovado.\nMedia final: %.1f\n",media);
	        }
	    }
	}
}


