"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa 
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale  população do país B, mantidas as taxas de crescimento
"""
a_hab = 80000
b_hab = 200000
loop = 0
while a_hab < b_hab:
    a_hab *= 1.03
    b_hab *= 1.015
    loop += 1
if b_hab < a_hab:
    print(f'{loop} anos')
