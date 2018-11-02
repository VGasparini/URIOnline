# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: CPF 1
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1769

while (True):  
  try:
    a = list(input().split("-"))
    b = a[0].replace(".","")
    c,d = [],[]
    for i in range(9):
      c.append(int(b[i])*(i+1))
      d.append(int(b[i])*(9-i))
    rc = sum(c)%11
    if(rc==10): rc=0
    rd = sum(d)%11
    if(rd==10): rd=0
    if (rc == int(a[1][0]) and rd == int(a[1][1])):
      print("CPF valido")
    else:
      print("CPF invalido")
  except EOFError:
    break
