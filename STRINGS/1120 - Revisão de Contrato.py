# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Revisão de Contrato
# Nível: 3
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1120

while True:
  falho,original = input().split()
  if (falho == "0" and original == "0"):
    break
  else:
    novo = original
    while falho in novo:
      novo = original.replace(falho,"")
    if(novo == ""):
      novo = "0"
    print(int(novo))
