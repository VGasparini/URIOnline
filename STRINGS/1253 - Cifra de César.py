# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Cifra de César
# Nível: 2
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1253

def cifra(n,s):
    nova = ''
    for letra in s:
        nova += base[base.index(letra)-n]
    return nova

base = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


k = int(input())
for i in range(k):
    s = input()
    n = int(input())
    print(cifra(n,s))

