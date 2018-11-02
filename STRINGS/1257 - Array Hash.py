# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Array Hash
# Nível: 3
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1257

alpha_lower = [chr(i) for i in range(ord('A'),ord('Z')+1)]

for i in range(int(input())):
    hashh = 0
    n = int(input())
    for j in range(n):
        s = input()
        for letter in range(len(s)):
            a = alpha_lower.index(s[letter])
            hashh+=(a+letter+j)
    print(hashh)
