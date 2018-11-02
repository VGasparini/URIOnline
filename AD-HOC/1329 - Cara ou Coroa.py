# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Cara ou Coroa
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1329

n = int(input())
while (n != 0):
  j = list(map(int,input().split()))
  print("Mary won",j.count(0),"times and John won",j.count(1),"times")
  n = int(input())
