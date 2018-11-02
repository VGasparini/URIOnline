# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Teclado Zoeiro
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2692

n,m = map(int,input().split())
alpha = dict()
for i in range(n):
    s,ss = input().split()
    alpha[s]=ss
    alpha[ss]=s
for i in range(m):
    s,ss = input(),''
    for k in s:
        try:
            ss += alpha[k]
        except:
            ss += k
    print(ss)
    del ss
