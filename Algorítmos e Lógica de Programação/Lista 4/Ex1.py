# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
import random
numeros = random.sample(range(100), 10)
def isSorted(lista):
    k = 0
    while k < len(lista)-1:
        if lista[k] > lista[k+1]:
            return False
        k += 1
    return True

while isSorted(numeros) == False:
    loop = 0
    while loop < len(numeros)-1:
        if numeros[loop] > numeros[loop+1]:
            numeros[loop], numeros[loop+1] = numeros[loop+1], numeros[loop]
        loop +=1

print(f"O menor número é {numeros[0]}, e o maior número é {numeros[-1]}")
    