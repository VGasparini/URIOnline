# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Presente?!
# Nível: 5
# Categoria: ESTRUTURAS E BIBLIOTECAS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1425

while(True):
  i,a,d=2,1,0
  n,m = map(int,input().split())
  if(n==0 and m==0): break
  if(m>100): print("Let me try!")
  else:
    while(a>0 and a<n+1):
        if(a==m): #caso ja esteja na pedra certa logo no primeiro pulo
            d+=1
            break
        elif(a<m): #se tiver numa pedra atras
            if(a+(2*i-1)<n+1):
                a+=2*i-1
            else:
                a-=2*i-1
            i+=1
        else: #se tiver numa pedra pra frente
            if(a-(2*i-1)>0):
                a-=2*i-1
            else:
                a+=2*i-1
            i+=1
    if(d!=0): print("Let me try!")
    else: print("Don't make fun of me!")
