# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Blobs
# Nível: 1
# Categoria: MATEMÁTICA
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1170

n = int(input())
for i in range(n):
  a = float(input())
  cont = 0
  while True:
    a = a/2
    cont+=1
    if(a<=1):
      print(cont,"dias")
      break
