# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Combinador
# Nível: 2
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1238

for i in range(int(input())):
    nova = ''
    a,b = input().split()
    if len(a)>len(b):
        for l in range(len(b)):
            nova += a[l]+b[l]
            if(l == len(b)-1): nova += a[l+1:]
    else:
        for l in range(len(a)):
            nova += a[l]+b[l]
            if(l == len(a)-1): nova += b[l+1:]
    print(nova)

