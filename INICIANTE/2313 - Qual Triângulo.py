# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Qual Triângulo
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/2313

vetor = list(range(3))
vetor[0],vetor[1],vetor[2] = map(int, input().split())
vetor.sort(reverse=True)
if (vetor[0] < (vetor[1]+vetor[2])):
  if (vetor[0]**2 == (vetor[1]**2+vetor[2]**2)):
    ret = 'Retangulo: S'
  else:
    ret = 'Retangulo: N'
  if(vetor[0]==vetor[1] and vetor[1]==vetor[2]):
    print ("Valido-Equilatero")
  elif(vetor[0]!=vetor[1] and vetor[1]!=vetor[2]):
    print ("Valido-Escaleno")
  elif((vetor[0]==vetor[1] and vetor[1]!=vetor[2]) or (vetor[0]!=vetor[1] and vetor[1]==vetor[2]) or (vetor[0]==vetor[2] and vetor[2]!=vetor[1] )):
    print ("Valido-Isoceles")
  print(ret)
else:
  print("Invalido")
