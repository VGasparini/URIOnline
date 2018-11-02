// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Jogando Cartas Fora
// Nível: 2
// Categoria: ESTRUTURAS E BIBLIOTECAS
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1110

#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;

    while( n!= 0){
        if(n == 0) break;
        deque<int> cartas;
        for(int i = 1; i <= n; i++) cartas.push_back(i);

        cout << "Discarded cards: ";
        while(cartas.size() >= 2){
            if(cartas.size() != 2) cout << cartas.front() << ", ";
            else cout << cartas.front() << endl;
            cartas.pop_front();
            cartas.push_back(cartas.front());
            cartas.pop_front();
        }
        cout << "Remaining card: "<< cartas.front() << endl;
        cin >> n;
    }
    return 0;
}

