# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Fuso Horário
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2057

S,T,F = map(int,input().split())
if S==0:
    S=24
chegada= S+T+F
if chegada>24:
    chegada=chegada-24
    print(chegada)
elif chegada==24:
    chegada=0
    print(chegada)
else:
    print(chegada)
