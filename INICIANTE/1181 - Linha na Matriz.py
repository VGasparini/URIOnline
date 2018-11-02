# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Linha na Matriz
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1181

l = int(input())
op = input()
m=[]
for y in range(12):
	linha = []
	for x in range(12):
		linha.append(float(input()))
	m.append(linha)
if (op == 'S'):
  print(sum(m[l]))
elif (op == 'M'):
	print("{:.1f}".format(sum(m[l])/12))
