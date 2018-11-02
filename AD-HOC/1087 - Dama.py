# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Dama
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1087

while True:
  x1,y1,x2,y2 = map(int,input().split())
  if (x1==x2 and y1==y2 and x1==0 and y1==0):
    break
  if((x1 == x2) and (y1 == y2)):
    print("0")
  elif(abs(x2-x1) == abs(y2-y1) or (x1 == x2 or y1 == y2)):
    print("1")
  else:
    print("2")
  
