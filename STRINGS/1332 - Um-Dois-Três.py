# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Um-Dois-Três
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1332

for i in range(int(input())):
    t = input()
    
    if(len(t)>3):
        print(3)
    else:
        s = 0
        if (t[0:1]=='o'):
            s+=1
        if (t[1:2]=='n'):
            s+= 1
        if (t[2:3]=='e'):
            s += 1
        if(s>=2):
            print(1)
        else:
            print(2)
