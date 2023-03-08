# Verifique se um inteiro positivo n é primo.
num = int(input("Digite um numero: "))
def isPrime(n):
    check = True
    for i in range(2, n):
        if num % i == 0:
            check = False
            break
    return check
if isPrime(num) == True:
    print(f"O numero {num} é primo.")
else:
    print(f"O numero {num} não é primo.")