# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Mensagem Oculta
# Nível: 2
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1272

n = int(input())
for i in range(n):
  text=[]
  text1 = list(map(str,input().split()))
  for j in range(len(text1)):
    text.append(text1[j][:1])
  a = "".join(text)
  print(a)
