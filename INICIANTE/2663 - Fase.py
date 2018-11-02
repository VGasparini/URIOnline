# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Fase
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2663

n = int(input())
m = int(input())
num,cont = [],0
for i in range(n):
    num.append(int(input()))
uni = list(sorted(set(num)))[::-1]
for i in uni:
    if cont < m:
        cont += num.count(i)
print(cont)
