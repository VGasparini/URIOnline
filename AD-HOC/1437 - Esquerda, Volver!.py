# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Esquerda, Volver!
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1437

n = int(input())
while(n!=0):
  a = input()
  d = a.count("D")
  e = a.count("E")
  if (d>4):
    d = 4*(float(d/4)-int(d/4))
  if (e>4):
    e = 4*(float(e/4)-int(e/4))
  ang = 90*d-90*e
  if(ang==0 or ang==360 or ang==-360):
    print("N")
  elif(ang==90 or ang==-270):
    print("L")
  elif(ang==180 or ang==-180):
    print("S")
  elif(ang==270 or ang==-90):
    print("O")
  n = int(input())
