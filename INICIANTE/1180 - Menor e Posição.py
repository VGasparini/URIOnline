# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Menor e Posição
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1180

oie = input()
vetor = list(map(int, input().split()))
min = min(vetor)
p = vetor.index(min)
print("Menor valor: %d\nPosicao: %d"%(min,p))
