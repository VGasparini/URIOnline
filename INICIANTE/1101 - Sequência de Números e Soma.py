# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Sequência de Números e Soma
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1101

a, b = map(int, input().split())
soma = 0

while(a > 0 and b > 0):
    if(a > b):
        for i in range(b, a + 1):
            print(b, end=" ")
            soma += b
            b += 1
        print("Sum=%i" %soma)
        
    else:
        for i in range(a, b + 1):
            print(a, end=" ")
            soma += a
            a += 1
        print("Sum=%i" %soma)
    soma = 0
    a, b = map(int, input().split())

