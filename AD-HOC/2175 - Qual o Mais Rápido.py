# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Qual o Mais Rápido?
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2175

v = list(map(float,input().split()))
n = ["Otavio","Bruno","Ian","Empate"]
m = min(v)
s = sorted(v)
if (s[0]==s[1]):
    print(n[3])
else:
    print(n[v.index(m)])
