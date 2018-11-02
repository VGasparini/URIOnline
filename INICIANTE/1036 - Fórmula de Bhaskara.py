# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Fórmula de Bhaskara
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1036

a,b,c = map(float,input().split())
delta=(b*b)-(4*a*c)
if(delta<0 or a==0):
    print("Impossivel calcular")
else:
    x1=(-b+(delta)**(1/2))/(2*a)
    x2=(-b-(delta)**(1/2))/(2*a)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))

