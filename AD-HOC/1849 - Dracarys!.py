# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Dracarys!
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1849

while(True):
	try:
	  a,b,c,d = map(int,input().split())
	  e = min(a,b)
	  f = min(c,d)

	  e += f

	  g = min(max(a, b), max(c, d))
	  h = min(e, g)

	  print(h*h)
	except:
	  break

