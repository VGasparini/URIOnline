# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Top N
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1943

n = int(input())
m = [1, 3, 5, 10, 25, 50 ,100]
for i in range(len(m)):
    if(n <= m[i]):
        print("Top",m[i])
        break

