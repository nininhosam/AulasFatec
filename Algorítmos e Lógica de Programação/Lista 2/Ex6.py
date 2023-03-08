"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. 
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
  a.+ Salário Bruto : R$
  b.-IR (11%) : R$
  c.-INSS (8%) : R$
  d.-Sindicato ( 5%) : R$
  e.= Salário Liquido : R$
"""
hourly_wage = float(input("Salário horario (R$): "))
work_hours = int(input("Horas trabalhadas: "))
gross = (hourly_wage*work_hours)
ir = gross*0.11
inss = gross*0.08
sind = gross*0.05
net = gross*0.76
print(f"Salário: R${gross:.2f}\nIR: R${ir:.2f}\nINSS: R${inss:.2f}\nSindicato: R${sind:.2f}\nLíquido: R${net:.2f}")
