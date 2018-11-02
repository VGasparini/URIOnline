# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: OBI URI
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2062

n=input()
s = [j for j in input().split()]
saida = []
for j in s:
    if j[:2] == 'OB' and len(j)==3:
        saida.append('OBI')
    elif j[:2] == 'UR' and len(j)==3:
        saida.append('URI')
    else:
        saida.append(j)
print(*saida)
