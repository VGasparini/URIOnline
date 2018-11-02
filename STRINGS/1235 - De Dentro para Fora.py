# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: De Dentro para Fora
# Nível: 2
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1235

def transforma(s):
    meio = len(s)//2
    s1 = s[-meio:]
    s2 = s[:-meio]
    return s2[::-1]+s1[::-1]

for i in range(int(input())):
    s = input()
    print(transforma(s))
