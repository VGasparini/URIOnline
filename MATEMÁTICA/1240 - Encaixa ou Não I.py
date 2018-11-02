# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Encaixa ou Não I
# Nível: 1
# Categoria: MATEMÁTICA
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1240

n = int(input())
for i in range(n):
    a,b = map(str,input().split())
    c = a[-len(b):]
    if (c == b): print("encaixa")
    else: print("nao encaixa")

