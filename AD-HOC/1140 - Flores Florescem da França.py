# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Flores Florescem da França
# Nível: 3
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1140

palavras = list(map(str,input().split()))
while(palavras[0][0] != "*"):
    a = []
    for i in range(len(palavras)):
        a.append(palavras[i][0].lower())
    if(a.count(a[0]) == len(a)): print("Y")
    else: print("N")
    palavras = list(map(str,input().split()))

