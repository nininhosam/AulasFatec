"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendidaem latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Obs. : somente são vendidos um número inteiro de latas.
"""
area = float(input("Área a ser pintada (m²): "))
tinta = area/3
if tinta%18 == 0:
    latas = int(tinta/18)
else:
    latas = int(tinta//18+1)
price = latas*80
print(f"Serão necessárias {latas} lata(s) de tinta, totalizando R${price:.2f}")