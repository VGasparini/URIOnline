# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Frequência de Números
# Nível: 2
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1171

n = int(input())
m = []
for i in range(n):
	m.append(int(input()))
l = sorted(set(m))
for i in range(len(l)):
	print("{} aparece {} vez(es)".format(l[i], m.count(l[i])))
