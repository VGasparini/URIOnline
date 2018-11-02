# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Alarme Despertador
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1103

while True:  
  n = list(map(int,input().split()))
  if n.count(0)==4:
    break
  else:
    if(n[0] == 0): inicio = 24*60 + n[1]
    else: inicio = n[0]*60 + n[1]
             
    if(n[2] == 0): fim = 24*60 + n[3]
    else: fim = n[2]*60 + n[3]
             
    if(fim > inicio): print(fim-inicio)
    else: print(24*60 - (inicio-fim))
