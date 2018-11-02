// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Abracadabra
// Nível: 1
// Categoria: STRINGS
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2484

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,m=0;
    string a;
    while(cin >> a){
        for(int i = 0 ; i < a.size() ; i++) {
            for(int j = 0 ; j < a.size() ; j++) {
                if(j < i)
                    cout << " ";
                else
                  if(j == a.size() - 1)
                    cout << a[j-i];
                  else
                    cout << a[j-i] << " ";
            }
            cout << endl;
        }
     cout << endl;
    }
    return 0;
} 
