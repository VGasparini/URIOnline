# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Área Inferior
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1188

op = input()
mat = []
for m in range(12):
    temp = []
    for n in range(12):
        temp.append(float(input()))
    mat.append(temp)
    del temp
j,k,cont,soma = 1,10,0,0
for m in range(11,6,-1):
    for n in range(j,k+1):
        soma+=mat[m][n]
        cont+=1
    j+=1
    k-=1

if (op == 'S'):
    print("%.1f"%(soma))
else:
    print("%.1f"%(soma/cont))

