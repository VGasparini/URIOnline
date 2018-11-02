# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Criptografia
# Nível: 2
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1024

def primeira_passada(palavra):
    nova = ''
    for i in range(len(palavra)):
        if palavra[i].isalpha():
            nova += chr(ord(palavra[i])+3)
        else:
            nova += palavra[i]
    return nova

def segunda_passada(palavra):
    return palavra[::-1]

def terceira_passada(palavra):
    meio = int(len(palavra)/2)
    met1 = palavra[:meio]
    met2 = palavra[meio:]
    nova = ''
    for i in range(len(met2)):
        nova += chr(ord(met2[i])-1)
    return met1+nova

n = int(input())
for k in range(n):
    s = input()
    print(terceira_passada(segunda_passada(primeira_passada(s))))

