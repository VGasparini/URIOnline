# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Zero vale Zero
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1871

a,b=input().split()
while(a!='0' and b!='0'):
    print(str(int(a)+int(b)).replace('0',''))
    a,b=input().split()
