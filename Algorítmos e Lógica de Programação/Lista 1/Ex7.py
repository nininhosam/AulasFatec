# Converta uma temperatura digitada em Celsius para Fahrenheit.F = 9*C/5 + 32
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = 9*(celsius/5)+32
print("{}° Celsius é equivalente a {}° Fahrenheit".format(celsius, fahrenheit))
