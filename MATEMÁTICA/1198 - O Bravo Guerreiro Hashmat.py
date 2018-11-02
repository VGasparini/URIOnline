# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: O Bravo Guerreiro Hashmat
# Nível: 1
# Categoria: MATEMÁTICA
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1198

while True:
    try:
        a,b = map(int,input().split())
        print(abs(a-b))
    except EOFError:
        break
