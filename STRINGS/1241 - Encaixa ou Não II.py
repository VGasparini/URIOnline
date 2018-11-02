# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Encaixa ou Não II
# Nível: 2
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1241

for i in range(int(input())):
    a,b = input().split()
    if (a[-len(b):] == b): print('encaixa')
    else: print('nao encaixa')

