# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Acima da Média
# Nível: 2
# Categoria: MATEMÁTICA
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1214

for i in range(int(input())):
    n = list(map(int,input().split()))
    a = n.pop(0)
    med = sum(n)/a
    cont = 0
    for x in range(len(n)):
        if(n[x]>med): cont+=1
    print("{:.3%}".format(cont/a))

