# Dado um número inteiro positivo, determine a sua decomposição em fatores primos calculando também a multiplicidade de cada fator

n = int(input("Digite um numero: "))
def isPrime(num):
    check = True
    for i in range (2, num):
        if num % i == 0:
            check = False
            break
    return check
def nextPrime(num):
    if isPrime(num) == False:
        return nextPrime(num+1)
    else: 
        return num
def fatorar(num):
    lista = []
    count = 2
    while num != 1:
        if num%count == 0:
            lista.append(count)
            num /= count
        else:
            count = nextPrime(count+1)
    return lista
print(fatorar(n))
