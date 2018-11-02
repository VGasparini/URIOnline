// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Jogatina UFPR
// Nível: 1
// Categoria: INICIANTE
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2543

#include <bits/stdc++.h>
#define endl '\n'

using namespace std;
int main() {
  
  string chave,atual;
  int n,ver,cont;
  while(cin >> n >> chave){
  cont = 0;
  for(int i = 0;i < n; i++){
    cin >> atual >> ver;
    if(atual == chave && ver == 0) cont++;
  }
  cout << cont << endl;
}
}
