# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: LED
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1168

for k in range(int(input())):
  a = str(input())
  t=0
  for i in range(len(a)):
    if(a[i]=='0'):
      t+=6
    elif(a[i]=='1'):
      t+=2
    elif(a[i]=='2'):
      t+=5
    elif(a[i]=='3'):
      t+=5
    elif(a[i]=='4'):
      t+=4
    elif(a[i]=='5'):
      t+=5
    elif(a[i]=='6'):
      t+=6
    elif(a[i]=='7'):
      t+=3
    elif(a[i]=='8'):
      t+=7
    elif(a[i]=='9'):
      t+=6
  print(t,"leds")
