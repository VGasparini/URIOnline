# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Colisão
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1618

n = int(input())
for i in range(n):
  Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, Rx, Ry = map(int,input().split())

  if (Ry>=Ay and Ry<=Dy):
    if (Rx>=Ax and Rx<=Bx):
      print(1)
    else:
      print(0)
  else:
    print(0)
