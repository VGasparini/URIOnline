# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Teste de Seleção 1
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1035

a,b,c,d = map(int,input().split())
if (b>c and d>a and (c+d)>(a+b) and (c>0 and d>0) and (a%2==0)): print("Valores aceitos")
else: print("Valores nao aceitos")

