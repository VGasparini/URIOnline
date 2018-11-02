# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Adivinha
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1547

n = int(input())
for i in range(n):
  q,l = [],[]
  a,b = map(int,input().split())
  p = list(map(int,input().split()))
  for j in range(len(p)):
    q.append(abs(b-p[j]))
  try:
    print(p.index(0)+1)
  except:
    print(q.index(min(q))+1)
