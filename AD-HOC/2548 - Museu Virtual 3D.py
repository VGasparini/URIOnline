# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Museu Virtual 3D
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2548

while True:
  try:
    m,n = map(int,input().split())
    a = list(map(int,input().split()))
    a = sorted(a,reverse=True)
    b = []
    for i in range(n):
      b.append(a[i])
    print(sum(b))
  except EOFError:
    break
