# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Instruções do Robô
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1574

n = int(input())
for i in range(n):
    m = int(input())
    p = 0
    k = []
    for j in range(m):
        a = input()
        if(a=="LEFT"):
            p-=1
            k.append(-1)
        elif(a=="RIGHT"):
            p+=1
            k.append(1)
        else:
            l = int(a[8:])
            p+=k[l-1]
            k.append(k[l-1])
    print(p)

