"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
while True:
  num = float(input("Digite uma nota entre 0 e 10: "))
  if 0 <= num <= 10:
      print("Validado.")
      break
  else:
      print("Valor Invalido.")
