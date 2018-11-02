// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Detetive Watson
// Nível: 2
// Categoria: AD-HOC
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1533

#include <stdio.h>
 
int main() {
 
int n, j, aux;
scanf("%d", &n);
while(n!=0){
if(n==0)
return 0;
int a[n], i, posicao[n];
for(i=0;i<n;i++)
{
scanf("%d", &a[i]);
posicao[i]=i+1;
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(a[i]>a[j])
{
aux=a[i];
a[i]=a[j];
a[j]=aux;
aux=posicao[i];
posicao[i]=posicao[j];
posicao[j]=aux;
}
}
}
printf("%d\n", posicao[n-2]);
scanf("%d", &n);
}
 
return 0;
}
