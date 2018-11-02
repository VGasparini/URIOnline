# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Sequência Espelho
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2157

n = int(input())
for i in range(n):
  s = ''
  a,b = map(int,input().split())
  for j in range(a,b+1):
    s += str(j)
  for j in reversed(range(a,b+1)):
    s += str(j)[::-1]
  print (s)
