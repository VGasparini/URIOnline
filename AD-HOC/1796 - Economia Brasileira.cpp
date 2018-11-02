// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Economia Brasileira
// Nível: 1
// Categoria: AD-HOC
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1796

#include <bits/stdc++.h>

using namespace std;
int main(){

  int n,m,p=0;

  cin >> n;
  for(int i=0;i<n;i++){
    scanf("%d",&m);
    if(m==0) p--;
    else p++;
  }
  if(p>=0) cout << "N" << endl;
  else cout << "Y" << endl;
}
