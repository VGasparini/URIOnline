// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Jogo do Maior
// Nível: 1
// Categoria: AD-HOC
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1397

#include <stdio.h>

int main(void) {

	int n,i=0,a,b,ap=0,bp=0;
	scanf("%d",&n);
	while(n!=0)
	{
	    for(i = 1;i <= n;i++)
	    {
	        scanf("%d %d",&a,&b);
	        if(a > b)
	        {
	            ap++;
	        }else
	        {if(a < b)
	        {
	            bp++;
	        }
	        }
	    }
        printf("%d %d\n",ap,bp);
        ap=bp=0;
	    scanf("%d",&n);
	}
	return 0;
}

