// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Matriz 123
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1534

#include <stdio.h>

int main(){
  int n,m,par,i,j;
 
  while(scanf("%d",&n) != EOF){
    m = n-1;
    par = n%2;
    for(i=0;i<n;i++){
      for(j=0;j<n;j++){
        if (i == j){
          if (par != 0 && i == ((n-1)/2) && j == ((n-1)/2)){
            printf("2");
          }
          else printf("1");
        }
        else if (j == m){
          printf("2");
        }
        else{
          printf("3");
        }
      }
       m--;
      printf("\n");
    }
  }
}
