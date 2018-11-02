# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Ajude o Cupido
# Nível: 3
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1750

fodac = input()

lista = [int(i) for i in input().split()]
lista.sort()

cval1 = 0
cval2 = 0
for i in range(0, len(lista), 2):
    aux1 = lista[i+1]-lista[i]
    try:
        aux2 = lista[i+2]-lista[i+1]
    except:
        aux2 = lista[i+1]-lista[0]
    cval1 += min(aux1, 24 - aux1)
    cval2 += min(aux2, 24 - aux2)

print(min(cval1, cval2))

