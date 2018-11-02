# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Loop Musical
# Nível: 2
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1089

n = int(input())
while n != 0:
	ondas = list(map(int, input().split()))
	picos = 0
	ondas *= 2
	for i in range(n):
		if (ondas[i+1] > ondas[i] and ondas[i+1] > ondas[i+2]) or (ondas[i+1] < ondas[i] and ondas[i+1] < ondas[i+2]):
			picos += 1

	print(picos)
	n = int(input())
