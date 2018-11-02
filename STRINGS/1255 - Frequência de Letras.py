# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Frequência de Letras
# Nível: 2
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1255

def conta(s):
    for letter in s:
        try:
            contagem[alpha_lower.index(letter)][1] += 1
        except:
            continue


alpha_lower = [chr(i) for i in range(ord('a'),ord('z')+1)]

for i in range(int(input())):
    contagem = [[chr(i),0] for i in range(ord('a'),ord('z')+1)]
    s = input().lower()
    conta(s)
    contagem.sort(key=lambda x: x[1],reverse= True)
    printar = ''
    printar += contagem[0][0]
    for i in range(1,len(contagem)):
        if contagem[i][1] == contagem[0][1]: printar += contagem[i][0]
        else: break
    print(printar)

