// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Soma de Fatoriais
// Nível: 1
// Categoria: MATEMÁTICA
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1161

#include<stdio.h>

long long int fatorial (numero);

int main()
{
	long long int m,n,soma;
	long long int f1,f2;
	f1=f2=1;
	while(scanf("%lld %lld",&m,&n) != EOF){
		
		soma = fatorial(m) + fatorial(n);
		printf("%lld\n",soma);
	}
}

long long int fatorial (numero) {
if ((numero==1) || (numero==0)){
	return 1;
}             
   else{
      return numero * fatorial(numero-1);
   }
}
