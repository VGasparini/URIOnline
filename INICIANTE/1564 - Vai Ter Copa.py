# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Vai Ter Copa?
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1564

while True:
  try:
    a = int(input())
    if (a==0):
        print("vai ter copa!")
    else:
        print("vai ter duas!")
  except EOFError:
    break
