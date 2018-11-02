# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Corrida
# Nível: 1
# Categoria: MATEMÁTICA
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2516

while True:
  try:
    d,a,b = map(int,input().split())
    if(b>=a):
      print("impossivel")
    else:
      print("%.2f"%(d/(a-b)))
  except EOFError:
    break
