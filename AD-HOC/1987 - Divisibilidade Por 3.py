# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Divisibilidade Por 3
# Nível: 1
# Categoria: AD-HOC
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1987

while True:
    try:
        a,n = input().split()
        n = list(n)
        s = sum([int(i) for i in n])
        print(s,'sim') if s%3==0 else print(s,'nao') 
    except EOFError:
        break
