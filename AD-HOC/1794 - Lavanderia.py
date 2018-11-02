# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Lavanderia
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1794

n = int(input())
la,lb = map(int,input().split())
sa,sb = map(int,input().split())
if ((n>=la and n<=lb) and (n>=sa and n<=sb)):
  print("possivel")
else:
  print("impossivel")
