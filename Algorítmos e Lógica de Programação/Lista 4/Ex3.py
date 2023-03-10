"""
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
intercalados dos dois outros vetores.Imprima os três vetores.
"""
import random
vetor1 =  random.sample(range(100), 10)
vetor2 =  random.sample(range(100), 10)
vetor3 = []
k = 0
while k<20:
    if k%2==0:
        vetor3.append(vetor1[int(k/2)])
    else:
        vetor3.append(vetor2[int((k-1)/2)])
    k += 1
print(f"Vetor 1: {vetor1}\nVetor 2: {vetor2}\nVetor 3: {vetor3}")