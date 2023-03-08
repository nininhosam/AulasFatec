# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
segundos_total = segundos + (60 * (minutos + (60 * (horas + (24 * dias)))))
print("o total em segundos é de {}".format(segundos_total))
