""" 
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
"""
rodado = float(input("Quantos quilômetros foram percorridos com o carro? "))
dias_alugados = int(input("Por quantos dias este carro foi alugado? "))
final_price = (rodado*0.15)+(dias_alugados*60)
print("O preço final a ser pago é de R${}".format(final_price))
