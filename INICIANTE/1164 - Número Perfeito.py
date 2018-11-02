# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Número Perfeito
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1164

n = int(input())
for i in range(n):
    a = []
    b = int(input())
    for j in range(int(b-1)):
        if(b%(j+1) == 0): a.append(j+1)

    if(sum(a)==b): print(b,"eh perfeito")
    else: print(b,"nao eh perfeito")

