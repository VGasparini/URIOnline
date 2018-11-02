# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Escolha Difícil
# Nível: 5
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2702

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
for i in range(len(a)):
  if (b[i]>a[i]):
    c.append(b[i]-a[i])
print(sum(c))
