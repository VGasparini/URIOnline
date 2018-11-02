# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Abaixo da Diagonal Principal
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1184

m,linha,n,l,s,cont = [],[],0,[],0,0
op = input()
for y in range(12):
	linha = []
	for x in range(12):
		linha.append(float(input()))
	m.append(linha)
for i in range(12):
	for j in range(0,n):
		l.append(m[i][j])
		cont += 1
	s += sum(l)
	del l[:]
	n+=1
	
if(op == 'S'):
	print(s)
elif(op == 'M'):
	print("%.1f"%(s/cont))
