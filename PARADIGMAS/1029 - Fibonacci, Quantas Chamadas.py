# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Fibonacci, Quantas Chamadas?
# Nível: 2
# Categoria: PARADIGMAS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1029

def fib(n):

	fib = [0, 1]
	for i in range(n-1):
		fib.append(fib[-1] + fib[-2])
	return fib[-1]

def countfib(n):
	
	if n < 2:
		return 0
	if n == 2:
		return 2

	f1, f2, f3 = 2, 0, 0

	for i in range(n-2):
		d1 = f1 - f2
		d2 = f2 - f3
		f3 = f2
		f2 = f1
		f1 = f1 + d1 + d2

	return f1

n = int(input())
for i in range(n):
	m = int(input())
	print("fib({}) = {} calls = {}".format(m, countfib(m), fib(m)))
