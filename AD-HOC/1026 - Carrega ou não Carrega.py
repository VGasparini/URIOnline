# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Carrega ou não Carrega?
# Nível: 2
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1026

while(1):
	try:
		a, b = list(map(int, input().split()))
		print(a^b)
	except EOFError:
		break
