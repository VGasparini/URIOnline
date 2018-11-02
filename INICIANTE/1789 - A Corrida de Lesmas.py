# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: A Corrida de Lesmas
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1789

while True:
  try:
    n = int(input())
    l = list(map(int,input().split()))
    n = max(l)
    if n<10:
      print(1)
    elif n>=20:
      print(3)
    else:
      print(2)
  except EOFError:
    break
