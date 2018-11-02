# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: A Resposta de Theon
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1858

a = int(input())
y = []
e = 1
d = 0
y=list(map(int,input().split()))
c = y[d]
for d in range(a):
  if y[d]<c:
    c=y[d]
    e=d+1
print(e)
