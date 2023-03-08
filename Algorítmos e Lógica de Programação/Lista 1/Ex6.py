# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem
distance = float(input("Digite a distância em Quilômetros: "))
velocity = float(input("Digite a velocidade média em Km/H: "))
time = distance/velocity
print("A viagem deve durar {} horas".format(time))
