# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Fibonacci Fácil
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1151

n = int(input())
a = []
for i in range(n):
    if(i==0 or i==1):  a.append(i)
    else:
        a.append(a[i-2]+a[i-1])
for i in range(len(a)):

    if(i==(len(a)-1)): print(a[i])
    else: print(a[i],"",end="")

