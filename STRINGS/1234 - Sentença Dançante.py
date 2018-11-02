# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Sentença Dançante
# Nível: 2
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1234

while True:
    try:
        s = input()
        nova = ''
        mai = True
        for l in s:
            if l == ' ':
                nova += ' '
                continue
            if mai:
                nova += l.upper()
                mai = False
            else:
                nova += l.lower()
                mai = True
        print (nova)
    except EOFError:
        break

