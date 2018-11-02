# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: A Última Criança Boa
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2023

ori,nomes,i = [],[],0
while True:
    try:
        t = input()
        ori.append(t)
        nomes.append((t.lower(),i))
        i+=1
    except EOFError:
        nomes.sort(key=lambda x: x[0])
        print(ori[int(nomes[-1][1])])
        break
