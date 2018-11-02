// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Embaralhando
// Nível: 1
// Categoria: AD-HOC
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1980

#include <bits/stdc++.h>

using namespace std;

long long int dp[20];

long long int fat(int n){
    if(n == 1 or n== 0) return 1;
    else{
        if(dp[n] != 0 ) return dp[n];
        return dp[n] = (fat(n-1) * n);
    }
}


int main(){
    dp[0] = 1;
    string s;
    cin >> s;
    while(s != "0"){
        cout << fat(s.length()) << endl;
        cin >> s;
    }
}
