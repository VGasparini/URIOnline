# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Rot13
# Nível: 2
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1249

def transforma(s):
    nova = ''
    for letter in s:
        if letter.isalpha():
            if letter.islower():
                nova += alpha_lower[(alpha_lower.index(letter)+13)%tam]
            else:
                nova += alpha_upper[(alpha_upper.index(letter)+13)%tam]
        else:
            nova += letter
    return nova
    
alpha_lower = [chr(i) for i in range(ord('a'),ord('z')+1)]
alpha_upper = [chr(i) for i in range(ord('A'),ord('Z')+1)]
tam = len(alpha_lower)

while True:
    try:
        print(transforma(input()))
    except EOFError:
        break
