# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Divisão da Nlogônia
# Nível: 2
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1091

n = int(input())
while (n!=0):
    x0,y0 = map(int,input().split())
    for i in range(n):
        x,y = map(int,input().split())
        if(x==x0 or y==y0):
            print("divisa")
        else:
            if(x>x0 and y>y0):
                print("NE")
            elif(x>x0 and y<y0):
                print("SE")
            elif(x<x0 and y>y0):
                print("NO")
            else:
                print("SO")
    n = int(input())

