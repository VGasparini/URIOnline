# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: O jogo Matemático de Paula
# Nível: 2
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1192

n = int(input())
for i in range(n):
    mai = 0
    texto = input()
    if any(x.isupper() for x in texto):
        mai = 1
    a,b = int(texto[0]),int(texto[2])
    if (a==b):
        print(a*b)
    else:
        if (mai==1):
            print(b-a)
        else:
            print(a+b)

