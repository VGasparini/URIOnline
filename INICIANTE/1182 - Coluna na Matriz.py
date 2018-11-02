# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Coluna na Matriz
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1182

l = int(input())
op = input()
m,linha,coluna=[],[],[]
for y in range(12):
	linha = []
	for x in range(12):
		t=float(input())
		if (x == l):
			coluna.append(t)
if (op == 'S'):
  print(sum(coluna))
elif (op == 'M'):
	print("{:.1f}".format(sum(coluna)/12))
