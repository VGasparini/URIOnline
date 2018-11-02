# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Trigo no Tabuleiro
# Nível: 1
# Categoria: MATEMÁTICA
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1169

n = int(input())
for i in range(n):
  j = float(input())
  j = 2**j/12000
  j = int (j)
  print("{} kg".format(j))
