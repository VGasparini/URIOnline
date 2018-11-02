# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Preenchimento de Vetor IV
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1179

par = []
impar = []

def printp(x):
  for u in range(0,len(x)):
      print("par[{}] = {}".format(u,x[u]))
def printi(x):
  for u in range(0,len(x)):
      print("impar[{}] = {}".format(u,x[u]))

for i in range(0,15):
  n=int(input())
  if(n%2==0):
    par.append(n)
    if(len(par)==5):
      printp(par)
      par=[]
  else:
    impar.append(n)
    if(len(impar)==5):
      printi(impar)
      impar=[]

printi(impar)
printp(par)
