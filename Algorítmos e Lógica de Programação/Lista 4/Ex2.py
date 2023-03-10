"""
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista
PAR e os números ímpares na lista IMPAR. Imprima as três listas.
"""
import random
numlist = random.sample(range(100), 20)
pares = []
impares = []
for n in numlist:
    if n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f"Pares: {pares}\nImpares: {impares}")