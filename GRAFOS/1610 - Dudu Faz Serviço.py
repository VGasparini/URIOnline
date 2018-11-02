# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Dudu Faz Serviço
# Nível: 2
# Categoria: GRAFOS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1610

#include <bits/stdc++.h>

using namespace std;

vector<vector<int> > v;
vector<int> visited;
bool cicle;

void dfs(int n)
{
	visited[n] = 1;
	if (cicle) return;
	for (int i = 0 ; i < v[n].size(); i++){
		if (visited[v[n][i]] == 1){
			cicle = true;
			return;
		}
		else if (visited[v[n][i]] == 0)
			dfs(v[n][i]);
	}	
	visited[n] = 2;
}

int main (){
	int c, n, m, u, w;
	
	cin >> c;
	while(c--)	{
		cin >> n >> m;
		v.assign(n, vector<int> ());
		visited.assign(n,0);
		
		for (int i = 0 ; i < m; i++){
			cin >> u >> w;
			v[u-1].push_back(w-1);
		}
		cicle = false;
		for (int i = 0 ; i < n; i++){
			if (!visited[i])
				dfs(i);
			if (cicle) break;
		}
		if (cicle) cout << "SIM\n";
		else cout << "NAO\n";
		visited.clear();
		v.clear();
	}
}

