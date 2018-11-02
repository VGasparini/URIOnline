# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Getline One
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1216

cont,c = 0,[]
while (True):  
  try:
    a = input()
    b = int(input())
    c.append(b)
    cont+=1
  except EOFError:
    print("{:.1f}".format(sum(c)/cont))
    break
