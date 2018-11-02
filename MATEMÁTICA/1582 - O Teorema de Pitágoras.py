# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: O Teorema de Pitágoras
# Nível: 1
# Categoria: MATEMÁTICA
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1582

def ckpytha(a,b,c):
  maxi=a
  s1=b
  s2=c
  if(b>maxi and b>c):
    maxi=b
    s1=a
    s2=c
    return (maxi*maxi)==(s1*s1)+(s2*s2)
  elif(c>maxi and c>b):
    maxi=c
    s1=b
    s2=a
    return (maxi*maxi)==(s1*s1)+(s2*s2)
  else:
    return (maxi*maxi)==(s1*s1)+(s2*s2)
    
def gcd(a,b):
  tmp=0;
  while(b!=0):
    tmp=b
    b=a%b
    a=tmp
  return a

while True:
  try:
    a,b,c = map(int,input().split())
    if(ckpytha(a,b,c)==1 and gcd(gcd(a,b),c)==1):
      print("tripla pitagorica primitiva")
    elif(ckpytha(a,b,c)):
      print("tripla pitagorica")
    else:
      print("tripla")
  except EOFError:
    break


