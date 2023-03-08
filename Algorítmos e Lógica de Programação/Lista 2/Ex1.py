"""
Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
"""
a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))
if a+b > c and b+c > a and a+c > b:
    print("O triângulo é valido.")
    if a == b and b == c:
        print("O triângulo é equilatero")
    elif a != b and b != c and a != c:
        print("O triângulo é escaleno")
    else:
        print("O triângulo é isósceles")
else:
    print("O triângulo é invalido.")
