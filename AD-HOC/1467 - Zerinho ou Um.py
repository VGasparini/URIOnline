# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Zerinho ou Um
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1467

while True:  
  try:
    t = input().split()
    v = ['A','B','C','*']
    if (t.count('1')==2):
    
      print(v[t.index('0')])
    elif (t.count('0')==2):
    
      print(v[t.index('1')])
    else:
      print(v[3])
  except EOFError:
    break
