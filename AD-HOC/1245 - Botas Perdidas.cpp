// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Botas Perdidas
// Nível: 2
// Categoria: AD-HOC
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1245

#include <bits/stdc++.h>

using namespace std;

int main(){

    int n,i,j;

    while(cin >> n){
        char p[n];
        int b[n];
        int par = 0;

        for(i = 0; i < n; i++) cin >> b[i] >> p[i];

        for(i = 0; i < n; i++){
            for(j = i; j < n; j++){
                if(b[i] == b[j] && p[i] != p[j] && b[i] > 0){
                    par++;
                    b[i] = b[j] = 0;
                }
            }
        }
        cout << par << endl;
    }
}
