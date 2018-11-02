# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Enigma
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2880

s = list(input())
crib = list(input())
cont = 0
for i in range(len(s)-len(crib)+1):
  flag = False
  tmp = s[i:len(crib)+i]
  for j in range(len(tmp)):
    if tmp[j]==crib[j]:
      flag = True
      break
  if not flag:
    cont+=1
    flag = False
print(cont)


