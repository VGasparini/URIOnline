# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Pedra-papel-tesoura-lagar...
# Nível: 1
# Categoria: STRINGS
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1873


for i in range(int(input())):
    a,b = input().split()
    if(a == b): print('empate')
    else:
        if(a == 'tesoura'):
            if(b == 'papel'): print ('rajesh')
            elif(b == 'lagarto'): print ('rajesh')
            else: print('sheldon')
        elif(a == 'papel'):
            if(b == 'pedra'): print ('rajesh')
            elif(b == 'spock'): print ('rajesh')
            else: print('sheldon')
        elif(a == 'pedra'):
            if(b == 'lagarto'): print ('rajesh')
            elif(b == 'tesoura'): print ('rajesh')
            else: print('sheldon')
        elif(a == 'lagarto'):
            if(b == 'spock'): print ('rajesh')
            elif(b == 'papel'): print ('rajesh')
            else: print('sheldon')
        elif(a == 'spock'):
            if(b == 'tesoura'): print ('rajesh')
            elif(b == 'pedra'): print ('rajesh')
            else: print('sheldon')

