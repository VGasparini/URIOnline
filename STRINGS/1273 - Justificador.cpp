// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Justificador
// Nível: 2
// Categoria: STRINGS
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1273

#include <bits/stdc++.h>
#define debug(x) cout << #x " = " << (x) << endl
#define endl '\n'

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);cin.tie(NULL);
  int t;
  int first = true;
  while (cin >> t && t) {
    vector<string> a(t);
    int mmax = 0;
    for (auto &i : a) {
      cin >> i;
      mmax = max<int>(mmax, i.size());
    }
    if (!first)
      cout << endl;
    for (auto &i : a) {
      int m = mmax - i.size();
      cout << string(m, ' ') << i << endl;
    }
    first = false;
  }
  return 0;
}

