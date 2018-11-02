# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Coleção de Pomekon
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2174

s = set()
for i in range(int(input())):
    s.add(input())
print("Falta(m) {} pomekon(s).".format(151-len(s)))
