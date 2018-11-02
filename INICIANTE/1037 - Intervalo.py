# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Intervalo
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1037

a = float(input())
if(a >= 0 and a <= 25):
    print("Intervalo [0,25]")
else:
    if(a > 25 and a <= 50):
        print("Intervalo (25,50]")
    else:
        if(a > 50 and a <= 75):
            print("Intervalo (50,75]")
        else:
            if( a> 75 and a <= 100):
                print("Intervalo (75,100]")
            else:
                print("Fora de intervalo")

