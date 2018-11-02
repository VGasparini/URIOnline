# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Funções
# Nível: 1
# Categoria: MATEMÁTICA
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1555

n = int(input())
text = ['Carlos ganhou','Beto ganhou','Rafael ganhou']
for i in range(n):
  x,y = map(int,input().split())
  r = (3*x)**2+y**2
  b =  2*(x**2) + (5*y)**2
  c = -100*x + y**3
  v = [c,b,r]
  print(text[v.index(max(v))])
