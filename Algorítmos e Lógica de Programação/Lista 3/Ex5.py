# Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
num1 = int(input("Primeiro Numero: "))
num2 = int(input("Segundo Numero: "))
def mdc(n1, n2):
    a = max(n1, n2)
    b = min(n1, n2)
    if n1 == n2:
        return a
    else:
        while a > b:
            a = a-b
        if b > a:
            mdc(b, a)
            return a
        else:
            return a
print(mdc(num1, num2))