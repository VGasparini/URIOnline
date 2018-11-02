# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Máquina de Verificação Au...
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1743

a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = [1,1,1,1,1]
c=[]
for i in range(len(a)):
  c.append(a[i]+b[i])
if(c == d):
  print("Y")
else:
  print("N")
