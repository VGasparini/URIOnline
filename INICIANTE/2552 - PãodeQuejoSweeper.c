// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: PãodeQuejoSweeper
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2552

#include <stdio.h>
int main ()
{
    int m,n,cont,i,j;

    while (scanf ("%d %d",&m,&n) != EOF){
    	
    	int v[m][n];
    	
    	for (i=0;i<m;i++){
    		for (j=0;j<n;j++){
    			scanf("%d",&v[i][j]);
    		}
    	}
    	
    	int k[110][110] = {};
    	
    	for(i=0;i<m;i++){
        	for (j=0;j<n;j++){
    			  if(v[i][j] == 0){
          		if (v[i][j-1] == 1 && j-1 >= 0) k[i][j] += 1;
          		if (v[i][j+1] == 1 && j < n-1) k[i][j] += 1;
          		if (v[i-1][j] == 1 && i-1 >= 0) k[i][j] += 1;
          		if (v[i+1][j] == 1 && i < m-1) k[i][j] += 1;
          		}
        		else{
        			if(v[i][j] == 1) k[i][j] = 9;
        		}
      }
    }
    for (i=0;i<m;i++){
    		for (j=0;j<n;j++){
    			v[i][j]=0;
    	}
    }
	for(i=0;i<m;i++){
      for (j=0;j<n;j++){
        printf("%d",k[i][j]);
      }printf("\n");
    }
  }
}
