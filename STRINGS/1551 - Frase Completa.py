# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Frase Completa
# Nível: 3
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1551

for i in range(int(input())):
    s = input().upper()
    unicas = set()
    for j in s:
        if j.isalpha():
            unicas.add(j)
    if(len(unicas)==26):
        print("frase completa")
    elif(len(unicas)<26 and len(unicas)>=13):
        print("frase quase completa")
    else:
        print("frase mal elaborada")
